id_cards = []


# Function to create an ID card
def create_id_card():
    ID = input("Enter ID: ")
    name = input("Enter Name: ")
    sex = input("Enter Sex: ")
    dob = input("Enter Date of Birth (DOB): ")
    pob = input("Enter Place of Birth (POB): ")
    address = input("Enter Address: ")
    creation_date = input("Enter Creation Date: ")
    expire_date = input("Enter Expiration Date: ")

    card = (ID, name, sex, dob, pob, address, creation_date, expire_date)
    id_cards.append(card)
    print("ID Card Created Successfully!\n")


# Function to display all ID cards
def check_id_cards():
    if not id_cards:
        print("No ID cards found.\n")
        return
    for card in id_cards:
        print("ID:", card[0])
        print("Name:", card[1])
        print("Sex:", card[2])
        print("DOB:", card[3])
        print("POB:", card[4])
        print("Address:", card[5])
        print("Creation Date:", card[6])
        print("Expire Date:", card[7])
        print("-----------------------\n")


# Function to update an ID card
def update_id_card():
    ID = input("Enter ID to update: ")
    for i, card in enumerate(id_cards):
        if card[0] == ID:
            print("Updating ID:", ID)
            name = input("Enter New Name (or press Enter to keep current): ") or card[1]
            sex = input("Enter New Sex (or press Enter to keep current): ") or card[2]
            dob = input("Enter New DOB (or press Enter to keep current): ") or card[3]
            pob = input("Enter New POB (or press Enter to keep current): ") or card[4]
            address = input("Enter New Address (or press Enter to keep current): ") or card[5]
            creation_date = card[6]  # Can't change creation date
            expire_date = input("Enter New Expiration Date (or press Enter to keep current): ") or card[7]

            updated_card = (ID, name, sex, dob, pob, address, creation_date, expire_date)
            id_cards[i] = updated_card
            print("ID Card Updated Successfully!\n")
            return
    print("ID not found.\n")


# Function to delete an ID card
def delete_id_card():
    ID = input("Enter ID to delete: ")
    for i, card in enumerate(id_cards):
        if card[0] == ID:
            id_cards.pop(i)
            print("ID Card Deleted Successfully!\n")
            return
    print("ID not found.\n")


# Main menu loop
while True:
    print("1. Create ID Card")
    print("2. Check ID Cards")
    print("3. Update ID Card")
    print("4. Delete ID Card")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_id_card()
    elif choice == '2':
        check_id_cards()
    elif choice == '3':
        update_id_card()
    elif choice == '4':
        delete_id_card()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
