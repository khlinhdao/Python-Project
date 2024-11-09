import requests
# backend
class DictionaryBackend:
    def __init__(self):
        self.api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    def get_word_info(self, word):
        response = requests.get(self.api_url.format(word=word))
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Example usage:
backend = DictionaryBackend()
word_data = backend.get_word_info('example')
print(word_data) 

# frontend
class DictionaryFrontend:
    def __init__(self, backend):
        self.backend = backend

    def search_word(self):
        word = input("Enter a word to search: ").strip()
        if not word:
            print("Please enter a word to search.")
            return
        
        word_info = self.backend.get_word_info(word)
        if word_info:
            self.display_word_info(word_info)
        else:
            print(f"No information found for word: '{word}'")

    def display_word_info(self, word_info):
        word_data = word_info[0]
        phonetic = word_data.get('phonetic', 'No phonetic available')
        meanings = word_data.get('meanings', [])

        print(f"\nWord: {word_data['word']}")
        print(f"Phonetic: {phonetic}\n")

        for meaning in meanings:
            part_of_speech = meaning.get('partOfSpeech', '')
            definitions = meaning.get('definitions', [])
            print(f"{part_of_speech.capitalize()}:")
            for i, definition in enumerate(definitions, 1):
                print(f" {i}. {definition.get('definition', '')}")
                if 'example' in definition:
                    print(f"    Example: {definition['example']}")
            print()  # Add space between meanings

def main():
    backend = DictionaryBackend()
    frontend = DictionaryFrontend(backend)
    frontend.search_word()

if __name__ == "__main__":
    main()
