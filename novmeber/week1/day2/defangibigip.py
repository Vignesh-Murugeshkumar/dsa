def defangIPaddr(address: str) -> str:
    chars = []
    for ch in address:
        if ch == ".":
            chars.append("[.]")
        else:
            chars.append(ch)
    return "".join(chars)
s="192.168.1.1"
print(defangIPaddr(s))
