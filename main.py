
#storing tickets in list 
tickets = []
ticket_counter = 1000

#creating a new tickets
def create_ticket():
    global ticket_counter
    ticket_counter += 1
    ticket_id = f'INC{ticket_counter}'
    print("Creating a new Ticket")
    ticket = {
            "id" : ticket_id,
            "title" : input("Enter Ticket Title: "),
            "description" :  input("Enter Descriptipon: "),
            "priority" : input("Enter priority :"),
            "status" : "Open" 
            }
    tickets.append(ticket)

    print("\n Ticket Created Successfully!")
    print(f'Ticket ID : {ticket_id}')

#dispalying all tickets 
def display_tickets():
    if not tickets:
        print("No tickets available.")
        return

    print("\n ===== All Tickets ==== ")

    for ticket in tickets:
        print(f"ID       : {ticket['id']}")
        print(f"Title    : {ticket['title']}")
        print(f"Priority : {ticket['priority']}")
        print(f"Status   : {ticket['status']}")
        print('\n')

def searching_tickets():
    if not tickets:
        print("No tickets available.")
        return

    search_id = input("Enter Tikcet Id :")

    for ticket in tickets:
        if ticket["id"] == search_id:
            print("\n===== Ticket Found =====")
            print(f"ID          : {ticket['id']}")
            print(f"Title       : {ticket['title']}")
            print(f"Description : {ticket['description']}")
            print(f"Priority    : {ticket['priority']}")
            print(f"Status      : {ticket['status']}")
            return
    print("Tikcet not found ")
        

while True:

    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Search Ticket")
    print("4. Exit")  

    choice = input("Enter your choice: ")


    if choice == "1":
        create_ticket()
    elif choice == "2":
        display_tickets()
    elif choice == "3":
        searching_tickets()
    elif choice =="4":
        print("Exiting application?")
        break
    else:
        print("Invalid choice")

#print(f"You selected option {choice}")