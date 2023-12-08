"""
Basic
"""

# String
print("The " + str(3000) + " is great number")
print(f"The {3000} is great number" )


# Number
print(3000 + 2000)
print(45.6 + 0.001)
print(20 * 24 * 60)

# Variables
days_to_hrs = 24
days_to_secs= days_to_hrs * 3600
n_days = 20
u_second = "seconds"
u_hours = "hours"
u_days = "days"

print(f"{n_days} {u_days} is {n_days * days_to_secs} {u_second}")

# Encapsulate logic with
def days_to_seconds(days):
    print(f"{days} days is {days * 24 * 3600} seconds")


def days_to_minutes(days):
    print(f"{days} days is {days * 24 * 60} minutes")


def days_to_hours(days):
    print(f"{days} days is {days * 24} days")


def add_number(a, b):
    return a + b


def scope_check(p_days):
    my_var = "variable inside function"
    n_days = "abc"
    print(n_days, p_days, u_second)
    print(my_var)



days_to_seconds(1)
days_to_seconds(20)

days_to_minutes(1)
days_to_minutes(20)

days_to_hours(1)
days_to_hours(20)

print (add_number(1, 2), add_number(3, 4), add_number(5, 6))

scope_check(300)