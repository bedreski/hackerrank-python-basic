def validate_string(s):
    alphanumeric = any(c.isalnum() for c in s )
    print("True" if alphanumeric == True else "False")

    alphabetical = any(c.isalpha() for c in s)
    print("True" if alphabetical == True else "False")

    digits = any(c.isdigit() for c in s)
    print("True" if digits == True else "False")

    lowercase = any(c.islower() for c in s)
    print("True" if lowercase == True else "False")

    uppercase = any(c.isupper() for c in s)
    print("True" if uppercase == True else "False")

    return


if __name__ == '__main__':
    s = input()
    validate_string(s)