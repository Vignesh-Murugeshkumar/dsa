def sortwithFre(s):
    freq={} # dict to count frequency of each character
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    chars=list(freq.keys())
    n=len(chars)
    for i in range(n):
        for j in range(i+1,n):
            if freq[chars[j]]>freq[chars[i]]:
                chars[i],chars[j]=chars[j],chars[i]
    result=""
    for ch in chars:
        result+=ch*freq[ch] #to append the character ch freq[ch] times to the result string
    return result
s="banana"
print(sortwithFre(s))