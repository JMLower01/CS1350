#Problem 2

class Session:
    def __init__(self, title):
        self.title = title
        self.attendees = set()
        
    def register(self, name):
        self.attendees.add(name)
        
    def unregister(self,name):
        self.attendees.discard(name)
    
    def attendee_count(self):
        return len(self.attendees)
    
def attended_all(sessions):
    attended_all = sessions[0].attendees
    for session in sessions:
        attended_all &= session.attendees
    return attended_all

def attended_exactly_one(sessions):
    attended_one = set()
    for session in sessions:
        attended_one ^= session.attendees
    return attended_one

def no_shows(registered, sessions):
    no_shows = set(registered)
    for session in sessions:
        no_shows -= session.attendees
    return no_shows

def summary(sessions):
    attended_any = set()
    for session in sessions:
        print(f"{session.title}: {len(session.attendees)} attendees")
        attended_any |= session.attendees
    print(f"Distinct attendees: {len(attended_any)}")

keynote = Session("Keynote")
for p in ["Ana", "Ben", "Cruz", "Dee"]:
    keynote.register(p)
    
workshop = Session("Workshop")
for p in ["Ana", "Cruz", "Eli"]:
    workshop.register(p)

panel = Session("Panel")
for p in ["Ana", "Dee", "Eli", "Fay"]:
    panel.register(p)

workshop.unregister("Eli")
workshop.unregister("Zed")
print(workshop.attendee_count())
sessions = [keynote, workshop, panel]
print(attended_all(sessions))
print(attended_exactly_one(sessions))
print(no_shows({"Ana", "Ben", "Fay", "Gus"}, sessions))

summary(sessions)

#Problem 4

from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, number, nights):
        self.number = number
        if Room.validate_nights(nights):
            self.nights = nights
    
    @abstractmethod
    def cost(self):
        pass
    
    def receipt(self):
        return f"Room {self.number} ({self.nights} nights): ${self.cost():.2f}"
    
    @staticmethod
    def validate_nights(nights):
        if nights > 0:
            return True
        else:
            raise ValueError("Nights must be positive")
class StandardRoom(Room):
    def __init__(self, number, nights, rate=100.00):
        super().__init__(number, nights)
        self.rate = rate
    
    def cost(self):
        return self.nights * self.rate

class DeluxeRoom(StandardRoom):
    def __init__(self, number, nights, rate=100.00, breakfast=15.00):
        super().__init__(number, nights, rate)
        self.breakfast = breakfast
            
    def cost(self):
        return super().cost() + (self.nights * self.breakfast)

class Suite(Room):
    def __init__(self, number, nights, rate=250.00, discount_pct=0.10):
        super().__init__(number, nights)
        self.rate = rate
        self.discount_pct = discount_pct
        
    def cost(self):
        if self.nights >= 3:
            return self.nights * self.rate * (1 - self.discount_pct)
        else:
            return self.nights * self.rate
        
def invoice(rooms):
    total = 0.0
    for room in rooms:
        print(room.receipt())
        total += room.cost()
    print(f"Total: ${total:.2f}")
    return total


rooms = [
    StandardRoom(101, 2),
    DeluxeRoom(205, 2, rate=120.00),
    Suite(901, 3)
]
       
total = invoice(rooms)

try:
    Room.validate_nights(0)
except ValueError as e:
    print("Caught:", e) 