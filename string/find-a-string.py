#Solution: https://www.geeksforgeeks.org/python/python-ways-to-count-number-of-substring-in-string/

def count_substring(string, sub_string):

    if 1 < len(string) < 200:
        cnt = 0

        for i in range(len(string) - len(sub_string) + 1):
            if string[i:i + len(sub_string)] == sub_string: 
                cnt += 1
        return cnt

    return 0

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)