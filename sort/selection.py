from typing import List

def selectoin_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i+1,len_numbers):
            if(numbers[min_idx] > numbers[j]):
                min_idx = j
        numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]
    return numbers

if __name__ == '__main__':
    nums = [2, 5, 1, 8, 7, 3]
    print(selectoin_sort(nums))
