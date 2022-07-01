'''
In DNA strings, symbols "A" and "T" are complements of each other,
as "C" and "G". You have function with one side of the DNA (string,
except for Haskell); you need to get the other complementary side.
DNA strand is never empty or there is no DNA at all (again, except for Haskell).

'''
def DNA_strand(dna):
    # code here
    dnacopy = dna.upper()
    result = ""
    for letter in dnacopy:
        if letter == "A":
            result += "T"
        if letter == "T":
            result += "A"
        if letter == "G":
            result += "C"
        if letter == "C":
            result += "G"

    return result


print DNA_strand("GAT")