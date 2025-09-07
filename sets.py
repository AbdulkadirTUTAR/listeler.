fruits = {'orange', 'Apple', 'banana'}

#print(fruits[0]) indekslenemez

for x in fruits:
    print(x)
    
fruits.add('cherry')
print(fruits)

my_list = [1,2,2,4,5,5,6]
print(set(my_list))
print(my_list)
fruits.remove('Apple')
fruits.pop()
print(fruits)
