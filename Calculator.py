def calculator(expression):
    nums = expression.split()
    
    total = int(nums[0])
    operator = None
    for i in range(1, len(nums)):
        if nums[i] in ['+', '-', '*', '/']:
            operator = nums[i]
        else:
            if operator == '+':
                total += int(nums[i])
            elif operator == '-':
                total -= int(nums[i])
            elif operator == '*':
                total *= int(nums[i])
            elif operator == '/':
                total /= int(nums[i])
    
    return total

expression = input("Enter the expression to calculate: ")
result = calculator(expression)
print("Result: ", result)
