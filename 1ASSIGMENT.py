# Calorie Tracker Program 
#Piyush

food_log = []
exercise_log = []

while True:
    print("\n--- Calorie Tracker Menu ---")
    print("1. Add Food Item")
    print("2. Add Exercise")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        food = input("Enter food item: ")
        calories = float(input(f"Enter calories for {food}: "))
        food_log.append(calories)
        print(f"✅ Added {calories} calories from {food}.")

    elif choice == "2":
        activity = input("Enter exercise activity: ")
        calories = float(input(f"Enter calories burned for {activity}: "))
        exercise_log.append(calories)
        print(f"🔥 Recorded {calories} calories burned for {activity}.")

    elif choice == "3":
        total_food = sum(food_log)
        total_exercise = sum(exercise_log)
        net_calories = total_food - total_exercise

        print("\n===== Calorie Summary =====")
        print("Total Calories Consumed :", total_food)
        print("Total Calories Burned   :", total_exercise)
        print("Net Calories (Balance)  :", net_calories)

        if net_calories > 0:
            print("⚠️  You consumed more than you burned!")
        elif net_calories < 0:
            print("💪 You burned more than you consumed!")
        else:
            print("😎 Perfect balance today!")

    elif choice == "4":
        print("👋 Exiting Calorie Tracker. Stay healthy!")
        break

    else:
        print("❌ Invalid choice. Try again.")