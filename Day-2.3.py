## Your Life in Weeks ##

age=input("what is your current age?")

age_int=int(age)
years_remaining=90-age_int
days_remaining=years_remaining * 365
weeks_remaining=years_remaining * 52
months_remaining=years_remaining * 12


print(f"you have {days_remaining} days, {weeks_remaining} weeks remaining, and {months_remaining} months left.") 
