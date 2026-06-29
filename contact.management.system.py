contacts={}
while True:
    print("\n1.Add contact")
    print("2.Search Contact")
    print("3.Delete Contact")
    print("4.Show All Contacts")
    print("5.Exit")
    choice = input("Enter your choice:")
    if choice=="1":
        name=input("Enter Name:")
        number=input("Enter phone number:")
        contacts[name]=number
        print("Contact added successfully.")
    elif choice=="2":
        name=input("Enter name to search:")
        if name in contacts:
            print("Phone Number:",contacts[name])
        else:
            print("Contact not found.")
    elif choice=="3":
        name=input("Enter name to delete:")
        if name in contacts:
            del contacts[name]
            print("Contact delete successfully:")
        else:
            print("Contact not found.")
    elif choice=="4":
        if contacts:
            for name,number in contacts.items():
                print(name,":",number)
        else:
            print("No Contact available.")
    elif choice=="5":
        print("Exiting Contact Book.")
        break
    else:
        print("invalid choice.")
