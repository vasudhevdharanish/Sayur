import datetime
def calculate_fee(entry_time, exit_time):

  total_minutes = int((exit_time - entry_time).total_seconds() / 60)
  free_minutes = 15
  parking_fee = 0

  if total_minutes <= free_minutes:
    return 0  # Free parking for 15 minutes

  parking_fee += 100  # Fee for 1st the hr

  # Calculating  remaining minutes after the first hour
  remaining_minutes = total_minutes - free_minutes - 60
  # Rounding up to the approx 30 minute
  hours_after_first = (remaining_minutes + 29) // 30
  parking_fee += hours_after_first * 150

  return parking_fee

def main():
  total_fee = 0
  current_time = datetime.datetime.now()
  parking_lot = [True for _ in range(10)]  # Initializing all lots as available

  while True:
    choice = input("Enter 1 (Park), 2 (Exit), or 3 (Exit Program): ")

    if choice == "1":  # Park car
      if not any(parking_lot):  # Checking if any lot is available
        print("Sorry, parking lot is full!")
        continue
      available_lot = parking_lot.index(True)
      parking_lot[available_lot] = False
      entry_time = datetime.datetime.now()
      print(f"Your car is parked in lot {available_lot + 1}.")

    elif choice == "2":  # Exit car
      lot_number = int(input("Enter the lot number of your car: ")) - 1
      if not 0 <= lot_number < 10 or parking_lot[lot_number]:
        print("Invalid lot number!")
        continue
      exit_time = datetime.datetime.now()
      parking_lot[lot_number] = True
      fee = calculate_fee(entry_time, exit_time)
      print(f"Your parking fee is Rs.{fee}.")
      total_fee += fee

    elif choice == "3":  # Exit program
      if (datetime.datetime.now() - current_time).total_seconds() / 3600 > 24:
        print("Program running for more than 24 hours.Hence.Exit")
      print(f"Total fees collected today: Rs.{total_fee}")
      break

    else:
      print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
  main()
 