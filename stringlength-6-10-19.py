# Define the length of the string, print out the text and print the string length
def str_len(text):
    #print(text)
    count = 0
    for char in text:
        #print(char)
        count += 1
    print(text, ": ", count)


def sep_word(text):
    text_list = text.split(" ")
    word_count = 0
    for word in text_list:
        word_count += 1
        str_len(word)
    print(word_count)


if __name__ == "__main__":
    text = "I like pie"

    sep_word(text)
