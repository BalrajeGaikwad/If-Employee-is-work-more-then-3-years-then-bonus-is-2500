#The current year and the year in which the employee joined the organization are entered through the keyboard. 
#If the number of years for which the employee has served the organization is greater than 3, then a bonus of Rs. 2500/- is given to the employee. 
#If the years of service are not greater than 3, then the program should do nothing.

"""!- current yaer
!- year in which employee joined
!- no of year> 3 --> 2500"""


join_year=int(input("Enter the year in which employee was joined :--"))
current_year=int(input("Enter the current year :-- "))

total_year=current_year-join_year

print(total_year)
emp=0

if(total_year>3):
    emp+=2500
    print(emp," : - employee is able to take a bonus")
else:
    print("not able to take a bonus u need to complete atleast 3 years in organization")