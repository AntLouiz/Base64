import string
from textwrap import wrap

ascii_uppercase = list(string.ascii_uppercase)
ascii_lowercase = list(string.ascii_lowercase)
specials = ['/', '+']
numbers = list(str(n) for n in range(10))

alphabet_base_64 = ascii_uppercase + ascii_lowercase + numbers + specials


def encode_base64(word):
    binaries = [format(ord(c), '08b') for c in word]
    word_binary_len = sum([len(b) for b in binaries])
    if word_binary_len < 24:
        binaries = ''.join(binaries)
        binaries = '{:024d}'.format(int(binaries))
    else:
        binaries = ''.join(binaries)

    binaries = wrap(binaries, 6)
    cod_word = [alphabet_base_64[int(b, 2)] for b in binaries]

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


if __name__ == '__main__':
    main()
