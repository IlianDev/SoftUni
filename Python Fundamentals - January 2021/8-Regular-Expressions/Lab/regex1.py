text = "Hello there some nums 1234. That is all."

index = 0
nums = ""
while index < len(text):
    if text[index].isdigit():
        while text[index].isdigit():
            nums += text[index]
            index += 1
        nums = int(nums)
    index += 1

print(nums)
