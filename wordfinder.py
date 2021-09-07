from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,file_path):
        """Initialize wordfinder with file path and list of words"""
        #self.file_path = file_path
        file = open(file_path, 'r')
        self.words = self.get_words(file)
        #Print a message that we did this correctly

    def get_words(self):
        """creates list of words from file"""
        return [line.strip() for line in file] #Elie's way
        
        #Our way:
        # words = []
        # for line in file:
        #     if "\n" in line:
        #         words.append(line[:-1])
        #     else:
        #         words.append(line)
        # return words

    def get_random_word(self):
        """gets random word from list of words"""
        return choice(self.words)

    
class SpecialWordFinder(WordFinder):
    """Random Word Finder: Extends WordFinder, ignores empty lines and lines starting with #"""
    #Import the init of WordFinder
    #New method goes line by line and has if statement that ignores if the line starts with # or is empty
    #Option 1: Import the get_words and have a second method to read the words and remove "#" and "" elements
    #Option 2: Have a new get_words
    #Import get_random_word method

    # def __init__(self,file_path):
    #     '''Initializes Special Word Finder with inherited init from WordFinder and runs method trim_file_words'''
    #     super().__init__(file_path)
    #     self.trim_file_words()

    def get_words(self,file):
        '''Removes blank links and # from file'''
        return [word for word in super().get_words(file) if not (word == "" or word.startswith("#"))]
