# ChatBot ATBM HTTT

Hệ thống trả lời các câu hỏi về An toàn bảo mật và Hệ thống thông tin. Chatbot này sử dụng LightRAG và OpenAI để cung cấp câu trả lời chính xác về các chủ đề liên quan đến bảo mật thông tin.

## Cài đặt

1. Clone repository:
```
git clone https://github.com/Sgm27/Chatbot-ATBM-HTTT.git
cd Chatbot-ATBM-HTTT
```

2. Cài đặt các dependencies:
```
pip install -r requirements.txt
```

3. Tạo file `.env` với API key của OpenAI:
```
OPENAI_API_KEY=your_api_key_here
```

## Chạy ứng dụng

```
streamlit run app.py
```

## Tính năng

- Trả lời các câu hỏi về an toàn bảo mật và hệ thống thông tin
- Hỗ trợ phản hồi streaming
- Lưu trữ lịch sử chat 