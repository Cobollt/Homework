import os
import sys
from os import name


def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1

        average = total / count if count != 0 else 0
        return  total, average

    except FileNotFoundError:
        print("File not found")
        return 0,0
    except ValueError:
        print("Value error")
        return 0,0

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")