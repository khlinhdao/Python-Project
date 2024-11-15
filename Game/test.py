import random
from nicegui import ui



class WordScrambleBackend:
    def __init__(self):
        self.topic_flashcards = {
             "Nghề nghiệp": [
        {"word": "chef (n)", "info": "đầu bếp"},
        {"word": "comedian (n)", "info": "diễn viên hài"},
        {"word": "delivery man (n)", "info": "nhân viên giao hàng"},
        {"word": "doctor (n)", "info": "bác sĩ"},
        {"word": "entrepreneur (n)", "info": "nhà kinh doanh"},
        {"word": "engineer (n)", "info": "kỹ sư"},
        {"word": "factory worker (n)", "info": "công nhân nhà máy"},
        {"word": "office worker (n)", "info": "nhân viên văn phòng"},
        {"word": "florist (n)", "info": "người bán hoa"},
        {"word": "hairdresser (n)", "info": "thợ cắt tóc"},
    ],
    "Trái cây": [
        {"word": "pear (n)", "info": "quả lê"},
        {"word": "grape (n)", "info": "quả nho"},
        {"word": "peach (n)", "info": "quả đào"},
        {"word": "orange (n)", "info": "quả cam"},
        {"word": "mango (n)", "info": "quả xoài"},
        {"word": "coconut (n)", "info": "quả dừa"},
        {"word": "pineapple (n)", "info": "quả dứa"},
        {"word": "watermelon (n)", "info": "dưa hấu"},
        {"word": "durian (n)", "info": "sầu riêng"},
        {"word": "lychee (n)", "info": "quả vải"},
        {"word": "guava (n)", "info": "quả ổi"},
        {"word": "starfruit (n)", "info": "quả khế"},
    ],
    "Gia đình": [
        {"word": "parent (n)", "info": "bố hoặc mẹ"},
        {"word": "daughter (n)", "info": "con gái"},
        {"word": "son (n)", "info": "con trai"},
        {"word": "sibling (n)", "info": "anh chị em ruột"},
        {"word": "sister (n)", "info": "chị, em gái"},
        {"word": "brother (n)", "info": "anh, em trai"},
        {"word": "grandmother (n)", "info": "bà nội (ngoại)"},
        {"word": "grandfather (n)", "info": "ông nội (ngoại)"},
        {"word": "grandparent (n)", "info": "ông hoặc bà"},
        {"word": "relative (n)", "info": "họ hàng"},
        {"word": "aunt (n)", "info": "cô, dì"},
        {"word": "uncle (n)", "info": "chú, bác, cậu, dượng"},
    ],
    "Động Vật": [
        {"word": "mouse (n)", "info": "con chuột"},
        {"word": "cat (n)", "info": "con mèo"},
        {"word": "dog (n)", "info": "con chó"},
        {"word": "kitten (n)", "info": "mèo con"},
        {"word": "puppy (n)", "info": "chó con"},
        {"word": "pig (n)", "info": "con lợn, heo"},
        {"word": "chicken (n)", "info": "con gà"},
        {"word": "duck (n)", "info": "con vịt"},
        {"word": "goose (n)", "info": "con ngỗng"},
        {"word": "turkey (n)", "info": "con gà tây"},
        {"word": "stork (n)", "info": "con cò"},
        {"word": "swan (n)", "info": "thiên nga"},
    ],
    "Rau Quả": [
        {"word": "bean (n)", "info": "hạt đậu"},
        {"word": "pea (n)", "info": "đậu Hà Lan"},
        {"word": "cabbage (n)", "info": "bắp cải"},
        {"word": "carrot (n)", "info": "củ cà rốt"},
        {"word": "corn (n)", "info": "ngô, bắp"},
        {"word": "cucumber (n)", "info": "dưa chuột"},
        {"word": "tomato (n)", "info": "quả cà chua"},
        {"word": "garlic (n)", "info": "tỏi"},
        {"word": "onion (n)", "info": "củ hành"},
        {"word": "spring onion (n)", "info": "hành lá"},
        {"word": "ginger (n)", "info": "củ gừng"},
        {"word": "turmeric (n)", "info": "củ nghệ"},
        {"word": "potato (n)", "info": "khoai tây"},
        {"word": "sweet potato (n)", "info": "khoai lang"},
    ],
    "Đồ Ăn": [
        {"word": "soup (n)", "info": "món súp, món canh"},
        {"word": "salad (n)", "info": "rau trộn, nộm rau"},
        {"word": "bread (n)", "info": "bánh mì"},
        {"word": "sausage (n)", "info": "xúc xích"},
        {"word": "hot dog (n)", "info": "bánh mỳ kẹp xúc xích"},
        {"word": "bacon (n)", "info": "thịt xông khói"},
        {"word": "ham (n)", "info": "thịt giăm bông"},
        {"word": "egg (n)", "info": "trứng"},
        {"word": "pork (n)", "info": "thịt lợn"},
        {"word": "beef (n)", "info": "thịt bò"},
        {"word": "chicken (n)", "info": "thịt gà"},
        {"word": "duck (n)", "info": "thịt vịt"},
        {"word": "lamb (n)", "info": "thịt cừu"},
        {"word": "ribs (n)", "info": "sườn"},
    ],
    "Động tác cơ thể": [
        {"word": "tiptoe (v)", "info": "đi nhón chân"},
        {"word": "jump (v)", "info": "nhảy"},
        {"word": "leap (v)", "info": "nhảy vọt, nhảy xa"},
        {"word": "stand (v)", "info": "đứng"},
        {"word": "sit (v)", "info": "ngồi"},
        {"word": "lean (v)", "info": "dựa, tựa"},
        {"word": "wave (v)", "info": "vẫy tay"},
        {"word": "clap (v)", "info": "vỗ tay"},
        {"word": "point (v)", "info": "chỉ, trỏ"},
        {"word": "catch (v)", "info": "bắt, đỡ"},
        {"word": "stretch (v)", "info": "vươn (vai..), ưỡn lưng"},
        {"word": "push (v)", "info": "đẩy"},
        {"word": "pull (v)", "info": "kéo"},
        {"word": "crawl (v)", "info": "bò, trườn"},
    ],
    'Bộ phận cơ thế': [
    {"word": "head (n)", "info": "đầu"},
    {"word": "hair (n)", "info": "tóc"},
    {"word": "face (n)", "info": "gương mặt"},
    {"word": "forehead (n)", "info": "trán"},
    {"word": "eyebrow (n)", "info": "lông mày"},
    {"word": "eye (n)", "info": "mắt"},
    {"word": "eyelash (n)", "info": "lông mi"},
    {"word": "nose (n)", "info": "mũi"},
    {"word": "ear (n)", "info": "tai"},
    {"word": "cheek (n)", "info": "má"} 
    ],
    'Trường học': [
    {"word": "school (n)", "info": "trường học"},
    {"word": "class (n)", "info": "lớp học"},
    {"word": "student (n)", "info": "học sinh, sinh viên"},
    {"word": "pupil (n)", "info": "học sinh"},
    {"word": "teacher (n)", "info": "giáo viên"},
    {"word": "principal (n)", "info": "hiệu trưởng"},
    {"word": "course (n)", "info": "khóa học"},
    {"word": "semester (n)", "info": "học kì"},
    {"word": "exercise (n)", "info": "bài tập"},
    {"word": "homework (n)", "info": "bài tập về nhà"}
    ],
    'Tính cách': [
    {"word": "active (adj)", "info": "năng nổ, lanh lợi"},
    {"word": "alert (adj)", "info": "tỉnh táo, cảnh giác"},
    {"word": "ambitious (adj)", "info": "tham vọng"},
    {"word": "attentive (adj)", "info": "chăm chú, chú tâm"},
    {"word": "bold (adj)", "info": "táo bạo, mạo hiểm"},
    {"word": "brave (adj)", "info": "dũng cảm, gan dạ"},
    {"word": "careful (adj)", "info": "cẩn thận, thận trọng"},
    {"word": "careless (adj)", "info": "bất cẩn, cẩu thả"},
    {"word": "cautious (adj)", "info": "thận trọng, cẩn thận"},
    {"word": "conscientious (adj)", "info": "chu đáo, tỉ mỉ"},
    {"word": "courageous (adj)", "info": "can đảm"}
    ],
    'Đồ dùng học tập': 
    [
    {"word": "pen (n)", "info": "bút mực"},
    {"word": "pencil (n)", "info": "bút chì"},
    {"word": "highlighter (n)", "info": "bút nhớ"},
    {"word": "ruler (n)", "info": "thước kẻ"},
    {"word": "eraser (n)", "info": "tẩy, gôm"},
    {"word": "pencil case (n)", "info": "hộp bút"},
    {"word": "book (n)", "info": "quyển sách"},
    {"word": "notebook (n)", "info": "vở"},
    {"word": "paper (n)", "info": "giấy"},
    {"word": "scissors (n)", "info": "kéo"}
     ],
    'Thiên nhiên ': [
    {"word": "forest (n)", "info": "rừng"},
    {"word": "rainforest (n)", "info": "rừng mưa nhiệt đới"},
    {"word": "mountain (n)", "info": "núi, dãy núi"},
    {"word": "highland (n)", "info": "cao nguyên"},
    {"word": "hill (n)", "info": "đồi"},
    {"word": "valley (n)", "info": "thung lũng, châu thổ, lưu vực"},
    {"word": "cave (n)", "info": "hang động"},
    {"word": "rock (n)", "info": "đá"},
    {"word": "slope (n)", "info": "dốc"},
    {"word": "volcano (n)", "info": "núi lửa"}
    ],
    'Du lịch': [
    {"word": "travel (v)", "info": "đi du lịch"},
    {"word": "depart (v)", "info": "khởi hành"},
    {"word": "leave (v)", "info": "rời đi"},
    {"word": "arrive (v)", "info": "đến nơi"},
    {"word": "airport (n)", "info": "sân bay"},
    {"word": "take off (v)", "info": "cất cánh"},
    {"word": "land (v)", "info": "hạ cánh"},
    {"word": "check in (v)", "info": "đăng ký phòng ở khách sạn"},
    {"word": "check out (v)", "info": "trả phòng khách sạn"},
    {"word": "visit (v)", "info": "thăm viếng"}
]
}
    
        self.albums = {}
        self.review_album = []
        self.current_word = ""
        self.current_info = ""
        self.score = 0
        self.filtered_words = []

    def get_topics(self):
        return list(self.topic_flashcards.keys())

    def get_albums(self):
        return list(self.albums.keys())

    def get_words_from_source(self, source, is_album=False):
        if is_album:
            return [(entry["word"], entry["info"]) for entry in self.albums.get(source, [])]
        return [(entry["word"], entry["info"]) for entry in self.topic_flashcards.get(source, [])]

    def start_new_game(self, words):
        self.filtered_words = words.copy()
        self.score = 0
        return self.next_word()

    def next_word(self):
        if not self.filtered_words:
            return None, None
        
        self.current_word, self.current_info = random.choice(self.filtered_words)
        word_letters = list(self.current_word.lower())
        random.shuffle(word_letters)
        scrambled_word = ''.join(word_letters)
        
        return scrambled_word, self.current_info

    def check_answer(self, user_input):
        user_input = user_input.strip().lower()
        correct = user_input == self.current_word.lower()
        if correct:
            self.score += 1
            self.filtered_words.remove((self.current_word, self.current_info))
        else:
            self.add_to_review(self.current_word, self.current_info)
        return correct

    def skip_current_word(self):
        self.add_to_review(self.current_word, self.current_info)
        return self.next_word()

    def add_to_review(self, word, info):
        if (word, info) not in self.review_album:
            self.review_album.append((word, info))

    def remove_from_review(self, index):
        if 0 <= index < len(self.review_album):
            return self.review_album.pop(index)
        return None

    def get_review_word(self, index):
        if 0 <= index < len(self.review_album):
            return self.review_album[index]
        return None

    def get_review_count(self):
        return len(self.review_album)

    def get_score(self):
        return self.score
    

