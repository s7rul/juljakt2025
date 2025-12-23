import sys

def get_key_from_file(file_name):
    key = dict()

    with open(file_name) as key_file:
        for line in key_file:
            parts = line.strip().split('-')
            key[parts[0][0]] = parts[1][0]


    return key

def encrypt_decrypt(key_file, text_file):
    key = get_key_from_file(key_file)

    with open(text_file) as text:
        for line in text:
            for c in line:
                replace = key.get(c)
                if not replace == None:
                    print(replace, end="")
                else:
                    print(c, end="")
    

def __main__():
    key_file = sys.argv[1]
    text_file = sys.argv[2]

    encrypt_decrypt(key_file, text_file)

__main__()
