#Write your code below this line 👇
def prime_checker(number):

    is_prime_number = True

    for num in range(2, round(number / 2)):
        # print(num)
        if number % num == 0:
            is_prime_number = False

    if is_prime_number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
