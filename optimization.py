import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximizing_products", pulp.LpMaximize)

# Змінні для кількості вироблених одиниць
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')  # Кількість "Лимонаду"
juice = pulp.LpVariable('juice', lowBound=0, cat='Integer')  # Кількість "Фруктового соку"

# Функція мети: максимізація загальної кількості вироблених продуктів
objective = lemonade + juice

# Додавання мети до моделі
model += objective

# Обмеження на ресурси:
# 1. Вода: 2 од. для лимонаду та 1 од. для фруктового соку, загалом не більше 100 од.
model += 2 * lemonade + juice <= 100, "Water_Constraint"

# 2. Цукор: 1 од. для лимонаду, загалом не більше 50 од.
model += lemonade <= 50, "Sugar_Constraint"

# 3. Лимонний сік: 1 од. для лимонаду, загалом не більше 30 од.
model += lemonade <= 30, "Lemon_Juice_Constraint"

# 4. Фруктове пюре: 2 од. для фруктового соку, загалом не більше 40 од.
model += 2 * juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Отримання оптимальних значень змінних
print(f"Оптимальна кількість 'Лимонаду': {pulp.value(lemonade)}")
print(f"Оптимальна кількість 'Фруктового соку': {pulp.value(juice)}")

# Отримання максимальної кількості продуктів
print(f"Максимальна загальна кількість продуктів: {pulp.value(model.objective)}")
