def oneswaptomakeequal(s1,s):
    n1=len(s1)
    n2=len(s)
    if n1!=n2:
        return False
    diff_count=0
    first_diff=-1
    second_diff=-1
    for i in range(n1):
        if s1[i]!=s[i]:
            diff_count+=1
            if diff_count==1:
                first_diff=i
            elif diff_count==2:
                second_diff=i
            else:
                return False
    if diff_count==0:
        return True
    if diff_count==2:
        return s1[first_diff]==s[second_diff] and s1[second_diff]==s[first_diff]
    return False

s1="bank"
s2="kanb"
print(oneswaptomakeequal(s1,s2))
