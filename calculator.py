def calculator():
    print("Basic Calculator")
    print("Available Operations: +, -, /, *")
    print()

    try:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        operation=input("Enter operation: ").strip()

        if operation=="+":
            result =num1+num2
            print(f"{num1}+{num2}={result}")

        elif operation=="-":
            result=num1-num2
            print(f"{num1}-{num2}={result}")

        elif operation=="*":
            result=num1*num2
            print(f"{num1}*{num2}={result}")

        elif operation=="/":
            if num2==0:
                    print("Error: Cannot divide by zero!")
            else:
                    result=num1/num2
                    print(f"{num1}/{num2}={result}")
            
        else:
                print("Error: Invalid operation! Please use +, -, *, or /")
        
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    while True:
        calculator()
        again = input("\nWould you like to perform another calculation? (y/n): ")
        if again.lower() not in ('y', 'yes'):
            print("Thank you for using the calculator!")
            break