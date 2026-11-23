def mimchangeforbinary(s):
    n=len(s)
    mis_zero=0
    mis_one=0
    for i in range(n):
        if i%2==0:
            if s[i]!='0':
                mis_zero+=1
            else:
                mis_one+=1
        else:
            if s[i]!='1':
                mis_zero+=1
            else:
                mis_one+=1
    mis_one=n-mis_one
    if mis_zero<mis_one:
        return mis_zero
    return mis_one
s="0100"
print(mimchangeforbinary(s))