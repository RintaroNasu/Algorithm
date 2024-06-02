from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if (numbers[j] > numbers[j+1]):
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers

if __name__ == '__main__':
    nums = [2, 5, 1, 8, 7, 3]
    print(bubble_sort(nums))

# for文が2回繰り返されているのでn^2になる
