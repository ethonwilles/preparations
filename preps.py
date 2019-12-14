import math
from functools import reduce

guy = 3200*365
girl = 2400* 365

total = (guy * 3) + (girl * 2)

items = []

egg = 90
amt_of_chickens = 5
cal_per_day_chickens = (amt_of_chickens * egg) * 365
items.append(cal_per_day_chickens)


potato = 163
amt_of_potato_plants = 7
cal_total_for_potatoes = amt_of_potato_plants * (potato * 7)
amt_of_calo_for_potatoes_in_a_year = math.floor(cal_total_for_potatoes / 120) * 365
items.append(amt_of_calo_for_potatoes_in_a_year)

corn = 125
amt_of_corn_plants = 50
cal_total_corn = amt_of_corn_plants * (corn * 2)
amt_of_cal_per_corn_per_year = math.floor(cal_total_corn / 100) * 365
items.append(amt_of_cal_per_corn_per_year)

beans = 17 / 10
amt_of_bean_plants = 50
cal_total_beans = amt_of_bean_plants * (math.floor(beans * 120))
amt_of_cal_per_bean_per_year = math.floor(cal_total_beans / 55) * 365
items.append(amt_of_cal_per_bean_per_year)



print(f"Current Calculated Calories: {reduce(lambda elem, total: elem + total, items)}, Remaining Calories: {total - reduce(lambda elem, total: elem + total, items)}")
print(f"Current Calculated Calories: {reduce(lambda elem, total: elem + total, items)}, Remaining Calories for One Man: {guy - reduce(lambda elem, total: elem + total, items)}")


