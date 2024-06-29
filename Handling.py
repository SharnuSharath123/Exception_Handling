def enterage(num):
    if num<0:
        raise ValueError("Only integers are allowed")
    
    if num%2==0:
        print("Even")

    else:
        print("Odd")

print("Checking number is even or odd by calling function...")
num=-1
try:
    enterage(num)

except:
    print("ValueError Exception occurred and handled")

print("program completed!!!")


