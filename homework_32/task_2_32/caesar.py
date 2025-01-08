
def caesar_encode(text, shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            new_letter = chr((ord(letter) + shift - 65) % 26 + 65)
            result += new_letter
        else:
            result += letter
    return result

def caesar_decode(text, shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            new_letter = chr((ord(letter) - shift - 65) % 26 + 65)
            result += new_letter
        else:
            result += letter
    return result


if __name__ == '__main__':
    print(caesar_encode('HELLO, WORLD!', 3))

    print(caesar_decode("KHOOR, ZRUOG!", 3))