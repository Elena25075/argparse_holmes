import argparse

parser = argparse.ArgumentParser(description="This is interesting.")
parser.add_argument("-f", "--file")

args = parser.parse_args()

filename = args.file

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)

opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened

decode_Caesar_cipher(encoded_text, -13)


