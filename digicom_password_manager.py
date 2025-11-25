import os  # library module for file checks

# Global variable for the credentials file
FILE_NAME = "digicore_credentials.txt"


def encrypt(text):
    #Return text encoded with a simple ROT3 cipher.
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + 3)
    return encrypted


def decrypt(encoded):
    #Return text decoded from the simple ROT3 cipher.
    decrypted = ""
    for char in encoded:
        decrypted += chr(ord(char) - 3)
    return decrypted


def ensure_storage_file():
    #Create the credentials file if it does not already exist.
    if not os.path.exists(FILE_NAME):
        # Create an empty file
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.write("")


def display_menu():
    #Print the main menu.
    print(r" ____  _       _  ____")
    print(r"|  _ \(_) __ _(_)/ ___|___  _ __ ___")
    print(r"| | | | |/ _` | | |   / _ \| '_ ` _ \ ")
    print(r"| |_| | | (_| | | |__| (_) | | | | | |")
    print(r"|____/|_|\__, |_|\____\___/|_| |_| |_|")
    print(r"         |___/ ")
    print("\n----------------------------------------")
    print("        DigiCom Password Manager        ")
    print("----------------------------------------")
    print("[1] Add new credentials")
    print("[2] Retrieve credentials for a site")
    print("[3] List all stored entries")
    print("[4] Quit")
    print("----------------------------------------")


def add_credentials():
    #Ask the user for new credentials and append them to the file.
    ensure_storage_file()

    site = input("Please enter site / company / resource name: ")
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    # Encrypt each field before writing
    enc_site = encrypt(site)
    enc_username = encrypt(username)
    enc_password = encrypt(password)

    # Append to the file so previous entries are not overwritten
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{enc_site}|{enc_username}|{enc_password}\n")

    print(f"\nCredentials for '{site}' saved.\n")


def retrieve_credentials():
    #Retrieve credentials for a single site / resource.
    ensure_storage_file()

    search_site = input("Enter the site / company name to retrieve: ")
    found = False

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip blank lines

            enc_site, enc_username, enc_password = line.split("|")

            site = decrypt(enc_site)
            username = decrypt(enc_username)
            password = decrypt(enc_password)

            # Case-insensitive comparison
            if site.lower() == search_site.lower():
                print("\nStored credentials:")
                print(f"Site / Resource : {site}")
                print(f"Username        : {username}")
                print(f"Password        : {password}\n")
                found = True
                break

    if not found:
        print("\nNo credentials found for that site.\n")


def list_all_credentials():
    #Display all stored credentials in a presentable way.
    ensure_storage_file()

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("\nNo entries stored yet.\n")
        return

    print("\n------- Stored Credentials -------\n")

    # Use a data structure (list of lines) and string manipulation
    for index, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue

        enc_site, enc_username, enc_password = line.split("|")
        site = decrypt(enc_site)
        username = decrypt(enc_username)
        password = decrypt(enc_password)

        print(f"Entry {index}")
        print(f"Site / Resource : {site}")
        print(f"Username        : {username}")
        print(f"Password        : {password}\n")


def main():
    #Main program loop.
    ensure_storage_file()

    while True:
        display_menu()
        choice = input("Please choose an option -> ").strip()

        if choice == "1":
            add_credentials()
        elif choice == "2":
            retrieve_credentials()
        elif choice == "3":
            list_all_credentials()
        elif choice == "4":
            print("\nExiting program... Goodbye!")
            break
        else:
            print("\nInvalid option, please try again.\n")


# Run the program
if __name__ == "__main__":
    main()
