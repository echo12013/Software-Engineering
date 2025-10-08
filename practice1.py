def max_subarray_sum(nums):

    if not nums:
        return 0
    
    max_sum = nums[0]  
    current_sum = nums[0]  
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# 测试用例
test_cases = [
    [1, -2, 3, 5, -1],      
    [1, -2, 3, -8, 5, 1],  
    [1, -2, 3, -2, 5, 1],   
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],  
    [-1, -2, -3, -4],       
]

for i, test in enumerate(test_cases):
    result = max_subarray_sum(test)
    print(f"测试用例 {i+1}: {test} -> {result}")