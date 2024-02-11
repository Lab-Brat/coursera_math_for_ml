import random

def simulate(pfunc, student_num, runs):
    matches = len([run for run in range(runs) if pfunc(student_num)])
    return matches / runs

# problem 1
# given a pre-defined date, 
# what is the value of n such that the probability of having 
# a match is greater than or equal to 0.5?

def problem_1(student_num):
    birthday = random.randint(1, 365)
    birthdays = [random.randint(1, 365) for _ in range(student_num)]
    return birthday in birthdays


students = 255
runs = 100
sums = 0
for sim in range(100):
    sums += simulate(problem_1, students, runs)
print(sums / 100)
