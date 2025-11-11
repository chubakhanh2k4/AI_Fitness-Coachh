import streamlit as st
from openai import OpenAI
import matplotlib.pyplot as plt
import json

# --- Cấu hình Streamlit ---
st.set_page_config(page_title="AI Fitness Coach", layout="wide")

# --- Sidebar nhập thông tin người dùng ---
st.sidebar.header("Thông tin người dùng")
gender = st.sidebar.selectbox("Giới tính", ["Nam", "Nữ"])
age = st.sidebar.number_input("Tuổi", min_value=10, max_value=80, value=25)
weight = st.sidebar.number_input("Cân nặng (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input("Chiều cao (cm)", min_value=120.0, max_value=220.0, value=170.0)
goal = st.sidebar.selectbox("Mục tiêu tập luyện", ["Tăng cơ", "Giảm mỡ", "Giữ dáng"])
sessions = st.sidebar.slider("Số buổi tập mỗi tuần", 1, 7, 4)

# --- Main page ---
st.title("🏋️‍♂️ AI Fitness Coach - Trợ lý thể hình thông minh")
st.write("Nhập thông tin bên sidebar để nhận lịch tập cá nhân hóa!")

# --- Thêm ảnh minh họa ---
st.image("https://wallpaperaccess.com/full/4692606.jpg",
         caption="Ví dụ bài tập: Squat", use_container_width=True)

# --- Kết nối OpenAI ---
client = OpenAI(api_key="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")

# --- Nút gợi ý lịch tập và thực đơn ---
if st.button("Gợi ý lịch tập & dinh dưỡng"):
    prompt = f"""
Bạn là huấn luyện viên AI và chuyên gia dinh dưỡng.
Người dùng {gender}, {age} tuổi, cao {height}cm, nặng {weight}kg,
mục tiêu {goal}, tập {sessions} buổi/tuần.
1. Hãy gợi ý lịch tập 7 ngày chi tiết: bài tập, nhóm cơ, hiệp và lần lặp.
2. Gợi ý thực đơn cơ bản cho 7 ngày phù hợp với mục tiêu.
Chia rõ ngày và thông tin.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content
    st.markdown(result)

    # --- Lưu thông tin người dùng và kết quả ---
    data = {
        "gender": gender,
        "age": age,
        "weight": weight,
        "height": height,
        "goal": goal,
        "sessions": sessions,
        "result": result
    }
    with open("userdata.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    st.success("Thông tin và lịch tập đã được lưu!")

# --- Dashboard tiến độ giả lập ---
st.subheader("📊 Dashboard tiến độ (ví dụ tuần này)")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
completion = [1, 1, 0, 1, 0, 1, 0]  # 1 = hoàn thành, 0 = chưa

fig, ax = plt.subplots()
ax.bar(days, completion, color="skyblue")
ax.set_ylabel("Hoàn thành (1=done)")
ax.set_title("Tiến độ tập luyện tuần này")
st.pyplot(fig)

# --- Thông tin thêm ---
st.info("💡 Bạn có thể thay đổi thông tin bên sidebar và nhấn lại 'Gợi ý lịch tập & dinh dưỡng' để nhận lịch mới.")
