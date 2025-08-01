import streamlit as st
import openai
import os
from dotenv import load_dotenv
import PyPDF2
import io

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(page_title="Simple ChatGPT Chatbot", page_icon="🤖", layout="wide")


def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""


def create_context_message(context_text, role=""):
    """Create system message with context"""


def initialize_openai():
    """Initialize OpenAI client with API key"""


def get_chatgpt_response(messages, client=None):
    """Get response from ChatGPT API"""


def main():
    # Initialize OpenAI
    openai_client = initialize_openai()

    # App title and description
    st.title("🤖 Simple ChatGPT Chatbot")
    st.markdown(
        "Chào mừng bạn đến với trợ lý AI cá nhân của mình! Hãy hỏi tôi bất cứ điều gì."
    )

    # Instructions

    # Initialize session state for conversation history

    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Cài đặt")

        # Context Section
        st.subheader("📚 Thêm Context")

        # Role selection
        role_options = {
            "": "Trợ lý AI thông thường",
            "teacher": "Giáo viên",
            "doctor": "Bác sĩ",
            "lawyer": "Luật sư",
            "programmer": "Lập trình viên",
            "translator": "Người dịch",
            "customer service representative": "Nhân viên chăm sóc khách hàng",
        }

        selected_role = st.selectbox(
            "Chọn vai trò cho AI:",
            options=list(role_options.keys()),
            format_func=lambda x: role_options[x],
            key="role_select",
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
        if full_context or selected_role:
            system_message = create_context_message(full_context, selected_role)
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
            system_message = create_context_message(full_context, selected_role)
            st.session_state.messages = [{"role": "system", "content": system_message}]
            st.session_state.chat_history = []
            st.session_state.selected_template = None  # Reset template selection
            st.rerun()

        st.markdown("---")
        st.markdown("### Nội dung")
        st.markdown(
            "Đây là một chatbot đơn giản được xây dựng bằng Streamlit và OpenAI ChatGPT API."
        )

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

        if selected_role:
            st.info(f"🎭 Vai trò hiện tại: {role_options[selected_role]}")

        st.markdown("### Chuẩn bị")
        st.markdown("1. Tạo tệp `.env` trong thư mục gốc của dự án")
        st.markdown(
            "2. Thêm khóa API OpenAI của bạn: `OPENAI_API_KEY=your_api_key_here`"
        )
        st.markdown("3. Chạy với: `streamlit run chatbot.py`")

    # Display chat history

    # Chat input


if __name__ == "__main__":
    main()
