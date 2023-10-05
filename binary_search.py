import random
def binary_search(nums,value):
    lo = 0
    high = len(nums)
    while(lo<=high):
        mid = (lo+high)//2
        if(nums[mid]==value):
            return mid
        elif(nums[mid]>value):
            high = mid - 1
        elif(nums[mid]<value):
            lo = mid + 1
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binary_search(nums,15))