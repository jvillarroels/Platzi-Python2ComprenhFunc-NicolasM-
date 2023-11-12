set_a = {'col','mex','bol'}
set_b = {'pe','bol'}

# Unión de 2 conjuntos
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# Intersección de 2 conjuntos
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# Diferencias entre conjuntos
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# Diferencia simpetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)
