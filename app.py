from gtts import gTTS
from playsound import playsound
from nicegui import ui
import os
import string


class Dictation:
    def __init__(self):
        # Danh sách câu
        self.sentences = [
            "Hello, how are you?",
            "Goodbye! See you later.",
            "Thank you for your help.",
            "I am sorry for the inconvenience.",
            "Could you please help me?",
            "How about we go out for dinner?",
            "I completely agree with you.",
            "I see your point, but I disagree.",
            "Would you like to join us for lunch?",
            "You did a great job!",
            "It is a beautiful day outside.",
            "I love reading books in my free time.",
            "What do you think about this idea?",
            "Always follow your heart."
        ]
        self.current_index = 0
        self.result_label = None

    def normalize(self, word):
        """Chuyển đổi từ thành chữ thường và loại bỏ dấu câu."""
        return word.lower().translate(str.maketrans('', '', string.punctuation))

    def compare_answers(self, user_answer, correct_sentence):
        """So sánh từng từ trong câu trả lời của người dùng với câu chuẩn."""
        user_words = user_answer.split()
        correct_words = correct_sentence.split()

        # Chuẩn hóa từ
        user_words = [self.normalize(word) for word in user_words]
        correct_words = [self.normalize(word) for word in correct_words]

        # Kiểm tra xem câu trả lời có đúng không
        if user_words == correct_words:
            return "Correct answer!", None
        else:
            return "Wrong answer!", correct_sentence

    def generate_audio(self, sentence):
        """Tạo và phát file âm thanh cho câu hiện tại."""
        tts = gTTS(sentence)
        audio_path = "dictation.mp3"
        tts.save(audio_path)

        try:
            playsound(audio_path)  # Phát âm thanh
        except Exception as e:
            print(f"Audio playback error: {e}")
        finally:
            os.remove(audio_path)  # Xóa file sau khi phát

    def play_feedback_sound(self, feedback_type):
        """Phát âm thanh dựa trên kết quả đúng hoặc sai."""
        feedback_messages = {
            1: "Correct answer!",
            2: "Wrong answer!",
            3: "You have not entered your answer yet.",
            4: "The correct answer is:"
        }
        
        tts = gTTS(feedback_messages.get(feedback_type, ""))
        audio_path = f"{feedback_messages[feedback_type].replace(' ', '_').lower()}.mp3"
        tts.save(audio_path)

        try:
            playsound(audio_path)
        except Exception as e:
            print(f"Audio playback error: {e}")
        finally:
            os.remove(audio_path)

    def play_sound(self):
        """Phát âm thanh cho câu hiện tại."""
        self.result_label.set_text("")  # Xóa nội dung kết quả trước đó
        current_sentence = self.sentences[self.current_index]
        ui.timer(0.1, lambda: self.generate_audio(current_sentence), once=True)  # Phát âm thanh

    def submit_answer(self, answer_input):
        """Xử lý khi người dùng nhấn nút Kiểm tra."""
        user_answer = answer_input.value.strip()

        if not user_answer:
            self.result_label.set_text("You have not entered your answer yet!")
            self.result_label.style('color: orange; font-size: 28px;')
            ui.timer(0.1, lambda: self.play_feedback_sound(3), once=True)
            return

        result, correct_sentence_returned = self.compare_answers(user_answer, self.sentences[self.current_index])
        if correct_sentence_returned:
            self.result_label.set_text(result)
            self.result_label.style('color: red; font-size: 28px;')
            ui.timer(0.1, lambda: self.play_feedback_sound(2), once=True)
        else:
            self.result_label.set_text(result)
            self.result_label.style('color: green; font-size: 28px;')
            ui.timer(0.1, lambda: self.play_feedback_sound(1), once=True)

    def see_answer(self):
        """Hiển thị câu trả lời đúng."""
        correct_sentence = self.sentences[self.current_index]
        self.result_label.set_text(f"The correct answer is: '{correct_sentence}'")
        self.result_label.style('color: blue; font-size: 28px;')
        ui.timer(0.1, lambda: self.play_feedback_sound(4), once=True)

    def change_sentence(self, answer_input):
        """Chuyển câu và phát âm thanh câu mới."""
        answer_input.set_value("")  # Xóa nội dung ô nhập câu trả lời
        self.result_label.set_text("")  # Xóa nội dung kết quả trước đó
        self.current_index += 1
        if self.current_index >= len(self.sentences):
            self.current_index = 0  # Reset về đầu danh sách khi hết câu

        ui.timer(0.1, self.play_sound, once=True)  # Phát âm thanh của câu mới

    def run(self):
        """Khởi chạy giao diện người dùng."""
        # Giao diện người dùng
        with ui.column().style('align-items: center; justify-content: center; height: 100vh; width: 100vw;'):
            ui.label("Dictation").style('font-size: 80px; color: #6D8EBF; margin-bottom: 20px;')

            answer_input = ui.input(placeholder="Enter your answer:").style('width: 500px; height: 50px; font-size: 18px; margin-bottom: 20px;')

            self.result_label = ui.label("").style('color: #2196F3; font-size: 28px; margin-bottom: 20px;')

            # Bố cục ngang để xếp các nút cạnh nhau
            with ui.row().style('justify-content: center; margin-bottom: 20px;'):
                # Nút phát âm thanh
                ui.button("Play Sound", on_click=self.play_sound, icon='volume_up').style('background-color: #4CAF50; color: white; font-size: 18px; margin: 10px;')
                # Nút kiểm tra câu trả lời
                ui.button("Check", on_click=lambda: self.submit_answer(answer_input), icon='check').style('background-color: #20B2AA; color: white; font-size: 18px; margin: 10px;')
                # Nút xem câu trả lời đúng
                ui.button("See Answer", on_click=self.see_answer, icon='visibility').style('background-color: #0000FF; color: white; font-size: 18px; margin: 10px;')
                # Nút chuyển câu
                ui.button("Skip", on_click=lambda: self.change_sentence(answer_input), icon='fast_forward').style('background-color: #FF9800; color: white; font-size: 18px; margin: 10px;')

        ui.run(host="0.0.0.0", port=8080)


# Khởi chạy ứng dụng
if __name__ in {"__main__", "__mp_main__"}:
    dictation = Dictation() 
    dictation.run()
