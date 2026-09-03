contacts = {}

while True:
    print("\n1.Add  2.Search  3.Update  4.Delete  5.Display  6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact added")

    elif ch == 2:
        name = input("Name: ")
        print(contacts.get(name, "Contact not found"))

    elif ch == 3:
        name = input("Name: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
            print("Updated")
        else:
            print("Contact not found")

    elif ch == 4:
        name = input("Name: ")
        if name in contacts:
            del contacts[name]
            print("Deleted")
        else:
            print("Contact not found")

    elif ch == 5:
        print(contacts)

    elif ch == 6:
        break
