# try : Error message write inside this try block.
# except : executes only when exception occurred.
# else : executes only when exceptions not occurred.
# finally : always executives

try:
    num1,num2=10.0
    result=num1/num2
    print("Result is: ", result)

except ZeroDivisionError:
    print("Thrown ZeroDivisionError exception...")

except SyntaxError:
    print("Thrown SyntaxError exception...")

except:
    print("Exception handled...")

else:
    print("No exception occurred...")

finally:
    print("Always execute...")
