summation = int(input("What number do you want a summation for: "))
answer=0
solution=0
x=summation
while x >= 0:
    solution=x+solution
    x=x-1
print(solution)
