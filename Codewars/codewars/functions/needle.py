def find_needle(haystack):
    if "needle" in haystack:
        result = "found the needle at position " + str(haystack.index("needle"))
    else:
        result = "needle not found"
    return result

print find_needle(["a", "b", True, True, "needle", 1, 2, 3, 4, 5, 6, 7])
print find_needle(["a", "b", True, True, 1, 2, 3, 4, 5, 6, 7])
