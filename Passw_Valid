# Password Validation:
code = input()

valid = False
nums = 0
long = len(code)
char = ('!', '@', '#', '$', '%', '&', '*')
nums_char = 0

for i in code:
    if i.isdigit():
        nums += 1
    if i in char:
        nums_char += 1

if nums > 1:
    if nums_char > 1:
        if long >= 7:
            valid = True

if valid == True:
    print("Strong")
else:
    print("Weak")
