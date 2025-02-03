def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


print(spy_game([0, 1, 0, 7])) 
print(spy_game([0, 7, 0]))  