def calculate_calories(minutes):
    return minutes * 4.9

def program():
    print("Calorie calculation")
    print("-----------------------")
    time = input("Enter running time in minutes: ")

    while not time.isdigit() or int(time) <= 5:
        print("Time must be greater than 5 minutes.")
        time = input("Enter running time in minutes: ")

    time = int(time)

    minutes = 5
    print("Calorie calculation")
    print("-----------")
    while minutes <= time:
        calories = calculate_calories(minutes)
        print(f"Minutes: {minutes:.1f} burns {calories:.1f} calories")
        minutes += 5
    print("-----------")

choice = 'y'
while choice == 'y':
    program()
    choice = input("Again y/n? ").lower()
    if choice != 'y':
        print("done")
