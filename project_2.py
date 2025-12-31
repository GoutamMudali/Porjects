def get_safe_division():
    while True:
        try:
            num = float(input("Enter a number to divide 100 by: "))
            result = 100 / num
            
        except ValueError:
            print(" Input Error: That's not a valid number. Try again.")
            
        except ZeroDivisionError:
            print(" Math Error: You cannot divide by zero!")
            
        else:
            print(f"✅ Success! 100 / {num} = {result}")
            break 
            
        finally:
            print("--- Attempt complete ---")

get_safe_division()