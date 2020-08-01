from sys import argv

sript, input_file = argv

# fuel calculator based on example
def fuel_calc(mass):
    return int((mass / 3)) - 2


def fuel_fuel_calc(fuel):
    # print(fuel)
    if int(fuel/3) - 2 <= 0:
        return fuel
    return fuel + fuel_fuel_calc(int(fuel/3) - 2)

print(fuel_fuel_calc(33583))
total_fuel = 0

open_file = open(input_file)
content = open_file.readlines()

for line in content:
    total_fuel += fuel_fuel_calc(fuel_calc(int(line)))


print(f"total fuel: {total_fuel}")
open_file.close()
