import random

def simulate(pfunc, student_num, runs):
    matches = len([run for run in range(runs) if pfunc(student_num)])
    return matches / runs

students = 100
runs = 100

# problem 1
# given a pre-defined date, 
# what is the value of n such that the probability of having 
# a match is greater than or equal to 0.5?

def problem_1_simulate(student_num):
    birthday = random.randint(1, 365)
    birthdays = [random.randint(1, 365) for _ in range(student_num)]
    return birthday in birthdays

def problem_1_analytic(student_num):
    prob = 1 - (1 - 1/365) ** student_num
    return f"{prob:.2f}"

sums = 0
for sim in range(100):
    sums += simulate(problem_1_simulate, students, runs)
print(f"{sums / 100:.2f}")
print(problem_1_analytic(students))


# problem 2
# same as p1, but birhday is take from a person in the room,
# instead of being predefined.

def problem_2_simulate(student_num):
    birthdays = [random.randint(1, 365) for _ in range(student_num)]
    random_birthday = random.randint(0, len(birthdays)-1)
    birthday = birthdays[random_birthday]
    birthdays.remove(birthday)
    return birthday in birthdays

def problem_2_analytic(student_num):
    prob = 1 - (1 - 1/365) ** (student_num - 1)
    return f"{prob:.2f}"

sums = 0
for sim in range(100):
    sums += simulate(problem_2_simulate, students, runs)
print(f"{sums / 100:.2f}")
print(problem_2_analytic(students))