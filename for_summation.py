summation = int(input("What number do you want a summation for: "))
answer=0
solution=0
x=summation
for x in range(summation+1):
    answer=x+answer
print(answer)
