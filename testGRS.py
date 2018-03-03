from grs import Stock

stock = Stock('2454') #get the price for Stock number 2618
print stock.moving_average(5) 
print stock.moving_average_value(5)
print stock.moving_average_bias_ratio(5, 10)

stock = Stock('2454', 12)

stock.out_putfile('2454.csv')