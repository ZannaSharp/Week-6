class Tickets:
    counter = 0  # Static field to keep track of ticket numbers

    def __init__(self):
        self.staff_id = input("Enter Staff ID: ")
        self.ticket_creator_name = input("Enter Ticket Creator Name: ")
        self.contact_email = input("Enter Contact Email: ")
        self.description = input("Enter Description of the Issue: ")
        Tickets.counter += 1
        self.ticket_number = Tickets.counter + 2000  # Assigning ticket number

    def submit_ticket(self):
        print("Ticket submitted successfully!")
        

    def respond_to_ticket(self):
        if "Password Change" in self.description:
            new_password = self.generate_password()
            print("New password:", new_password)
        else:
            print("No action needed for this ticket.")
    def generate_password(self):
    # Extract the required characters
        first_two_staff_id = self.staff_id[:2]
        first_three_creator_name = self.ticket_creator_name[:3]

    # Concatenate and return the new password
        new_password = first_two_staff_id + first_three_creator_name
        return new_password

# Example usage
def main():
    staff_id = input("Enter Staff ID: ")
    ticket_creator_name = input("Enter Ticket Creator Name: ")
    description = input("Enter Description of the Issue: ")


# Example usage
if __name__ == "__main__":
    ticket = Tickets()
    ticket.submit_ticket()
    ticket.respond_to_ticket()

    if "Password Change" in ticket.description:
        new_password = ticket.generate_password()
        print("New password:", new_password)
    else:
        print("No action needed for this ticket.")
