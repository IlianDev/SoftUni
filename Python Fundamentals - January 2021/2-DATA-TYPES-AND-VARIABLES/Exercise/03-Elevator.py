import math

n_persons = int(input())
p_capacity = int(input())

courses_to_make = math.ceil(n_persons/p_capacity)
print(courses_to_make)
