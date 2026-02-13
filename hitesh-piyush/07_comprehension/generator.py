# its a memory efficiency thingy

daily_sales = [5,10,12,20,7,8,9,3,5,8,3]
total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
