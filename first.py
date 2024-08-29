from setuptools.command.develop import develop

print('hello')
print('hii')
print('first line /t second line')


m1=23
m2=23
m3=11

#calculator
print("addition",m1+m2+m3)
print("sustraction",m1-m2)
print("mul",m1*m2)
print("division",m1/m2)
print((m1+m2+m3)/3)

#split te bill program
total=128
n=5

share=total/n


print("bill split is",share)
tip_percent= 0.15
tip_amount= total+tip_percent

print("bill split is",share)

days=45
weeks=days//7
rem=days%7
print(f"{days}")

#road trip program
total_budget=1500
gas_cost=600
food_cost=300
accomodation_cost=200
souver=25




print(gas_cost+food_cost+accomodation_cost)
print(f"you can buy {souver}")

#remainder operation in python
print(10**2)

volume=4
print("vol of cube is",volume **3)

basic_tier_price=9.99
pro_tier_price=19.99
basic_tier_users=1000
pro_tier_users=500

server_cost=1000
support_cost=5000
misc_cost=2000

name=input("prt name")
pet_age=int(input('enter age'))
pet_species=input('enter pet species')

print(f"pet name is {name}, age is {pet_age}, species is  {pet_species}")

num1=int(input('enter num1'))
num2=int(input('enter num2'))
op=input('enter operation')

if op == '+':
    result=num1+num2
elif op== '-':
    result=num1-num2
elif op=='/':
    result=num1/num2
elif op=='*':
    result=num1*num2
else:
    result='invalid'

print(result)



