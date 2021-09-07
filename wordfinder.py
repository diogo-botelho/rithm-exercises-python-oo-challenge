from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,file_path):
        """Initialize wordfinder with file path and list of words"""
        self.file_path = file_path
        self.file_words = self.get_words()

    def get_words(self):
        """creates list of words from file"""
        file = open(self.file_path, 'r')
        file_words=[]

        for line in file:
            if "\n" in line:
                file_words.append(line[:-1])
            else:
                file_words.append(line)
        return file_words

    def get_random_word(self):
        """gets random word from list of words"""
        return choice(self.file_words)

    
    