#Словари
my_dict = {'John' : 142, 'Troy' : 153, 'Richard' : 134}
print(my_dict)
print(my_dict['John'])
print(my_dict.get('Harold'))
a = my_dict.pop('Troy')
print(a)
my_dict.update({'Doris' : 112, 'Harold' : 138})
print(my_dict)

#Множества
my_set = {True, 62, 34, 62, (10, 53, 74), 60, 'Troy'}
print(my_set)
my_set.add(34)
my_set.add('Harold')
my_set.discard((10, 53, 74))
print(my_set)
