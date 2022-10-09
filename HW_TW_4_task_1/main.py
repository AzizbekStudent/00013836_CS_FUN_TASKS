def countdown(n): #00013836 countdown
    if n <= 0:  #if number is less or equal to zero show blastoff

        print('Blastoff!')

    else: #if number is more than zero print numbers

        print(n)

        countdown(n - 1)


def count_up(n):  #00013836 countup
    if n >= 0: #if number is more or equal to zero show blastoff
        print("Blastoff!")
    else: #00013836 if number is less than zero start to count up to zero
        print(n)
        count_up(n + 1)

def condition(): #00013836 check users input if it is more than zero call countdown, else call countup
    if n >= 0:
        print("Count down!!")
        countdown(n)
    else:
        print("Count up!!")
        count_up(n)


n = int(input("enter the number: ")) # 00013836 user inputs enter the number
condition() #call the function called condition to check number