price = 100 # global

def increment():
    price = 200 # local
    price = price + 10
    #result = price + 10
    print('price increment() => ', price)
    return price
    #return result


print('price global => ', price)
price_2 = increment()
print('price_2 => ',price_2)
#print(result)
