def find_word_offset(file_path, target):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            offset = content.find(target)
            if offset != -1:
                print(f'"{target.decode()}" expression found at {offset} address.')
            else:
                print(f'"{target.decode()}" expression not found in any location.')
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    path = "wordlist.txt"
    word = b"word"
    
    find_word_offset(path, word)