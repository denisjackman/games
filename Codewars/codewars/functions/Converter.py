class Converter():
    @staticmethod
    def to_ascii(h):
        #your code here
        return h.decode("hex")
    @staticmethod
    def to_hex(s):
        #your code here
        return s.encode("hex")


s="Look mom, no hands"
h="4c6f6f6b206d6f6d2c206e6f2068616e6473"

print Converter.to_hex(s) == h
print Converter.to_ascii(h) == s
Test.assert_equals(Converter.to_hex(Converter.to_ascii(h)),h)
Test.assert_equals(Converter.to_ascii(Converter.to_hex(s)),s)