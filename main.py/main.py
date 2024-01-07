def main():
    book_path = "/home/brad/workspace/github.com/bradweber22/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_character(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print (f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")


    print ("--- End report ---")
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




    
def get_num_character(text):
    count = {}
    for i in text.lower():
        if i in count:
            count [i] = count[i] + 1
        else:
            count [i] = 1
    return count


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


    
    



main()