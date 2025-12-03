battery_list = []

with open("input_day3.txt") as f:
    battery_list= [line.rstrip("\n") for line in f.readlines()]

for bat in battery_list:
    print(bat)