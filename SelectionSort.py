


def SelectionSort(nums):
    for i in range(7):
        minpos = i
        for j in range(i,8):
            if nums[j]<nums[minpos]:
                minpos = j

       # nums[minpos], nums[8] = nums[8], nums[minpos]
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)


nums = [5,2,7,9,8,6,4,3]
SelectionSort(nums)