def closestring(s1,s2):
    n1=len(s1)
    n2=len(s2)
    if n1!=n2:
        return False
    freq1=[0]*26
    freq2=[0]*26
    for i in range(n1):
        idx1=ord(s1[i])-ord('a')
        idx2=ord(s2[i])-ord('a')
        freq1[idx1]+=1
        freq2[idx2]+=1
    for i in range(26):
        has1=freq1[i]>0
        has2=freq2[i]>0
        if has1!=has2:
            return False
    for i in range(1,26):
        key1=freq1[i]
        j=i-1
        while j>=0 and freq1[j]>key1:
            freq1[j+1]=freq1[j]
            j-=1
        freq1[j+1]=key1
        key2=freq2[i]
        k=i-1
        while k>=0 and freq2[k]>key2:
            freq2[k+1]=freq2[k]
            k-=1
        freq2[k+1]=key2
    for i in range(26):
        if freq1[i]!=freq2[i]:
            return False
    return True

s1="abc"
s2="bca"
print(closestring(s1,s2))