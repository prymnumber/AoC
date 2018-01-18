from datetime import date , timedelta
import pdb

peeps = ['ann','bob','dan','joe','kay']
ages = [20,30,40,50,60]

for i in range(len(peeps)):
    print(peeps[i], ages[i])

x = zip(peeps,ages)

print(i)

class tooCheap(Exception):
    pass

today = date.today()
tomorrow = today+timedelta(days=1)
item1 = {'prod':'apple','exp_date':today,'price':100}
item2 = {'prod':'pear','exp_date':today,'price':40}
item3 = {'prod':'bananna','exp_date':tomorrow,'price':500}
item4 = {'prod':'momo','exp_date':tomorrow,'price':20}

basket = [item1,item2,item3,item4]
pdb.set_trace()

try:
    print('in try block')
    for item in basket:
        if item['exp_date'] == today:
            item['price'] *= 0.8
            print('price of ',item['prod'],'is now',item['price'])
        if item['price']<30:
            raise tooCheap('too cheap!')

except tooCheap:
    print('tooCheap')
    #None
else:
    print('else')
finally:
    print('finally')

for item in basket:
    print(item)
