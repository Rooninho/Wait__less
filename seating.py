from collections import deque

class SeatingManager:
    def __init__(self):
        self.wingA = deque(range(1, 8))   # Desks 1–7
        self.wingB = deque(range(8, 15))  # Desks 8–14
        self.queue = deque()

    def add_customer(self, customer_id):
        self.queue.append(customer_id)

    def has_customers(self):
        return len(self.queue) > 0

    def assign_desk(self):
        if not self.queue:
            return None, None

        customer_id = self.queue.popleft()
        if self.wingA:
            return customer_id, f"Desk {self.wingA.popleft()} (Wing A)"
        elif self.wingB:
            return customer_id, f"Desk {self.wingB.popleft()} (Wing B)"
        else:
            print("⚠️ No available desks!")
            return None, None


