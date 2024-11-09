#backend:
import random

class WordScrambleBackend:
    def __init__(self):
        self.albums = {}  # Dictionary to store flashcard albums
        self.review_album = []  # Album for words that need review
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
        }

    def get_albums(self):
        return self.albums
    
    def get_topic_flashcards(self):
        return self.topic_flashcards
    
    def get_review_album(self):
        return self.review_album

    def add_to_review(self, word, info):
        if (word, info) not in self.review_album:
            self.review_album.append((word, info))

    def remove_from_review(self, index):
        if 0 <= index < len(self.review_album):
            return self.review_album.pop(index)
        return None

    def get_words_from_source(self, source, mode='topic'):
        if mode == 'album':
            return [(entry["word"], entry["info"]) for entry in self.albums.get(source, [])]
        else:
            return [(entry["word"], entry["info"]) for entry in self.topic_flashcards.get(source, [])]

    def scramble_word(self, word):
        word_letters = list(word.lower())
        random.shuffle(word_letters)
        return ''.join(word_letters)
    

#front end:
import random
from nicegui import ui
from backend import WordScrambleBackend

class WordScrambleGame:
    def __init__(self, container):
        self.container = container
        self.backend = WordScrambleBackend()
        self.current_word = ""
        self.current_info = ""
        self.scrambled_word = ""
        self.score = 0
        self.filtered_words = []
        self.game_mode = None
        self.is_game_active = False
        self.current_review_index = 0
        self.card_flipped = False
        self.setup_ui()

    def setup_ui(self):
        with self.container:
            ui.label("Trò Chơi Sắp Xếp Lại Từ").classes('text-3xl font-bold mb-4')
            
            with ui.row().classes('gap-4 mb-4'):
                ui.button("Album của tôi", on_click=lambda: self.show_mode_options('album')).classes('bg-blue-500')
                ui.button("Chủ đề có sẵn", on_click=lambda: self.show_mode_options('topic')).classes('bg-green-500')
            
            self.mode_container = ui.column().classes('w-full mb-4')
            self.setup_game_controls()
            self.setup_game_interface()
            self.setup_review_section()

    def setup_game_controls(self):
        self.game_controls = ui.column().classes('w-full mb-4')
        with self.game_controls:
            self.start_button = ui.button("Bắt đầu", on_click=self.start_new_game).classes('bg-green-500')
            self.reset_button = ui.button("Chơi lại", on_click=self.reset_game).classes('bg-yellow-500')
        self.game_controls.set_visibility(False)

    def setup_game_interface(self):
        self.game_interface = ui.column().classes('w-full')
        with self.game_interface:
            self.score_label = ui.label(f"Điểm: {self.score}").classes('text-lg mb-2')
            self.word_display = ui.label().classes('text-xl mb-2')
            self.hint_label = ui.label().classes('text-sm text-gray-500 mb-2')
            
            with ui.row().classes('gap-2'):
                self.input_box = ui.input(placeholder='Nhập từ của bạn...').classes('w-64')
                self.check_button = ui.button("Kiểm tra", on_click=self.check_word).classes('bg-blue-500')
                self.skip_button = ui.button("Bỏ qua", on_click=self.skip_word).classes('bg-gray-500')
        self.game_interface.set_visibility(False)

    def setup_review_section(self):
        self.review_section = ui.column().classes('w-full mt-4')
        with self.review_section:
            ui.label("Từ cần ôn tập").classes('text-xl font-bold mb-2')
            self.review_count_label = ui.label().classes('text-sm text-gray-600 mb-2')
            
            self.flashcard = ui.card().classes('w-full h-48 cursor-pointer mb-4')
            with self.flashcard:
                self.card_content = ui.label().classes('text-xl text-center w-full h-full flex items-center justify-center')
            
            with ui.row().classes('w-full justify-center gap-4'):
                ui.button('←', on_click=self.prev_card).classes('bg-gray-500')
                ui.button('Lật thẻ', on_click=self.flip_card).classes('bg-blue-500')
                ui.button('→', on_click=self.next_card).classes('bg-gray-500')
            
            with ui.row().classes('w-full justify-center gap-4 mt-4'):
                ui.button('Đã nhớ', on_click=self.mark_as_remembered).classes('bg-green-500')
                ui.button('Chưa nhớ', on_click=self.mark_as_not_remembered).classes('bg-red-500')
        self.review_section.set_visibility(False)

    # ... (rest of the methods remain the same as in your original code, 
    # but now using self.backend to access the backend functionality)

@ui.page('/')
def main():
    with ui.column().classes('w-full max-w-3xl mx-auto p-4'):
        word_scramble_game = WordScrambleGame(ui.column().classes('w-full'))

if __name__ == '__main__':
    ui.run()
