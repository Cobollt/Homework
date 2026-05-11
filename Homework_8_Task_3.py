import sys


LOG_LEVELS = ["INFO", "DEBUG", "ERROR", "WARNING"]


def parse_log_line(line: str) -> dict:
    date, time, level, message = line.strip().split(" ", 3)

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def load_logs(file_path: str) -> list:
    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    logs.append(parse_log_line(line))

    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)

    except Exception as error:
        print(f"Помилка при читанні файлу: {error}")
        sys.exit(1)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    counts = {level: 0 for level in LOG_LEVELS}

    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1

    return counts


def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 31)

    for level in LOG_LEVELS:
        print(f"{level:<17} | {counts[level]:<10}")


def display_logs(logs: list):
    for log in logs:
        print(f"{log['date']} {log['time']} {log['level']} {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nДеталі логів для рівня '{level}':")
        display_logs(filtered_logs)


if __name__ == "__main__":
    main()