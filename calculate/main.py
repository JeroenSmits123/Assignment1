# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
items = {"broccoli": 2,"leek":2,"potato": 3, "spruit":7} 
sum_one_each=sum(items.values())
avg_price = sum(items.values())/len(items)

amount = [5,2,7,10]
price = []
for x in range(0,len(items)):
    price.append(list(items.values())[x] * amount[x])

sum_total = sum(price)
discount_percentage = 0.3
discounted_sum_total = round(sum_total*(1-discount_percentage),2)
print(discounted_sum_total)