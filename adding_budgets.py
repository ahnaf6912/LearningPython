def adding_budgets():
    total = 0
    budgets = [{"name": "john", "age": 21, "budget": 2300},
               {"name": "john", "age": 21, "budget": 2300},
               {"name": "john", "age": 21, "budget": 2300}]
    for item in budgets:
        total = total + item["budget"]
    print(total)

adding_budgets()