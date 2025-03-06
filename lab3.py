import queue
class Ticket:
    def __init__(self, customer_name, ticket_id, issue, priority):
        self.customer_name = customer_name
        self.ticket_id = ticket_id
        self.issue = issue
        self.priority = priority

    def __lt__(self, other):
        return self.priority > other.priority  # Higher priority comes first

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Customer: {self.customer_name}, Priority: {self.priority}, Issue: {self.issue}"


class TicketingSystem:
    def __init__(self):
        self.ticket_counter = 1
        self.queue = queue.PriorityQueue()

    def submit_ticket(self, customer_name, issue, priority=False):
        ticket = Ticket(customer_name, self.ticket_counter, issue, priority)
        self.queue.put(ticket)
        print(f"Ticket submitted successfully! {ticket}")
        self.ticket_counter += 1

    def view_tickets(self):
        if self.queue.empty():
            print("No tickets to display")
            return
        
        temp_list = []
        while not self.queue.empty():
            ticket = self.queue.get()
            temp_list.append(ticket)
            print(ticket)
        
        # Put the tickets back in the queue
        for ticket in temp_list:
            self.queue.put(ticket)

    def process_ticket(self):
        if self.queue.empty():
            print("kuch bhi noi he re dada ")
            return
        
        ticket = self.queue.get()
        print(f"Processing ticket: {ticket}")
        return ticket


def main():
    ticketing_system = TicketingSystem()
    while True:
        print("\n1. Submit Ticket\n2. View Tickets\n3. Process Ticket\n4. Exit")
        choice = input("choice daalo re baba: ")

        if choice == "1":
            customer_name = input("aapki taarif: ")
            issue = input("ab kya dikkat hai: ")
            priority = input("Is this a priority issue? (yes/no): ").lower() == "yes"
            ticketing_system.submit_ticket(customer_name, issue, priority)

        elif choice == "2":
            ticketing_system.view_tickets()

        elif choice == "3":
            ticketing_system.process_ticket()

        elif choice == "4":
            print("mai jaa rha hu by by ")
            break

        else:
            print("returning back from ticketing system")
            break


if __name__ == "__main__":
    main()


      