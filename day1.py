from sys import argv

sript, input_file = argv

# fuel calculator based on example
def fuel_calc(mass):
    return int((mass / 3)) - 2

total_fuel = int()

open_file = open(input_file)
content = open_file.readlines()

for line in content:
    total_fuel += fuel_calc(int(line))

print(f"total fuel: {total_fuel}")
open_file.close()
