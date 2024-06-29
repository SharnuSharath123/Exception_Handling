try:
    num1,num2=10.0
    result=num1/num2
    print("Result is: ", result)

except:
    print("Exception handled")

else:
    print("No exception occurred")

finally:
    print("Always execute...")
