def split_and_join_string(s):
    s = s.split(" ")
    s = "-".join(s)
    return s

s = input()
print(split_and_join_string(s))