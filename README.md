
# 🏋️‍♂️ AI Fitness Coach
<div align="center">
  <p align="center">
    <img src="https://raw.githubusercontent.com/anhminhvdvn/CanhBaoDotNhap/main/images/logoDaiNam.png" width="150"> </p> <br>




</br> </div>

**AI Fitness Coach** là một ứng dụng web được xây dựng bằng **Streamlit** và **OpenAI API**, giúp người dùng nhận gợi ý **lịch tập thể hình cá nhân hóa** dựa trên thông tin thể trạng và mục tiêu luyện tập.

---

## 🚀 Tính năng nổi bật

- 💬 Gợi ý **lịch tập 7 ngày** tự động dựa trên:
  - Giới tính, tuổi, chiều cao, cân nặng  
  - Mục tiêu tập luyện (Tăng cơ / Giảm mỡ / Giữ dáng)  
  - Số buổi tập mỗi tuần
- 🤖 Sử dụng **AI GPT-4o-mini** để tạo kế hoạch tập chi tiết.
- 📊 Giao diện đẹp, dễ sử dụng, chạy trực tiếp bằng **Streamlit**.
- 💾 Lưu lại thông tin người dùng (qua `userdata.json`) để cá nhân hóa kết quả.

---

## 🧰 Công nghệ sử dụng

| Thành phần | Mô tả |
|-------------|-------|
| **Python 3.11+** | Ngôn ngữ chính |
| **Streamlit** | Framework tạo web app |
| **OpenAI API** | Nền tảng AI sinh gợi ý |
| **Matplotlib** | Dự định dùng để vẽ biểu đồ (có thể mở rộng trong tương lai) |

---

## ⚙️ Cách chạy ứng dụng

### 1️⃣ Cài đặt thư viện cần thiết
Mở Terminal (CMD) trong thư mục dự án và chạy:
```bash
pip install streamlit openai matplotlib
2️⃣ Chạy ứng dụng
bash
Sao chép mã
python -m streamlit run app.py
Ứng dụng sẽ tự mở trong trình duyệt tại địa chỉ:

arduino
Sao chép mã
http://localhost:8501
🧠 Hướng phát triển trong tương lai
📅 Thêm chức năng lưu lịch tập và theo dõi tiến trình.

🍱 Gợi ý thực đơn dinh dưỡng phù hợp với mục tiêu.

🧍‍♂️ Gợi ý bài tập minh họa bằng hình ảnh hoặc video.

📈 Hiển thị biểu đồ tiến triển cân nặng / khối lượng cơ thể.

👨‍💻 Tác giả
Chu Bá Khánh
Sinh viên môn Chuyển đổi số
Trường Đại học Đại Nam

🏷️ Giấy phép
Dự án này chỉ dùng cho mục đích học tập và nghiên cứu.

