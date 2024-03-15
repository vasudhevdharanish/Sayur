def calculator(expression):
    nums = expression.split()
    if len(nums) < 3:
        return None
    if not nums[0].isdigit():
        return None
    total = int(nums[0])
    flag=1
    operator = None
    for i in range(1, len(nums)):
        if not nums[i].isdigit() and nums[i] not in ['+', '-', '*', '/']:
            return None
        if nums[i] in ['+', '-', '*', '/']:
            operator = nums[i]
            flag=flag-1
        else:
            flag=flag+1
            if(flag>1):
                return None
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
if not result is None:
    print("Result: ", result)
else:
    print("Invalid expression. Please input a valid expression.")
