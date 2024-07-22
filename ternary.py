# <expression_if_true> if <condition> else <expression_if_false>

x = 5
y = 10

# Assign the larger value to max_value
max_value = x if x > y else y

print(max_value)  # Output: 10


def check_age(age):
    return "Adult" if age >= 18 else "Minor"

print(check_age(20))  # Output: Adult
print(check_age(15))  # Output: Minor


score = 85

grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

print(grade)  # Output: B


x = 5
y = 10

if x > y:
    max_value = x
else:
    max_value = y

print(max_value)  # Output: 10


numbers = [1, 2, 3, 4, 5]
squared_even_numbers = [x**2 if x % 2 == 0 else x for x in numbers]

print(squared_even_numbers)  # Output: [1, 4, 3, 16, 5]
