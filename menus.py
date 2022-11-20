name = input("Enter name: ").upper()
menu = "(H)ello\n(G)oodbye\n(Q)uit"
word = 0
print(menu)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print(f"Invalid choice")
    print(menu)
    choice = input(">>> ").upper()

print("Finished")