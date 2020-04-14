#this is a new python file for a small finance company
#we will be using an investment calculator and home loan repayment calculator
#we will be calculating investment interest and bond repayments according to the users input
import math

print("Choose either ''investment'' or ''bond'' from the menu below to proceed:")

print("investment - to calculate the amount of interest you'll earn on interest")
print("bond - to calculate the amount you'll have to pay on a home loan")

calculator = input("Would you like to use the INVESTMENT or BOND calculator? : ")
interest = "SIMPLE" or "COMPOUND"
amount = ()
years = ()
rate = ()
#Get user input
if calculator.upper() == "BOND":
 value = int(input("Enter current value of the house:"))
 percentage = int(input("Enter interest rate:"))
 rate = int(percentage / 100/ 12)
 time = int(input("Enter number of months for repayment:"))
 bond = (rate),value/(1-(1+rate)**(-time))
 #bond = rate * value /(1 - (1+rate)** (-time))
 #bond = value * (rate * math.pow((1+rate), time))/ ((math.pow((1+rate), time))- 1) 
 #bond = value * rate / time
 print(bond)

elif calculator.upper() == "INVESTMENT":
    amount = int(input("Enter amount to be deposited"))
    percentage = float(input("At which percentage of the interest rate?"))
    rate = int(percentage / 100)
    years = int(input("Enter number of years for the investment"))
    interest == input("Would you like SIMPLE or COMPOUND interest? ")
    #Calculate
    if  interest.upper() == "SIMPLE":
        simple = amount *(1+rate*years)
        print(simple)
    elif interest.upper() == "COMPOUND":
        compound = amount * math.pow((1+rate),years)
        print(compound)
    #ouput
    else:
        print("Please enter correct value from above")


     
