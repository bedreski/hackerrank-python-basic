# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem 

def find_runner_up(arr):
    ranking = []
    no_equals = []

    no_equals = list(set(arr))

    ranking = no_equals
    ranking.sort(reverse=True)

    return ranking.pop(1)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(find_runner_up(arr))
