#
x = 0
# # break statement
#
# while x < 10:
#     print(x)
#     if x == 5:
#         break
#     x +=1

# continue statement
# continue skips the current iteration that has met the condition  being tested
while x < 10:
    x += 1
    if x == 5: # condition being tested
        continue
    print(x)
