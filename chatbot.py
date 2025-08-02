import streamlit as st
import openai
import os
from dotenv import load_dotenv
import PyPDF2
import io

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(page_title="ToanTran Chatbot", page_icon="🤖", layout="wide")


def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Lỗi khi đọc file PDF: {str(e)}")
        return None


def create_context_message(context_text, tone=""):
    """Create system message with context"""
    base_prompt = "You are a helpful AI assistant."

    if tone:
        base_prompt = f"Bạn là một trợ lý AI. Hãy trả lời với tông giọng {tone}."

    if context_text:
        base_prompt += f"\n\nTham khảo những thông tin sau khi trả lời:\n\n{context_text}\n\nHãy sử dụng thông tin này để trả lời câu hỏi của người dùng một cách chính xác và chi tiết."

    return base_prompt


def initialize_openai():
    """Initialize OpenAI client with API key"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error(
            "⚠️ OpenAI API key not found! Please set OPENAI_API_KEY in your .env file"
        )
        st.stop()

    # For OpenAI v1.0+ (recommended)
    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        return client
    except ImportError:
        # Fallback for older OpenAI versions
        openai.api_key = api_key
        return openai


def get_chatgpt_response(messages, client=None):
    """Get response from ChatGPT API"""
    try:
        # For OpenAI v1.0+ (recommended)
        if hasattr(client, "chat"):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1000,
                temperature=0.7,
            )
            return response.choices[0].message.content
        else:
            # Fallback for older OpenAI versions
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1000,
                temperature=0.7,
            )
            return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error calling OpenAI API: {str(e)}")
        return None


def main():
    # Initialize OpenAI
    openai_client = initialize_openai()

    # App title and description
    st.title("🤖 Simple ChatGPT Chatbot")
    st.markdown(
        "Chào mừng bạn đến với trợ lý AI cá nhân của mình! Hãy hỏi tôi bất cứ điều gì."
    )

    # Instructions
    with st.expander("📖 Hướng dẫn sử dụng"):
        st.markdown(
            """
        **Cách thêm context vào chatbot:**
        1. **Chọn tone giọng**: Chọn tone giọng cho AI trong sidebar (bình thường, hài hước, nghiêm túc...)
        2. **Nhập text**: Viết thông tin tham khảo vào ô "Nhập context"
        3. **Upload file**: Tải lên file .txt hoặc .pdf chứa thông tin
        4. **Bắt đầu chat**: AI sẽ trả lời dựa trên context bạn cung cấp
        
        **Ví dụ context:**
        - Thông tin về công ty, sản phẩm
        - Tài liệu hướng dẫn, quy trình
        - Kiến thức chuyên môn cụ thể
        - Dữ liệu để phân tích
        """
        )

    # Initialize session state for conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful AI assistant."}
        ]

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "system_message" not in st.session_state:
        st.session_state.system_message = "You are a helpful AI assistant."

    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Cài đặt")

        # Context Section
        st.subheader("📚 Thêm Context")

        # Tone selection
        tone_options = {
            "Bình thường": "Bình thường",
            "Hài hước": "Hài hước",
            "Nghiêm túc": "Nghiêm túc",
            "Thân thiện": "Thân thiện",
            "Lạnh lùng": "Lạnh lùng",
            "Hàn lâm": "Hàn lâm",
        }

        selected_tone = st.selectbox(
            "Chọn tone giọng cho AI:",
            options=list(tone_options.keys()),
            format_func=lambda x: tone_options[x],
            key="tone_select",
        )

        # Text context input - get value from template or keep existing
        context_text = st.text_area(
            "Nhập context/thông tin tham khảo:",
            height=150,
            placeholder="Nhập thông tin mà bạn muốn AI sử dụng để trả lời câu hỏi...",
            value=(st.session_state.get("context_text", "")),
            key="context_input",
        )

        # Store context text in session state
        st.session_state.context_text = context_text

        # Show character count and clear button
        if context_text:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.caption(f"📊 Độ dài context: {len(context_text)} ký tự")
            with col2:
                if st.button("🗑️", key="clear_context", help="Xóa context"):
                    st.session_state.context_text = ""
                    st.rerun()

        # File upload
        uploaded_file = st.file_uploader(
            "Hoặc upload file:", type=["txt", "pdf"], help="Hỗ trợ file .txt và .pdf"
        )

        # Process uploaded file
        file_context = ""
        if uploaded_file is not None:
            if uploaded_file.type == "text/plain":
                file_context = str(uploaded_file.read(), "utf-8")
                st.success(f"✅ Đã tải file: {uploaded_file.name}")
            elif uploaded_file.type == "application/pdf":
                file_context = extract_text_from_pdf(uploaded_file)
                if file_context:
                    st.success(f"✅ Đã tải file PDF: {uploaded_file.name}")

        # Combine contexts
        full_context = ""
        if context_text:
            full_context += context_text
        if file_context:
            if full_context:
                full_context += "\n\n" + file_context
            else:
                full_context = file_context

        # Update system message when context changes
        if full_context or selected_tone:
            system_message = create_context_message(full_context, selected_tone)
            if (
                "system_message" not in st.session_state
                or st.session_state.system_message != system_message
            ):
                st.session_state.system_message = system_message
                # Reset conversation with new context
                st.session_state.messages = [
                    {"role": "system", "content": system_message}
                ]
                st.session_state.chat_history = []
                st.success("🔄 Đã cập nhật context!")

        # Clear conversation button
        if st.button("🗑️ Xóa cuộc trò chuyện"):
            system_message = create_context_message(full_context, selected_tone)
            st.session_state.messages = [{"role": "system", "content": system_message}]
            st.session_state.chat_history = []
            st.session_state.selected_template = None  # Reset template selection
            st.rerun()

        # st.markdown("---")
        # st.markdown("### Nội dung")
        # st.markdown(
        #     "Đây là một chatbot đơn giản được xây dựng bằng Streamlit và OpenAI ChatGPT API."
        # )

        # Display current context info
        if full_context:
            with st.expander("📄 Context hiện tại"):
                st.text_area(
                    "",
                    value=(
                        full_context[:500] + "..."
                        if len(full_context) > 500
                        else full_context
                    ),
                    height=100,
                    disabled=True,
                )

        if selected_tone:
            st.info(f"🎭 Tone giọng hiện tại: {tone_options[selected_tone]}")

        # st.markdown("### Chuẩn bị")
        # st.markdown("1. Tạo tệp `.env` trong thư mục gốc của dự án")
        # st.markdown(
        #     "2. Thêm khóa API OpenAI của bạn: `OPENAI_API_KEY=your_api_key_here`"
        # )
        # st.markdown("3. Chạy với: `streamlit run chatbot.py`")

        st.markdown("---")
        st.markdown("🎭 Made by [ToanTran](https://toantran.dev)")

    # Display chat history
    for i, (user_msg, bot_msg) in enumerate(st.session_state.chat_history):
        with st.container():
            # User message
            st.markdown(f"**You:** {user_msg}")
            # Bot message
            st.markdown(f"**🤖 Assistant:** {bot_msg}")
            # st.markdown("---")

    # Chat input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Add user message to conversation
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get response from ChatGPT
        with st.spinner("🤔 Thinking..."):
            response = get_chatgpt_response(st.session_state.messages, openai_client)

        if response:
            # Add assistant response to conversation
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Add to chat history for display
            st.session_state.chat_history.append((user_input, response))

            # Rerun to update the display
            st.rerun()



if __name__ == "__main__":
    main()
