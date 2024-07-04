my_dict = {'Max': 1995, 'John': 1999, 'Anne': 2000}
print('Dict:', my_dict)
print('Existing value:', my_dict['Max'])
print('Not existing value:', my_dict.get('Ferb'))
my_dict.update({'Phineas': 2001,
                'Mersedes': 2002})
print('Deleted value:', my_dict.pop('Anne'))
print('Modified dictionary:', my_dict)
print()
my_set = {1, 1, '2', '2', (1, 2, 3), (1, 2, 3)}
print('Set:', my_set)
my_set.add(5)
my_set.add(6)
my_set.remove(1)
print('Modified set:', my_set)
