# ChatBot ATBM HTTT

Hệ thống trả lời các câu hỏi về An toàn bảo mật và Hệ thống thông tin. Chatbot này sử dụng LightRAG và OpenAI để cung cấp câu trả lời chính xác về các chủ đề liên quan đến bảo mật thông tin.

## Giới thiệu

Dự án này là một chatbot thông minh sử dụng LightRAG (Retrieval Augmented Generation) kết hợp với OpenAI để trả lời các câu hỏi về An toàn bảo mật và Hệ thống thông tin. Chatbot có khả năng hiểu và phản hồi các câu hỏi chuyên ngành, giải thích các khái niệm, và hỗ trợ học tập trong lĩnh vực bảo mật thông tin.

## Các tính năng chính

- Trả lời các câu hỏi về an toàn bảo mật và hệ thống thông tin
- Hỗ trợ phản hồi streaming để tạo trải nghiệm tự nhiên
- Lưu trữ lịch sử chat để dễ dàng xem lại
- Sử dụng LightRAG để cải thiện độ chính xác của câu trả lời
- Giao diện thân thiện với người dùng nhờ Streamlit

## Cài đặt

### Yêu cầu

- Python 3.9+
- Tài khoản OpenAI và API key

### Các bước cài đặt

1. Clone repository:
```bash
git clone https://github.com/Sgm27/Chatbot-ATBM-HTTT.git
cd Chatbot-ATBM-HTTT
```

2. Cài đặt các dependencies:
```bash
pip install -r requirements.txt
```

3. Tạo file `.env` từ file `.env.example`:
```bash
cp .env.example .env
```

4. Cập nhật file `.env` với API key của OpenAI:
```
OPENAI_API_KEY=your_api_key_here
```

## Sử dụng

1. Khởi động ứng dụng:
```bash
streamlit run app.py
```

2. Mở trình duyệt web và truy cập địa chỉ được hiển thị (thường là http://localhost:8501)

3. Nhập câu hỏi của bạn và đợi chatbot phản hồi

## Cấu trúc dự án

```
Chatbot-ATBM-HTTT/
├── app.py               # Ứng dụng Streamlit chính
├── data/                # Thư mục chứa dữ liệu
├── .env.example         # Mẫu cấu hình môi trường
├── .gitignore           # Cấu hình Git ignore
├── README.md            # Tài liệu hướng dẫn
└── requirements.txt     # Danh sách dependencies
```

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng gửi Pull Request hoặc mở Issue để đề xuất thay đổi.

## Giấy phép

Dự án này được phân phối theo giấy phép MIT. 