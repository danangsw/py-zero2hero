

def days_to_hours(days):
    i_days = int(days)
    return (f"{i_days} days is {i_days * 24} hours")


user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
result = days_to_hours(user_input)
print(f"Awesome!, {result}")