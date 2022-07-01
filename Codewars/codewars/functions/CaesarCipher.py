
class CaesarCipher:

    def __init__(self,shift):
        self.shift = shift

    def encode(self, str):
        result = ""
        temp = str.upper()
        r = range(65, 91)
        for letter in temp:

            if (ord(letter) in r):
                if ((ord(letter) + self.shift) > 90):
                    num = ((ord(letter) + self.shift) - 91) + 65
                else:
                    num = ord(letter) + self.shift
                result = result + chr(num)
            else:
                result = result + letter
        return result

    def decode(self, string):
        result = ""
        temp = string.upper()
        r = range(65, 91)
        for letter in temp:
            if (ord(letter) in r):
                if (ord(letter) - self.shift) < 65 :
                    num = 91 - (65 - (ord(letter) - self.shift))
                else:
                    num = ord(letter) - self.shift
                result = + chr(num)
            else:
                result = + letter
        return result

c = CaesarCipher(13)
print c.encode("PANCAKES")
print c.decode("CNAPNXRF")