class WordScrambleUI:
    def __init__(self, backend):
        self.backend = backend
        self.current_review_index = 0
        self.card_flipped = False
        self.game_mode = None
        self.is_game_active = False
        self.current_words = []

    def setup_ui(self):
        with ui.column().classes('w-full max-w-3xl mx-auto p-4'):
            ui.label("Trò Chơi Sắp Xếp Lại Từ").classes('text-3xl font-bold mb-4')
            
            with ui.row().classes('gap-4 mb-4'):
                ui.button("Album của tôi", on_click=lambda: self.show_mode_options('album')).classes('bg-blue-500')
                ui.button("Chủ đề có sẵn", on_click=lambda: self.show_mode_options('topic')).classes('bg-green-500')
            
            self.content_container = ui.column().classes('w-full')
            self.setup_game_interface()
            self.setup_review_section()
            
            # Initially hide game and review sections
            self.game_container.set_visibility(False)
            self.review_container.set_visibility(False)

    def show_mode_options(self, mode):
        self.game_mode = mode
        self.content_container.clear()
        
        with self.content_container:
            if mode == 'album':
                albums = self.backend.get_albums()
                if not albums:
                    ui.label("Bạn chưa có album nào").classes('text-red-500')
                    return
                options = albums
            else:
                options = self.backend.get_topics()

            self.source_select = ui.select(
                label="Chọn nguồn",
                options=options,
                on_change=self.on_source_change
            ).classes('w-full max-w-xs mb-4')

    def on_source_change(self, e):
        if not self.source_select.value:
            return
        
        self.current_words = self.backend.get_words_from_source(
            self.source_select.value, 
            is_album=(self.game_mode == 'album')
        )
        
        if not self.current_words:
            ui.notify('Không có từ nào trong nguồn này', color='warning')
            return
            
        self.game_container.set_visibility(True)
        self.review_container.set_visibility(True)
        self.start_new_game()

    def setup_game_interface(self):
        self.game_container = ui.column().classes('w-full mb-8')
        with self.game_container:
            with ui.row().classes('w-full justify-between mb-4'):
                self.score_label = ui.label('Điểm: 0').classes('text-xl font-bold')
                ui.button('Chơi lại', on_click=self.start_new_game).classes('bg-yellow-500')
            
            self.word_display = ui.label().classes('text-2xl font-bold mb-2 text-center')
            self.hint_label = ui.label().classes('text-gray-600 mb-4 text-center')
            
            with ui.row().classes('w-full gap-2 justify-center'):
                self.input_field = ui.input(placeholder='Nhập từ của bạn...').classes('w-64')
                self.check_button = ui.button("Kiểm tra", on_click=self.check_answer).classes('bg-blue-500')
                self.skip_button = ui.button("Bỏ qua", on_click=self.skip_word).classes('bg-gray-500')

    def setup_review_section(self):
        self.review_container = ui.column().classes('w-full mt-4 p-4 border rounded-lg')
        with self.review_container:
            ui.label("Từ cần ôn tập").classes('text-xl font-bold mb-2')
            self.review_count = ui.label().classes('text-gray-600 mb-4')
            
            self.flashcard = ui.card().classes('w-full h-48 cursor-pointer mb-4')
            with self.flashcard:
                self.card_content = ui.label().classes('text-xl text-center w-full h-full flex items-center justify-center')
            
            with ui.row().classes('w-full justify-center gap-4'):
                ui.button('←', on_click=self.prev_card).classes('bg-gray-500')
                ui.button('Lật thẻ', on_click=self.flip_card).classes('bg-blue-500')
                ui.button('→', on_click=self.next_card).classes('bg-gray-500')
            
            with ui.row().classes('w-full justify-center gap-4 mt-4'):
                ui.button('Đã nhớ', on_click=self.mark_remembered).classes('bg-green-500')
                ui.button('Chưa nhớ', on_click=self.mark_not_remembered).classes('bg-red-500')

    def start_new_game(self):
        if not self.current_words:
            ui.notify('Vui lòng chọn nguồn từ vựng', color='warning')
            return
        
        self.is_game_active = True
        scrambled_word, info = self.backend.start_new_game(self.current_words)
        if scrambled_word and info:
            self.word_display.text = scrambled_word
            self.hint_label.text = f"Gợi ý: {info}"
            self.input_field.value = ''
            self.update_score()
        else:
            ui.notify('Không còn từ nào để học', color='success')
            self.is_game_active = False

    def check_answer(self):
        if not self.is_game_active:
            return
            
        user_input = self.input_field.value
        if not user_input:
            ui.notify('Vui lòng nhập từ', color='warning')
            return
            
        is_correct = self.backend.check_answer(user_input)
        if is_correct:
            ui.notify('Chính xác!', color='success')
            self.update_score()
            self.next_word()
        else:
            ui.notify('Sai rồi, hãy thử lại!', color='error')
        
        self.input_field.value = ''
        self.update_review_section()

    def skip_word(self):
        if not self.is_game_active:
            return
            
        scrambled_word, info = self.backend.skip_current_word()
        if scrambled_word and info:
            self.word_display.text = scrambled_word
            self.hint_label.text = f"Gợi ý: {info}"
            self.input_field.value = ''
        else:
            ui.notify('Đã hoàn thành tất cả các từ!', color='success')
            self.is_game_active = False
            
        self.update_review_section()

    def update_score(self):
        self.score_label.text = f'Điểm: {self.backend.get_score()}'

    def next_word(self):
        scrambled_word, info = self.backend.next_word()
        if scrambled_word and info:
            self.word_display.text = scrambled_word
            self.hint_label.text = f"Gợi ý: {info}"
        else:
            ui.notify('Đã hoàn thành tất cả các từ!', color='success')
            self.is_game_active = False

    def update_review_section(self):
        review_count = self.backend.get_review_count()
        self.review_count.text = f'Số từ cần ôn tập: {review_count}'
        
        if review_count > 0:
            word_info = self.backend.get_review_word(self.current_review_index)
            if word_info:
                word, info = word_info
                self.card_content.text = word if not self.card_flipped else info
        else:
            self.card_content.text = "Chưa có từ nào cần ôn tập"

    def flip_card(self):
        self.card_flipped = not self.card_flipped
        self.update_review_section()

    def prev_card(self):
        if self.backend.get_review_count() > 0:
            self.current_review_index = (self.current_review_index - 1) % self.backend.get_review_count()
            self.card_flipped = False
            self.update_review_section()

    def next_card(self):
        if self.backend.get_review_count() > 0:
            self.current_review_index = (self.current_review_index + 1) % self.backend.get_review_count()
            self.card_flipped = False
            self.update_review_section()

    def mark_remembered(self):
        if self.backend.get_review_count() > 0:
            self.backend.remove_from_review(self.current_review_index)
            if self.current_review_index >= self.backend.get_review_count():
                self.current_review_index = max(0, self.backend.get_review_count() - 1)
            self.update_review_section()

    def mark_not_remembered(self):
        if self.backend.get_review_count() > 0:
            self.next_card()

# from nicegui import ui
# from game_backend import WordScrambleBackend
# from game_frontend import WordScrambleUI
ui.run()
@ui.page('/')
def main():
    backend = WordScrambleBackend()
    game_ui = WordScrambleUI(backend)
    game_ui.setup_ui()

if __name__ == '__main__':
    ui.run()