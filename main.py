import os
import string
from textwrap import wrap

# alfabeto com letras maiusculas
ascii_uppercase = list(string.ascii_uppercase)

# alfabeto om letras minusculas
ascii_lowercase = list(string.ascii_lowercase)

# barra e o caractere de adiçao
specials = ['/', '+']

# numeros de 0 a 9
numbers = []
for n in range(10):
    numbers.append(str(n))

alphabet_base_64 = ascii_uppercase + ascii_lowercase + numbers + specials


def encode_base64(word):
    binaries = []
    word_binary_len = 0
    cod_word = []

    # percorrendo a palavra
    for w in word:
        word_number_ascii = ord(w)
        word_binarie = format(word_number_ascii, '08b')
        binaries.append(word_binarie)

    for b in binaries:
        word_binary_len += len(b)

    if word_binary_len < 24:
        binaries = ''.join(binaries)
        binaries = '{:024d}'.format(int(binaries))

    else:
        binaries = ''.join(binaries)

    # separa em grupos de 6 bits
    binaries = wrap(binaries, 6)

    for b in binaries:
        decimal = int(b, 2)
        cod_word.append(alphabet_base_64[decimal])

    return ''.join(cod_word)


def decode_base64(hash_text):
    binaries = []
    decoded_word = []

    for h in hash_text:
        decimal = alphabet_base_64.index(h)
        binarie = '{:06b}'.format(decimal)
        binaries.append(binarie)

    binaries = ''.join(binaries)
    binaries = wrap(binaries, 8)

    for b in binaries:
        integer_word = int(b, 2)
        decoded_word.append(chr(integer_word))

    return ''.join(decoded_word)


def main():
    filename = 'test.txt'
    with open(filename, 'r') as file:
        text_encoded = encode_base64(file.read())

    os.remove(filename)

    with open(filename, 'w') as file:
        file.write(text_encoded)


if __name__ == '__main__':
    main()
