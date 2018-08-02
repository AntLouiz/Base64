import string
from textwrap import wrap

# alfabeto com letras maiusculas
ascii_uppercase = list(string.ascii_uppercase)

# alfabeto om letras minusculas
ascii_lowercase = list(string.ascii_lowercase)

# barra e o caractere de adiçao
specials = ['/', '+']

# numeros de 0 a 9
numbers = list(str(n) for n in range(10))

alphabet_base_64 = ascii_uppercase + ascii_lowercase + numbers + specials


def encode_base64(word):
    binaries = []
    word_binary_len = 0
    cod_word = []

    for w in word:
        word_binarie = format(ord(w), '08b')
        binaries.append(word_binarie)

    for b in binaries:
        word_binary_len += len(b)

    if word_binary_len < 24:
        binaries = ''.join(binaries)
        binaries = '{:024d}'.format(int(binaries))

    else:
        binaries = ''.join(binaries)

    binaries = wrap(binaries, 6)

    for b in binaries:
        decimal = int(b, 2)
        cod_word.append(alphabet_base_64[decimal])

    return ''.join(cod_word)


def decode_base64(hash_text):
    binaries = ['{:06b}'.format(alphabet_base_64.index(w)) for w in hash_text]
    binaries = ''.join(binaries)
    binaries = wrap(binaries, 8)
    word = [chr(int(b, 2)) for b in binaries]

    return ''.join(word)


def main():
    word = str(input('Insira uma palavra para ser codificada: '))
    cod_word = encode_base64(word)
    decode_word = decode_base64(cod_word)

    print("Palavra criptografada: {}\nPalavra descriptografada: {}".format(
        cod_word,
        decode_word
    ))


if __name__ == '__main__':
    main()
