def capitalizeTitle(title: str) -> str:
    chars = list(title)
    n = len(chars)
    start = 0

    for end in range(n + 1):
        if end == n or chars[end] == " ":
            word_len = end - start
            for i in range(start, end):
                code = ord(chars[i])
                if word_len > 2 and i == start:
                    # Force uppercase if currently lowercase ('a'-'z': 97-122)
                    if 97 <= code <= 122:
                        chars[i] = chr(code - 32)
                else:
                    # Force lowercase if currently uppercase ('A'-'Z': 65-90)
                    if 65 <= code <= 90:
                        chars[i] = chr(code + 32)
            start = end + 1

    return "".join(chars)
s="capiTalIze tHe titLe"
print(capitalizeTitle(s))
