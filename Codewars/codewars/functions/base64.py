def to_base_64(string):
    import base64
    return base64.b64encode(string)

def from_base_64(string):
    import base64
    result = base64.b64decode(string).replace("=","")
    return result

print to_base_64("yOCCJ9hqCOKLb")