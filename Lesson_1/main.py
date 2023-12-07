print("Виберіть операцію.")
print("1.Додати")
print("2.Відняти")
print("3.Помножити")
print("4.Розділити")

while True:
    # беремо вхідні дані від користувача
    choice = input("Введіть вибір (1/2/3/4): ")

    # перевіряємо, чи є вибір одним з чотирьох варіантів
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Неправильний ввід. Будь ласка, введіть число.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", num1 + num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1 * num2)

        elif choice == '4':
            print(num1, "/", num2, "=", num1 / num2)
        
        # перевіряємо, чи користувач хоче ще один розрахунок
        # вихід з циклу while, якщо відповідь - ні
        next_calculation = input("Давайте зробимо наступний розрахунок? (так/ні): ")
        if next_calculation == "ні":
          break
    else:
        print("Неправильний ввід")