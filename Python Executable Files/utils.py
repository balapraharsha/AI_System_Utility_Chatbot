def print_error(error):
    print(f"[ERROR] {error}")

def confirm_action(message):
    choice = input(f"{message} (y/n): ").lower()
    return choice == 'y'
