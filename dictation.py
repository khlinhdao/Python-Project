import streamlit as st
import pandas as pd
import os
import string

class Dictation:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def play_audio_file(self, index):
        audio_file = self.data.iloc[index]['audio_file']
        if os.path.exists(audio_file):
            audio_bytes = open(audio_file, 'rb').read()
            st.audio(audio_bytes, format='audio/mp3', start_time=0, autoplay=True)
        else:
            st.write(f"Audio file '{audio_file}' not found.")

    def normalize(self, text):
        return text.lower().translate(str.maketrans('', '', string.punctuation.replace("'", "")))

    def check_answer(self, user_answer, index):
        user_words = self.normalize(user_answer).strip().split()
        correct_answer = self.data.iloc[index]['sentence']
        correct_words = self.normalize(correct_answer).strip().split()
        return user_words == correct_words, correct_answer

    def run(self):
        if "index" not in st.session_state:
            st.session_state.index = 0
    
        if "user_answer" not in st.session_state:
            st.session_state.user_answer = ""

        st.markdown(
            "<h2 style='text-align: center; font-size: 60px; font-weight: bold; margin-top: 100px;'>Dictation</h2>",
            unsafe_allow_html=True
        )
        
        # Hàng 1: Nút Skip và thanh âm thanh
        col1, col2 = st.columns([8, 1])  # Tạo hai cột
        with col2:  
            if st.button("Skip", key="skip_button"):
                st.session_state.index = (st.session_state.index + 1) % len(self.data)
                st.session_state.user_answer = ""  # Xóa nội dung ô nhập liệu khi nhấn Skip
        with col1:
            self.play_audio_file(st.session_state.index)  # Phát âm thanh

        # Hàng 2: Input
        user_answer = st.text_input("Enter your answer:", value=st.session_state.user_answer)

        # Cập nhật giá trị của session state khi người dùng nhập
        st.session_state.user_answer = user_answer  # Cập nhật giá trị

        # Hàng 3: Check và Show
        col3, col4 = st.columns([1, 1], gap="small")  # Căn hai cột đều nhau
        with col3:
            if st.button("Check Answer", key="check_button"):
                if st.session_state.user_answer:
                    result, correct_answer = self.check_answer(st.session_state.user_answer, st.session_state.index)
                    if result:
                        st.success("Correct answer!")
                    else:
                        st.error(f"Wrong answer!")
                else:
                    st.warning("Please enter your answer before checking.")

        with col4:
            if st.button("Show Answer", key="show_button"):
                correct_answer = self.data.iloc[st.session_state.index]['sentence']
                st.info(f"The correct answer is: '{correct_answer}'")

        # Nút quay lại
        if st.button("Go Back to Level Selection"):
            st.session_state.show_dictation = False  # Quay lại trang chọn mức độ


if __name__ == "__main__":
    if "show_dictation" not in st.session_state:
        st.session_state.show_dictation = False

    if not st.session_state.show_dictation:
        # Tạo ba cột để căn giữa
        col1, col2, col3 = st.columns([5, 10, 5])  # Tạo ba cột, cột giữa lớn hơn

        with col1:
            st.write("")  # Khoảng cách ở trên

        with col2:  # Sử dụng cột giữa
            st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)
            st.markdown(
                """
                <style>
                .big-radio {
                    font-size: 400px;  /* Tăng kích thước chữ của radio button */
                }
                .big-button {
                    font-size: 40px;  /* Tăng kích thước chữ của nút */
                    padding: 20px 40px; /* Tăng padding của nút */
                    background-color: #4CAF50; /* Màu nền của nút */
                    color: white; /* Màu chữ của nút */
                    border: none; /* Bỏ đường viền */
                    border-radius: 10px; /* Bo tròn góc nút */
                    cursor: pointer; /* Con trỏ chuột khi di chuột qua nút */
                }
                .header {
                    font-size: 30px;  /* Kích thước chữ cho tiêu đề */
                    font-weight: bold; /* Độ đậm của chữ */
                    text-align: center; /* Căn giữa tiêu đề */
                    margin: 0 auto 30px; /* Căn giữa với margin tự động, khoảng cách dưới 30px */
                    width: 300px; /* Chiều rộng tự động theo nội dung */
                    display: block; /* Giúp chiều rộng có hiệu lực */
                }

                </style>
                """, unsafe_allow_html=True
            )

            # Hiển thị tiêu đề
            st.markdown('<p class="header">Select difficulty level:</p>', unsafe_allow_html=True)

            # Tạo radio button
            level = st.radio("", ("Easy", "Hard"), key="level_radio", index=0, label_visibility="collapsed")
            start_button = st.button("Start Dictation", key="start_button")
            if start_button:
                st.session_state.level = level
                if level == "Easy":
                    st.session_state.csv_file = r'Audio/easy.csv'
                else:
                    st.session_state.csv_file = r'Audio/hard.csv'
                st.session_state.show_dictation = True
                st.query_params = {"started": True}
        
        with col3:
            st.write("")  # Khoảng cách ở dưới
    else:
        dictation = Dictation(st.session_state.csv_file)
        dictation.run()
