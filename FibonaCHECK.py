def main():
    print("Welcome to FibonaCHECK!")
    while True:
        try:
            choice = int(input("Enter '1' to check if a number belongs to the Fibonacci sequence.\nEnter '2' to check the Fibonacci number of an nth term\nEnter '3' to check the nth term of a Fibonacci number.\nWhat do you want to check? Enter the number:\n"))
            if choice == 1:
                print("You chose '1'. Let's check if a number belongs to the Fibonacci sequence.")
                while True:
                    try:
                        import math
                        x = int(input("Enter the Number:\n"))
                        if x < 0:
                            print("Invalid input. Please try again.")
                        if x == 0:
                            print(x, "belongs to the Fibonacci sequence.")
                            break
                        elif x > 0:
                            formula = (5*(x**2))+4
                            secondFormula = (5*(x**2))-4
                            squareRoot = math.sqrt(formula)
                            secondSquareRoot = math.sqrt(secondFormula)
                            if squareRoot == int(squareRoot) or secondSquareRoot == int(secondSquareRoot):
                                print(x, "belongs to the Fibonacci sequence.")
                                break
                            else:
                                print(x, "does not belong to the Fibonacci sequence.")
                                break
                    except:
                        print("Ivalid input. Please try again.")
                break
            elif choice == 2:
                print("You chose '2'. Let's check the Fibonacci number of an nth term.")
                while True:
                    try:
                        num = int(input("Enter the nth term:\n"))
                        n1 = 0
                        n2 = 1
                        nth = 0
                        if num <= 0:
                            print("Invalid input. Please try again.")
                        elif num == 1:
                            print("The 1st term of the Fibonacci sequence is 0.")
                            break
                        elif num== 2:
                            print("The 2nd term of the Fibonacci sequence is 1.")
                            break
                        elif num== 3:
                            print("The 3rd term of the Fibonacci sequence is 1.")
                            break
                        else:
                            while nth < num:
                                fibo = n1 + n2
                                n1 = n2
                                n2 = fibo
                                nth += 1
                                if nth == num-1:
                                    n = n1
                                    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(num % 10, 4)]
                                    if 11 <= (num % 100) <= 13:
                                        suffix = 'th'
                                    print ("The", str(num) + suffix,"term of the Fibonacci sequence is",n)
                                    break
                            break
                    except:
                        print("Ivalid input. Please try again.")
                break
            elif choice == 3:
                print("You chose '3'. Let's check the nth term of a Fibonacci number.")
                while True:
                    try:
                        num = int(input("Enter the Fibonacci number:\n"))
                        n1 = 0
                        n2 = 1
                        nth = 0
                        if num < 0:
                            print("Invalid inout. Please try again.")
                        elif num == 0:
                            print("0 is the 1st term of the Fibonacci sequence.")
                            break
                        elif num == 1:
                            print("1 is the 2nd or the 3rd term of the Fibonacci sequence.")
                            break
                        else:
                            import math
                            formula = (5*(num**2))+4
                            secondFormula = (5*(num**2))-4
                            squareRoot = math.sqrt(formula)
                            secondSquareRoot = math.sqrt(secondFormula)
                            if squareRoot == int(squareRoot) or secondSquareRoot == int(secondSquareRoot):
                                while nth < num:
                                    fibo = n1 + n2
                                    n1 = n2
                                    n2 = fibo
                                    nth += 1
                                    if fibo == num:
                                        n = nth + 2
                                        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
                                        if 11 <= (n % 100) <= 13:
                                            suffix = 'th'
                                        print (num,"is the", str(n) + suffix,"term of the Fibonacci sequence.")
                                        break
                                break
                            else:
                                print(num,"is not a Fibonacci number.Please try again.")
                    except:
                        print("Invalid input. Please try again.")
                break
            else:
                print("Invalid input. Please try again.")
        except:
            print("Invalid input. Please try again.")
            
    while True:
        again = input("Do you want to try again? Enter 'YES' or 'NO'\n")
        if again == 'YES' or again == 'Yes' or again == 'yes':
            main()
            break
        elif again == 'NO' or again == 'No'or again == 'no':
            print("Thank you.")
            break
        else:
            print("Please enter only 'YES' or 'NO'")
main()