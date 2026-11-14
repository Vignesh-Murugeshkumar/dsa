def toLowerCase(s: str) -> str:
    chars = []
    for ch in s:
        code = ord(ch)
        if 65 <= code <= 90:  # 'A' to 'Z'
            chars.append(chr(code + 32))
        else:
            chars.append(ch)
    return "".join(chars)
s="Hello World"
print(toLowerCase(s))