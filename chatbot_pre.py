import streamlit as st
import openai
import os
from dotenv import load_dotenv
import PyPDF2
import io

# Tải biến môi trường
load_dotenv()

# Thiết lập cấu hình trang
st.set_page_config(page_title="Simple ChatGPT Chatbot", page_icon="🤖", layout="wide")


def extract_text_from_pdf(pdf_file):
    """Hàm trích xuất văn bản từ file PDF hoặc TXT đã tải lên.
    Đầu vào là file đã tải lên, đầu ra là chuỗi văn bản"""
    return


def create_context_message(context_text, role=""):
    """Tạo thông điệp hệ thống với context.
    Đầu vào là văn bản context và vai trò, đầu ra là chuỗi thông điệp hệ thống"""
    return


def initialize_openai():
    """Khởi tạo client OpenAI với khóa API.
    Đầu ra là client OpenAI đã khởi tạo"""
    return


def get_chatgpt_response(messages, client=None):
    """Lấy phản hồi từ API ChatGPT.
    Đầu vào là danh sách tin nhắn, đầu ra là phản hồi từ ChatGPT"""
    return


def main():
    # Khởi tạo client OpenAI
    openai_client = initialize_openai()

    # Tiêu đề và mô tả với st.title và st.markdown
    st.title("🤖 Simple ChatGPT Chatbot")
    st.markdown(
        "Chào mừng bạn đến với trợ lý AI cá nhân của mình! Hãy hỏi tôi bất cứ điều gì."
    )

    # Tạo box hướng dẫn với st.expander và st.markdown
    ##### CODE SNIPPET START #####

    # Khởi tạo trạng thái phiên cho lịch sử cuộc trò chuyện
    # Dùng st.session_state để lưu trữ trạng thái cuộc trò chuyện
    ##### CODE SNIPPET START #####

    # Khởi tạo sidebar với st.sidebar
    ##### CODE SNIPPET START #####
    with st.sidebar:
        st.header("⚙️ Cài đặt")

        # Mục Context
        st.subheader("📚 Thêm Context")

        # Chọn vai trò AI
        # Tạo dropdown menu với st.selectbox

        # Nhập context thù công bằng text area

        # Lưu context vào session state

        # Hiển thị độ dài context và nút xóa context

        # Tải lên file context nếu không muốn nhập tay
        # Hỗ trợ file .txt và .pdf

        # Xử lý file đã tải lên và thêm vào file_context

        # Kết hợp context từ text area và file

        # Cập nhật thông điệp cho hệ thống nếu context thay đổi

        # Tạo nút xóa cuộc trò chuyện và giữ nguyên thông điệp hệ thống

        st.markdown("---")
        st.markdown("### Nội dung")
        st.markdown(
            "Đây là một chatbot đơn giản được xây dựng bằng Streamlit và OpenAI ChatGPT API."
        )

        # Hiển thị context hiện tại nếu có

        # Hiện thị vai trò hiện tại nếu có

        st.markdown("### Chuẩn bị")
        st.markdown("1. Tạo tệp `.env` trong thư mục gốc của dự án")
        st.markdown(
            "2. Thêm khóa API OpenAI của bạn: `OPENAI_API_KEY=your_api_key_here`"
        )
        st.markdown("3. Chạy với: `streamlit run chatbot.py`")

    # Hiển thị lịch sử trò chuyện trong st.session_state.chat_history với st.markdown

    # Đầu vào câu hỏi từ người dùng với st.chat_input


if __name__ == "__main__":
    main()
