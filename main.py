#create - view all - search by id  - update by id - delted 

#storing tickets in list 
tickets = []
ticket_counter = 1000

#creating a new tickets
def create_ticket():
    global ticket_counter
    
    print("Creating a new Ticket")

    title = input("Enter Ticket Title : ").strip()
    if not title:
        print("ticket title can't be empty!")
        return
    
    description = input("Enter Description : ").strip()
    if not description:
        print("Description can't be empty.")
    
    #validate priority 
    priority = input("Enter Priority (Low/Medium/High : ").strip().lower()

    if priority not in ["low" , "medium" , "high"]:
        print("Invalid Priority. Please enter High , Medium or Low.")
        return
    priority = priority.capitalize()

    ticket_counter += 1
    ticket_id = f'INC{ticket_counter}'


    ticket = {
            "id" : ticket_id,
            "title" : title,
            "description" : description,
            "priority" : priority,
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

#searching ticket through id 
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

#update status 
def update_ticket_status():
    if not tickets:
        print("No Tickets Available.")
        return 
    search_id = input("Enter ticket ID: ")

    for ticket in tickets:
        if ticket["id"] == search_id:
            print("\n Current Status:" , ticket['status'])

            new_status = input("Update status (In Progress / Resolved / Closed): ").lower()

            if new_status not in ["in progress" , "resolved" , "closed"]:
                print("Invalid Stage.")
                return
            new_status = new_status.capitalize()

            ticket['status'] = new_status

            print("Ticket Status Successfully Updated!") 
            return

    print("Ticket not found..")     

#deleting ticket by id 
def delete_ticket():
    if not  tickets:
        print("No tickets are available")
        return

    delete_id = input("Enter Ticket Id to be deleted : ")

    for ticket in tickets:
        if ticket["id"] == delete_id:
            tickets.remove(ticket)
            print("Successfully Deleted!")
            return
    print("ticket not founded.")



while True:

    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Search Ticket")
    print("4. Update Ticket Status")
    print("5. Delete Tikcet")
    print("6. Exit")  

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please choice a valid number.")
        continue

    if choice == 1:
        create_ticket()
    elif choice == 2:
        display_tickets()
    elif choice == 3:
        searching_tickets()
    elif choice == 4:
        update_ticket_status()
    elif choice == 5:
        delete_ticket()
    elif choice == 6:
        print("Exiting application?")
        break
    else:
        print("Invalid choice")

#print(f"You selected option {choice}")