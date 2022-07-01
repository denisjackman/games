class Converter():
    @staticmethod
    def to_ascii(h):
        return ''.join(chr(int(h[i:i + 2], 16)) for i in range(0, len(h), 2))
    @staticmethod
    def to_hex(s):
        #your code here
        return lambda x: "".join([hex(ord(c))[2:].zfill(2) for c in s])


s="Look mom, no hands"
h="4c6f6f6b206d6f6d2c206e6f2068616e6473"

print s.encode("bin")
