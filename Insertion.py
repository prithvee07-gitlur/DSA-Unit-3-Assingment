def insertionSort(nums: list[int]):
    n = len(nums)
    for i in range(1, n):
        j = i - 1
        key = nums[i]
        
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
            
        nums[j+1] = key

def main():
    lis = [3,-1,2,4,0]
    insertionSort(lis)
    print(lis)

main()
