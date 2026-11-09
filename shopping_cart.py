name=input("Enter Customer Name: ")
p1,pr1 =input("Product 1 name: "), int(input("Product 1 price: "))
p2,pr2 =input("Product 2 name: "), int(input("Product 2 price: "))
p3,pr3 =input("Product 3 name: "), int(input("Product 3 price: "))
tot=pr1+pr2+pr3
if tot >= 5000: rate = 0.20
elif tot >= 3000: rate = 0.10
elif tot >= 1000: rate = 0.05
else: rate = 0.0
disc=int(tot*rate)
Ftot = tot-disc
print(f"""
Customer Name: {name}
Product 1: {p1}
Price: {pr1}
Product 2: {p2}
Price: {pr2}
Product 3: {p3}
Price: {pr3}
Subtotal: {tot}
Discount: {disc}
Final Total: {Ftot}""")