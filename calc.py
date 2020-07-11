print("calculator")

x=int(input())

print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLY")
print("4. divide")

choice = input("select choice from 1./2./3./4.")
y=int(input())

if(choice=='1'):
    print(x+y)
elif(choice=='2'):
    print(x-y)
elif(choice=='3'):
    print(x*y)
elif(choice=='4'):
    print(x/y)
else:
    print("invalid input")
