path = "books/frankenstein.txt"
def main():
    with open(path) as f:
        file_contents = f.read()
    print(1)
main()
 
def count_words():
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        count_words = len(words)
    print(count_words)
count_words()

def count_character():
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.lower()
        lower_words = words.split()
        characters = {}
        for word in words:
            if word in characters:
                characters[word] += 1
            else:
                characters[word] = 1
        print(characters)   
count_character()