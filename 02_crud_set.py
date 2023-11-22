set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print('set_countries => ', set_countries)
# se intenta agregar nuevamente pero los conjuntos no permiten duplicidad
set_countries.add('pe')
print('set_countries. Impide duplicidad => ',set_countries)

# update
set_countries.update({'ar','ecua','pe'})
print(set_countries)

# remove
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

# Cuando el elemento no existe Python da error:
# set_countries.remove('arg')
# Con discard no da error a pesar de que no exista:
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')

# Limpia todo el conjunto sin dejar ningún elemento
set_countries.clear()
print(set_countries)
print(len(set_countries))









