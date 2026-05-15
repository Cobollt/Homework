from Homework_10 import Record
from Homework_10 import AddressBook
from datetime import datetime, timedelta


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return "Give me name and phone please."
            if func.__name__ == "change_contact":
                return "Invalid Name."
        except KeyError as e:
            return "No contact."
        except IndexError as e:
            return "Enter a name."
    return inner

@input_error
def add_contact(args, book ):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message
@input_error
def change_contact(args, book,):
    name, old_number, new_numbers = args
    record = book.find(name)
    if record is None:
        return "No contact."
    record.edit_phone(old_number, new_numbers)
    return "Contact changed."
@input_error
def show_phones(args, book):
    name = args[0]
    return book.find(name)
@input_error
def show_all(book):
    for record in book.data.values():
        print(record)

def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday)
    return "Birthday added."

def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        return "No contact."
    if record.birthday is None:
        return "Birthday not found."
    return record.birthday.value

def all_birthdays(book):
    today = datetime.today().date()
    next_weak = today + timedelta(days=7)
    result = []
    for record in book.data.values():
        if record.birthday is not None:
            birthday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
            birthday_this_year = birthday.replace(year=today.year)
            if today <= birthday_this_year <= next_weak:
                result.append(f"{record.name.value}: {record.birthday.value}.")
    return "\n".join(result)



def main():
    book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        if not  user_input.strip():
            print("Please enter a command.")
            continue

        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phones(args, book))
        elif command == "all":
            show_all(book)
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday( args, book))
        elif command == "birthdays":
            print(all_birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()