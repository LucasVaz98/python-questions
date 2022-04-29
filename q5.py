

class Word: 
    def __init__(self, word):
        self.word = word

    def remove_spaces(self):
        self.word.replace(' ', '', 1)
        self.word[::-1].replace(' ', '', 1)

    def comma_to_exclamation(self):
        self.word.replace(',', '!')

    def change_saudation(self):
        words = self.word.split(' ')
        new_phrase = list()

        for w in words:
            if w == 'Ola':
                new_phrase.append('Bom dia, bebe ')
            else:
                new_phrase.append(w + ' ')

        self.word = new_phrase 

def main():
    word = Word(' Hi, my name is Lucas, ')
    print(word.__dict__)
    print(word.remove_spaces())
    print(word.comma_to_exclamation())
#    print(word.change_saudation())

if __name__ == '__main__':
    main()
