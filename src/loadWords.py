
def load_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()