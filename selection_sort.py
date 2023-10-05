import random
def selection_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]>nums[j]):
                nums[i],nums[j] = nums[j],nums[i]
    return nums


nums = [random.randint(1,15) for i in range(int(input("Input size array")))]
print(f"Array unsorted: {nums}")
print(f"ARray after selection sort {selection_sort(nums)}")