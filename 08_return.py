# Clase 12 Funciones: return

def sum_with_range(min, max):
    print('min = ', min, 'max = ', max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum
    
# 1,2,3,4,5,6,7,8,9 = 45

print('sum_with_range(1,10) = ', sum_with_range(1,10))
result =  sum_with_range(20,30)
print('result = ', result)
result_2 =  sum_with_range(result, result + 10)
print('result_2 = ',result_2)



