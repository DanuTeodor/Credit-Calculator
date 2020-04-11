import math


# inputs: principal for the amount of money you get, interest for interest rate
principal = int(input("Enter the credit principal:"))
interest_rate= int(input("Enter the interest rate:"))

# to calculate how much it will cost
def total_payment(months):
    total_pay = 0  # to calculate total payment
    month = 1  # to count every month
    rate = principal / months  # without interest
    prin = principal  # use to see how much remained to be paid
    while (month <= months):
        ''' to see how much is interest rate for every month and for first month it will be different from 
        second month and so'''
        interest_rate_monthly = (prin * interest_rate) % 100
        '''total pay is the rate + interest on the that month + how much you paid'''
        total_pay = rate + interest_rate_monthly + total_pay
        prin = prin - (rate + interest_rate_monthly)
        month = month + 1
    return total_pay



''' w - to calculate the months and/or month payment/last payment when you want to take a credit and 
    c - to see how much you will pay at final or monthly when you have a credit '''
print("Do you want to take a credit and do you don't know in how much months or how much you will pay?")
print("type 'w' - to calculate your future credit")
print("type 'c' - to see how much you will pay in total")
w_or_c = input()
if w_or_c in 'w':

    print("What do you want to calculate without interest rate: ")
    print('type "m" - for count of months, ')
    print('type "p" - for monthly payment:')
    option = input()
    if option in 'm':  # you want to see how much time will take to pay it

        print("Enter monthly payment:")
        payment = int(input())
        print("It takes ", round(principal / payment), " months to replay the credid")
    elif option in 'p':

        print("Enter count of months:")
        months = int(input())
        payment = math.ceil(principal / months)
        if (payment * months) != principal:
            last_payment = principal - (payment * (months - 1))
            if last_payment != 0:
                print("Your monthly payment = ", payment, "and last payment = ", last_payment)
        elif (payment * months) == principal:
            print("Your monthly payment = ", payment)
else:
    print(round(total_payment(12), 2))
