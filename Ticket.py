import datetime

name = input("Enter your name: ")
birthday = input("Enter your birthday (DD/MM/YYYY): ")
day, month, year = map(int, birthday.split('/'))
birth_date = datetime.date(year, month, day)
today = datetime.date.today()
age = today.year - birth_date.year
if age <= 12 or age >= 60:
    ticket_price = 50
else:
    ticket_price = 75
total_cost = ticket_price
if today.weekday() == 1 or today.weekday() == 3:
    total_cost *= 0.8

print("\nTicket Details:")
print("Name: ", name)
print("Age: ", age)
print("Ticket Price: Rs.", ticket_price)
print("Total Cost: Rs.", total_cost)
