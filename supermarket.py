# ==========================================
#       SUPER MARKET BILLING SYSTEM
# ==========================================

from datetime import datetime

print("=" * 50)
print("      WELCOME TO SUPER MARKET")
print("=" * 50)

# Customer Details
customer_name = input("Enter Customer Name : ")

# Current Date and Time
current_time = datetime.now()
date = current_time.strftime("%d-%m-%Y")
time = current_time.strftime("%H:%M:%S")

print("\nDate :", date)
print("Time :", time)
print("-" * 50)

# Variables
cart = []
subtotal = 0

# Item Entry Loop
while True:

    item = input("\nEnter Item Name : ")
    quantity = int(input("Enter Quantity : "))
    price = float(input("Enter Price per Item : "))

    total = quantity * price

    cart.append([item, quantity, price, total])

    subtotal += total

    choice = input("Add another item? (yes/no): ")

    if choice.lower() == "no":
        break

# Discount Calculation
if subtotal > 5000:
    discount = subtotal * 0.20
elif subtotal > 3000:
    discount = subtotal * 0.10
elif subtotal > 1000:
    discount = subtotal * 0.05
else:
    discount = 0

amount_after_discount = subtotal - discount

# GST Calculation (18%)
gst = amount_after_discount * 0.18

# Final Amount
final_amount = amount_after_discount + gst

# ==========================================
#              FINAL BILL
# ==========================================

print("\n")
print("=" * 60)
print("             SUPER MARKET BILL")
print("=" * 60)

print(f"Customer Name : {customer_name}")
print(f"Date          : {date}")
print(f"Time          : {time}")

print("-" * 60)
print("Item\t\tQty\tPrice\tTotal")
print("-" * 60)

for data in cart:
    print(f"{data[0]}\t\t{data[1]}\t{data[2]}\t{data[3]}")

print("-" * 60)
print(f"Subtotal           : ₹ {subtotal:.2f}")
print(f"Discount           : ₹ {discount:.2f}")
print(f"GST (18%)          : ₹ {gst:.2f}")
print("-" * 60)
print(f"Final Amount       : ₹ {final_amount:.2f}")
print("=" * 60)

print("\nThank you for shopping with us!")
print("Visit Again 😊")
input("\nPress Enter to exit...")