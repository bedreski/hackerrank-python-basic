n = int(input("Digite um inteiro: "))

if n >= 1 and n <= 100:
    if n % 2 == 1:
        print("Weird")
    else:
        if n % 2 == 0 and 2 <= n <= 5:
            print("Not Weird")
        else:
            if n % 2 == 0 and 6 <= n <= 20:
                print("Weird")
            else:
                if n % 2 == 0 and n > 20:
                    print("Not Weird")
