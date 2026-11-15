def rotate_string(s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in (s + s)
s="abcde"
goal="cdeab"    
print(rotate_string(s, goal))