from nicegui import ui
import pandas as pd
import string

class Dictation:
    def __init__(self):
        self.index = 0
        self.user_answer = ""
        self.audio_player = None
        self.data = pd.DataFrame()  # Khởi tạo DataFrame rỗng
        self.selected_difficulty = None
        self.selected_topic = None
        self.notification_label = ui.label('').style('margin-top: 20px; font-size: 20px; color: black;')  # Khởi tạo label thông báo

        # Tạo các column cho từng trang
        self.difficulty_column = ui.column().style('align-items: center;')
        self.topic_column = ui.column().style('align-items: center;')
        self.dictation_column = ui.column().style('align-items: center;')

        self.render_difficulty_page()  # Khởi động ứng dụng tại trang chọn độ khó

    def update_audio_file(self):
        audio_file = self.data.iloc[self.index]['audio_file']
        
        if self.audio_player:
            self.audio_player.delete()  # Xóa đối tượng âm thanh cũ

        # Tạo đối tượng âm thanh mới và hiển thị thanh điều khiển
        self.audio_player = ui.audio(audio_file).props('controls').style('width: 300px;')  
        self.audio_player.play()  # Phát âm thanh

    def normalize(self, text):
        return str(text).lower().translate(str.maketrans('', '', string.punctuation.replace("'", "")))

    def check_answer(self):
        user_words = self.normalize(self.user_answer).strip().split()
        correct_answer = self.data.iloc[self.index]['sentence']
        correct_words = self.normalize(correct_answer).strip().split()
        return user_words == correct_words

    def play_sound(self, audio_file):
        self.play = ui.audio(audio_file).style('display: none;')  
        self.play.play()

    def check_answer_click(self):
        if self.user_answer:
            result = self.check_answer()
            if result:
                self.notification_label.text = 'Câu trả lời đúng!'
                self.notification_label.style('color: green;')
                self.play_sound("https://raw.githubusercontent.com/Phamlong2675/Python-Project/refs/heads/main/Audio/effect%20sound/sound_correct.wav")
            else:
                self.notification_label.text = 'Câu trả lời sai!'
                self.notification_label.style('color: red;')
                self.play_sound("https://raw.githubusercontent.com/Phamlong2675/Python-Project/refs/heads/main/Audio/effect%20sound/sound_wrong.mp3")
        else:
            self.notification_label.text = 'Vui lòng nhập câu trả lời trước khi kiểm tra.'
            self.notification_label.style('color: orange;')

    def show_answer(self):
        correct_answer = self.data.iloc[self.index]['sentence']
        self.notification_label.text = f"Câu trả lời đúng là: '{correct_answer}'"
        self.notification_label.style('color: blue;')

    def skip(self):
        if len(self.data) > 0:  # Kiểm tra xem có dữ liệu trong DataFrame không
            self.index = (self.index + 1) % len(self.data)  # Tăng chỉ số và quay lại đầu nếu vượt quá
            self.user_answer = ""
            self.input.value = ""  # Xóa ô nhập câu trả lời
            self.notification_label.text = ""  # Xóa nội dung thông báo
            self.update_audio_file()  # Cập nhật âm thanh cho câu tiếp theo
            self.no_sens.delete()
            self.no_sens = ui.label(f'({self.index+1}/10)').style('font-size: 18px;')

    def turnback(self):
        if len(self.data) > 0:  # Kiểm tra xem có dữ liệu trong DataFrame không
            if self.index > 0:
                self.index -= 1
            else:
                self.index = 9
            self.user_answer = ""
            self.input.value = ""  # Xóa ô nhập câu trả lời
            self.notification_label.text = ""  # Xóa nội dung thông báo
            self.update_audio_file()  # Cập nhật âm thanh cho câu tiếp theo
            self.no_sens.delete()
            self.no_sens = ui.label(f'({self.index+1}/10)').style('font-size: 18px;')

    def load_data(self, url):
        self.data = pd.read_csv(url)
        self.index = 0  # Đặt lại chỉ số khi tải dữ liệu mới
        self.update_audio_file()  # Cập nhật tệp âm thanh cho mục đầu tiên

    def render_difficulty_page(self):
        self.difficulty_column.clear()  # Xóa nội dung cũ
        with self.difficulty_column:
            ui.label('Chọn Độ Khó:').style('margin-bottom: 20px; font-size: 24px;')
            with ui.row().style('justify-content: center; margin: 10px 0;'):
                ui.button('Easy', on_click=lambda: self.go_to_topic_selection('Easy')).style('margin: 10px; padding: 15px; font-size: 18px;')  # Căn giữa
                ui.button('Hard', on_click=lambda: self.go_to_topic_selection('Hard')).style('margin: 10px; padding: 15px; font-size: 18px;')  # Căn giữa

        self.topic_column.clear()  # Xóa nội dung cũ
        self.dictation_column.clear()  # Xóa nội dung cũ
        self.difficulty_column.visible = True
        self.topic_column.visible = False
        self.dictation_column.visible = False

    def go_to_topic_selection(self, difficulty):
        self.selected_difficulty = difficulty
        ui.notify(f'Bạn đã chọn độ khó: {self.selected_difficulty}')
        self.render_topic_page()  # Hiển thị trang chọn chủ đề

    def render_topic_page(self):
        self.topic_column.clear()  # Xóa nội dung cũ
        with self.topic_column:
            ui.label(f'Độ khó đã chọn: {self.selected_difficulty}').style('margin-bottom: 20px; font-size: 24px;')
            ui.label(f'Chọn chủ đề:').style('margin-bottom: 10px; font-size: 24px;')
            
            # Tạo hàng cho các nút chủ đề
            with ui.row().style('justify-content: center; margin: 10px 0;'):
                if self.selected_difficulty == 'Easy':
                    ui.button('Topic 1', on_click=lambda: self.set_topic('Topic 1 - Easy')).style('margin: 10px; padding: 15px; font-size: 18px;') 
                    ui.button('Topic 2', on_click=lambda: self.set_topic('Topic 2 - Easy')).style('margin: 10px; padding: 15px; font-size: 18px;')  
                    ui.button('Topic 3', on_click=lambda: self.set_topic('Topic 3 - Easy')).style('margin: 10px; padding: 15px; font-size: 18px;')
                    ui.button('Topic 4', on_click=lambda: self.set_topic('Topic 4 - Easy')).style('margin: 10px; padding: 15px; font-size: 18px;')  
                    ui.button('Topic 5', on_click=lambda: self.set_topic('Topic 5 - Easy')).style('margin: 10px; padding: 15px; font-size: 18px;')
                elif self.selected_difficulty == 'Hard':
                    ui.button('Topic 1', on_click=lambda: self.set_topic('Topic 1 - Hard')).style('margin: 10px; padding: 15px; font-size: 18px;')  
                    ui.button('Topic 2', on_click=lambda: self.set_topic('Topic 2 - Hard')).style('margin: 10px; padding: 15px; font-size: 18px;')
                    ui.button('Topic 3', on_click=lambda: self.set_topic('Topic 3 - Hard')).style('margin: 10px; padding: 15px; font-size: 18px;')
                    ui.button('Topic 4', on_click=lambda: self.set_topic('Topic 4 - Hard')).style('margin: 10px; padding: 15px; font-size: 18px;')
                    ui.button('Topic 5', on_click=lambda: self.set_topic('Topic 5 - Hard')).style('margin: 10px; padding: 15px; font-size: 18px;')        
            
            # Nút Quay lại căn trái
            ui.button('Quay lại', on_click=self.render_difficulty_page).style('margin: 10px 0; padding: 15px; font-size: 18px; align-self: flex-start;')

        self.difficulty_column.visible = False
        self.dictation_column.visible = False
        self.topic_column.visible = True

    def set_topic(self, topic):
        self.selected_topic = topic
        ui.notify(f'Bạn đã chọn chủ đề: {self.selected_topic}')
        self.start_dictation()

    def start_dictation(self):
        if self.selected_difficulty == 'Easy':
            if self.selected_topic == 'Topic 1 - Easy':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic1easy.csv')
            elif self.selected_topic == 'Topic 2 - Easy':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic2easy.csv')
            elif self.selected_topic == 'Topic 3 - Easy':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic3easy.csv')
            elif self.selected_topic == 'Topic 4 - Easy':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic4easy.csv')
            elif self.selected_topic == 'Topic 5 - Easy':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic5easy.csv')
        elif self.selected_difficulty == 'Hard':
            if self.selected_topic == 'Topic 1 - Hard':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic1hard.csv')
            elif self.selected_topic == 'Topic 2 - Hard':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic2hard.csv')
            elif self.selected_topic == 'Topic 3 - Hard':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic3hard.csv')
            elif self.selected_topic == 'Topic 4 - Hard':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic4hard.csv')
            elif self.selected_topic == 'Topic 5 - Hard':
                self.load_data('https://raw.githubusercontent.com/Phamlong2675/Python-Project/main/Audio/topic5hard.csv')

        self.render_dictation_page()  # Hiển thị trang dictation

    def render_dictation_page(self):
        self.dictation_column.clear()  # Xóa nội dung cũ
        with self.dictation_column:
            ui.label(f'Bắt Đầu Dictation cho: {self.selected_topic}').style('margin-bottom: 20px; font-size: 24px;')
   
            with ui.row().style('justify-content: center; margin: 10px 0; align-items: center;'):
                ui.button(on_click=lambda: [self.turnback(), setattr(self.input, 'value', '')], icon='fast_rewind').style('width: 50px; height: 50px; padding: 0;')
                ui.button(on_click=lambda: [self.skip(), setattr(self.input, 'value', '')], icon='fast_forward').style('width: 50px; height: 50px; padding: 0;')
                self.update_audio_file()  # Cập nhật âm thanh
                self.no_sens = ui.label(f'({self.index+1}/10)').style('font-size: 18px;')

            self.input = ui.input('Nhập câu trả lời của bạn:', on_change=lambda: setattr(self, 'user_answer', self.input.value)).style('margin-bottom: 10px; font-size: 24px; width: 400px; padding: 10px;')
            # Hiển thị label thông báo ở đây
            self.notification_label = ui.label('').style('margin-top: 20px; font-size: 20px; color: black;')  # Khởi tạo label thông báo

            # Tạo hàng cho các nút
            with ui.row().style('justify-content: center; margin: 10px 0;'):
                ui.button('Kiểm tra đáp án', on_click=self.check_answer_click).style('margin: 10px; padding: 15px; font-size: 18px;')
                ui.button('Hiển thị đáp án', on_click=self.show_answer).style('margin: 10px; padding: 15px; font-size: 18px;')

            with ui.row().style('justify-content: center; margin: 10px 0;'):
                ui.button('Chọn độ khó', on_click=self.render_difficulty_page).style('margin: 10px; padding: 15px; font-size: 18px;')
                ui.button('Chọn chủ đề', on_click=self.render_topic_page).style('margin: 10px; padding: 15px; font-size: 18px;')


        self.difficulty_column.visible = False
        self.topic_column.visible = False
        self.dictation_column.visible = True
        
Dictation()
ui.run()
