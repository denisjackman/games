def rot13(message):
    from string import maketrans

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    code = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

    encode = maketrans(alpha,code)
    normal = maketrans(code, alpha)
    return message.translate(encode)