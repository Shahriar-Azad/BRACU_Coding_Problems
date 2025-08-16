#SELECTION SORT__________________________

nums = [7,5,4,2]

for i in range(len(nums)):
    min_index = i

    for j in range(i+1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    
    temp = nums[min_index]
    nums[min_index] = nums[i]
    nums[i] = temp


print(nums)


