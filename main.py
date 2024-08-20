path = "books/frankenstein.txt"
def main():
    with open(path) as f:
        file_contents = f.read()
    print(f"--- Begin report of {path} ---")
main()
 
def count_words():
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        count_words = len(words)
    print(f"{count_words} words found in the document")
count_words()

def count_character():
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.lower()
        lower_words = words.split()
        characters = {}
        for word in words:
            if word.isalpha() == True:
                if word in characters:
                    characters[word] += 1
                else:
                    characters[word] = 1
        return characters
count_character()


dict = count_character()
dict_list = [{"char": k, "num": v} for k, v in dict.items()]

def sort_on(dict):
    return dict["num"]

dict_list.sort(reverse=True, key=sort_on)


for i in dict_list:
    character = i["char"]
    number = i["num"]
    print(f"The {character} character was found {number} times")

print("--- End report ---")