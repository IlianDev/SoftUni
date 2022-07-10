RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

effort = 0
put_out_fire = []

fire_data = input().split("#")
water_amount = int(input())

for fire in fire_data:
    type_of_fire, value = fire.split(" = ")
    value = int(value)

    if type_of_fire == "High" and value not in RANGE_HIGH:
        continue
    elif type_of_fire == "Medium" and value not in RANGE_MEDIUM:
        continue
    elif type_of_fire == "Low" and value not in RANGE_LOW:
        continue

    # TODO chek if water is enough
    if water_amount >= value:
        water_amount -= value
        effort += value * 0.25
        put_out_fire.append(value)

print("Cells:")
for fire_value in put_out_fire:
    print(f" - {fire_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_fire)}")


"""
<I>
Expected input: 
High = 89#Low = 28#Medium = 77#Low = 23
1250

output:
Cells:
 - 89
 - 28
 - 77
 - 23
Effort: 54.25
Total Fire: 217

<II>
expected input:
High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
220

output:
Cells:
 - 40
 - 110
Effort: 37.50
Total Fire: 150

"""