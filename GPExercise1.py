num = input("Enter a 3-digit number: ")

if not num.isdigit() or len(num) != 3:
    print("Invalid input, try again. Enter a 3-digit number.")
    
else:
    num = int(num)
    digit1 = num // 100
    digit2 = (num // 10) % 10
    digit3 = num % 10

    sum_of_cubes = digit1**3 + digit2**3 + digit3**3

    if sum_of_cubes == num:
        print(f"The sum of the cubes is {sum_of_cubes}. {num} Armstrong number.")
    else:
        print(f"The sum of the cubes is {sum_of_cubes}. {num} not Armstrong number.")