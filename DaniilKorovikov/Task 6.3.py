import string



class Cipher():
    def __init__(self, key):
        self.key = key
        self.real_alphabet = sorted(set(string.ascii_uppercase))
        self.keyword = []
        for letter in key:
            if letter not in self.keyword:
                self.keyword.append(letter.upper())
        self.new_alphabet = self.keyword + sorted(set(string.ascii_uppercase)-set(self.keyword))
        self.d_encode = {key: value for key, value in zip(self.real_alphabet,self.new_alphabet)}
        self.d_decode = {key: value for key, value in zip(self.new_alphabet,self.real_alphabet)}

    def encode(self, s):
        result = []
        for letter in s.upper():
            result.append(self.d_encode[letter] if letter in self.d_encode else letter)
        print(''.join(result))



    def decode(self, s):
        result = []
        for letter in s.upper():
            result.append(self.d_decode[letter] if letter in self.d_decode else letter)
        print(''.join(result))

cipher = Cipher("crypto")
cipher.encode("Hello world")
# # "BTGGJ VJMGP"
#
cipher.decode("Fjedhc dn atidsn")
# "KOJMA IS GENIUS"