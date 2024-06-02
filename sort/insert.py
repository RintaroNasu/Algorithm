from typing import List

def insert_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers
if __name__ == '__main__':
    nums = [2, 5, 1, 8, 7, 3]
    print(insert_sort(nums))
