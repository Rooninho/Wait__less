# from seating import SeatingManager
# from announcer import announce_customer
# import time

# def run_queue():
#     manager = SeatingManager()

#     # Sample customers (C = customer, S = staff)
#     arrivals = ["C101", "S001", "C102", "C103", "S002", "C104"]

#     for person in arrivals:
#         if person.startswith("S"):
#             print(f"{person} is staff → skipped.")
#             continue
#         manager.add_customer(person)

#     # Process queue every 30 seconds
#     while manager.has_customers():
#         customer, desk = manager.assign_desk()
#         if customer:
#             announce_customer(customer, desk)
#         time.sleep(5)  # use 30 for real

# if __name__ == "__main__":
#     run_queue()

from seating import SeatingManager
from announcer import announce_customer
import time

def run_queue():
    manager = SeatingManager()

    # Sample customers (C = customer, S = staff)
    arrivals = ["C101", "S001", "C102", "C103", "S002", "C104"]

    for person in arrivals:
        if person.startswith("S"):
            print(f"{person} is staff → skipped.")
            continue
        manager.add_customer(person)

    # Process queue every 30 seconds
    while manager.has_customers():
        customer, desk = manager.assign_desk()
        if customer:
            announce_customer(customer, desk)
        time.sleep(5)  # use 30 for real

if __name__ == "__main__":
    run_queue()