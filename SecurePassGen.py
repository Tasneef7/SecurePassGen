import random
import string
import datetime

def generate_random_password(length=10):
    # Define sets of characters for each category
    capital_letter = random.choice(string.ascii_uppercase)
    small_letter = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special_character = random.choice(string.punctuation)
    
    # Combine characters from each category with random characters
    characters = capital_letter + small_letter + digit + special_character
    characters += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - 4))
    
    # Shuffle the characters to randomize their order
    password_list = list(characters)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def save_password_to_file(service, username, password):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('passwords.txt', 'a') as file:
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Service: {service}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n\n")

def main():
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password_length = int(input("Enter the desired password length (default: 10): ") or 10)

    password = generate_random_password(password_length)

    print(f"Generated Password: {password}")

    save_password_to_file(service, username, password)
    print("Service, Username, and Password saved to 'passwords.txt'")

if __name__ == "__main__":
    main()