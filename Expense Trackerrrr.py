print(" « Expense Tracker » ".center(100,'•')) 
while True:
    print("\nSelect Operation - ")
    print("\n1.Add Expenses") 
    print("2.View Expenses") 
    print("3.View by category") 
    print("4.Total of same category") 
    print("5.Exit\n")
    op = int(input("Enter your choice: "))

    if op == 1:
        f = open("data1.txt", 'a')
        count = int(input("Enter the number of expenses to add: "))
        for i in range(count):
            print("\n‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣ Add Expenses ‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣‣")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            date = input("Enter date: ")
            f.writelines(f"{category},{amount},{description},{date}\n")
            print("\nExpenses added Successfuly!!")
        f.close()
        print("«»".center(100,'—'))

    elif op == 2:
        print("‣ Your Expenses ‣".center(70, "-"))
        f = open("data1.txt", 'r')
        res = f.readlines()
        if not res:
            print("No expenses recorded yet.")
        else:
            print("Category".rjust(10), end=" | ")
            print("Amount".rjust(10), end=" | ")
            print("Description".rjust(20), end=" | ")
            print("Date".rjust(10), end="")
            print()
            total=0
            for line in res:
                r = line.strip().split(",")
                print(r[0].rjust(10), end=" | ")
                print(r[1].rjust(10), end=" | ")
                print(r[2].rjust(20), end=" | ")
                print(r[3].rjust(10), end="")
                print()
                total=total+int(r[1])
            print(f"Total : {total}".rjust(23))
               
        f.close()
        print("«»".center(100,'—'))
    elif op == 3:
        same = input("Enter category to view expenses: ")
        print(f"‣ Expenses in Category: {same} ‣".center(80, "‣"))
        f = open("data1.txt", 'r')
        res = f.readlines()
        for line in res:
            r = line.strip().split(",")
            if r[0] == same:
                print("Category : ", r[0])
                print("Amount : ", r[1])
                print("Description : ", r[2])
                print("Date : ", r[3])
        f.close()
        print("«»".center(100,'—'))
    
    elif op == 4:
        same = input("Enter category: ")
        print(f"‣ Expenses in Category: {same} ‣".center(80, "‣"))
        f = open("data1.txt", 'r')
        res = f.readlines()
        total=0
        for line in res:
            r = line.strip().split(",")
            if r[0] == same:
                total=total+int(r[1])
        print(f"\nTotal Expense by {same} is {total}, Thank You!")
        f.close()
        print("«»".center(100,'—'))

    elif op == 5:
        print("Exiting The Expense Tracker...Thankkk Youuu!")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")
        
