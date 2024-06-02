import random

def in_order(numbers: list) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

def bogo_sort(numbers: list) -> list:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

if __name__ == '__main__':
    print(bogo_sort([1,2,3,6,5]))

# bogoソートは運が良ければ早く終わるがかなり時間がかかる。
