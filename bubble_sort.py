import random
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if(nums[j-1]>nums[j]):
                nums[j-1],nums[j] = nums[j],nums[j-1]

    return nums
nums = [random.randint(1,15) for i in range(int(input("Input size array: ")))]
print(f"Array not sorted {nums}")
print(f"Array sorted: {bubble_sort(nums)}")