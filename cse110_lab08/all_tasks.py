# nums = [1,2,5,33,55,22,4,-9,-3,-5,-2]

# nums_sorted = sorted(nums, reverse=True) #outer place sort

# print(nums_sorted)
###############################################################

# inventory = {"lays":10,"sun":20, "alooz":30, "meridian":15}

# inventory_sorted = sorted(inventory)

# print(inventory_sorted)


# dic = {}
# for key in inventory_sorted:
#     dic[key] = inventory[key]
# print(dic)
###############################################################


#sort built in function only works with lists. It basically sorts the list in place method..

# nums = [1,2,5,33,55,22,4,-9,-3,-5,-2]

# nums.sort()

# print(nums)

# nums = [1,2,5,33,55,22,4,-9,-3,-5,-2]

# nums.sort(reverse=True)

# print(nums)

#SELECTION SORT__________________________

# nums = [7,5,4,2]

# for i in range(len(nums)):
#     min_index = i

#     for j in range(i+1, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
    
#     temp = nums[min_index]
#     nums[min_index] = nums[i]
#     nums[i] = temp


# print(nums)


# def selection_sort(nums):
#     for i in range(len(nums)):
#         min_idx = i
#         for j in range(i+1, len(nums)):
#             if nums[j] < nums[min_idx]:
#                 min_idx = j
#         nums[i], nums[min_idx] = nums[min_idx], nums[i]
#     return nums

# nums = [7, 5, 4, 2]
# print(selection_sort(nums))


# nums = [5,9,4,3,8,1,7,6,2]

# for i in range(len(nums)):
#     for j in range(0, len(nums)-i-1):
#         if nums[j] > nums[j+1]:
#             temp = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]= temp

# print(nums)



# my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]


# for i in range(len(my_list)):
#     for j in range(0, len(my_list)-i-1):
#         if my_list[j] > my_list[j+1]:
#             temp = my_list[j]
#             my_list[j] = my_list[j+1]
#             my_list[j+1] = temp

# print(my_list)



# my_list= [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]


# for i in range(len(my_list)):
#     min_idx = i
#     for j in range(i+1, len(my_list)):
#         if my_list[j] < my_list[min_idx]:
#             min_idx = j

#     temp = my_list[min_idx]
#     my_list[min_idx] = my_list[i]
#     my_list[i] = temp


# print(my_list)



# my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]


# for i in range(len(my_list)):
#     for j in range(0, len(my_list)-i-1):
#         if my_list[j] < my_list[j+1]:
#             temp = my_list[j+1]
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp

# print(my_list)



sitting_list = [10,30,20,70,11,15,22,16,58,100,12,56,70,80]


ascending_list = []
descending_list = []

for i in range(len(sitting_list)):
    if sitting_list[i] % 2 == 0:
        ascending_list.append()

print(ascending_list)