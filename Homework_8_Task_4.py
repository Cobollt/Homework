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
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."
@input_error
def show_phones(args, contacts):
    name = args[0]
    return contacts[name]
@input_error
def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phones(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
