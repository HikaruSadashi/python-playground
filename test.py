def isDuplicate(nums, index):
  result = False
  for i in nums:
    if index == nums[i-1] and index != i-1:
      result = True
  return result  

def containDup(nums, elementIndex):
    result = False
    element = nums[elementIndex]

    for fakeIndex in nums:
        i = fakeIndex - 1
        
        if element == nums[i] and element != elementIndex:
            result = True
            print("Match found")
            break
    
    return result

nums = [1, 2, 3, 4]

print(containDup(nums, 3))