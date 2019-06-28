
def split_words(string):
    word_count = 0
    string_list = string.split(" ")
    for word in string_list:
        word_count += 1
        char_cnt(word)


def char_cnt(word):
    char_count = 0
    #string_list = string.split(" ")
    for char in word:
        char_count += 1
        #string_length(string)
    print(word, char_count)


if __name__ == "__main__":
    string = "I am new at python"
    split_words(string)







