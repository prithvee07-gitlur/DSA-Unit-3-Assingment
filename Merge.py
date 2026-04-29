def mergeSort(nums: list[int]):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n//2
    leftHalf = nums[:mid]
    rightHalf = nums[mid:]
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    return merge(sortedLeft, sortedRight)

def merge(left: list[int], right: list[int]):
    m = len(left)
    n = len(right)
    result = []
    i = j = 0
    while i < m and j < n:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    lis = [3,-1,2,4,0]
    print(mergeSort(lis))

main()