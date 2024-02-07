
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


def get_user_input(inpuniversal):
    return float(input(inpuniversal))  

x = get_user_input("Enter x coordinate for point1: ")
y = get_user_input("Enter y coordinate for point1: ")

point1 = Point(x, y)


dx = get_user_input("Enter dx (how much to move in x-direction): ")
dy = get_user_input("Enter dy (how much to move in y-direction): ")

original_point1 = Point(x, y)

# Move point1 by dx and dy
point1.move(dx, dy)

print(f"The coordinates of moved point: ({point1.x}:{point1.y})")

distance = point1.dist(original_point1)
print(f"Distance between the original and moved point1: {distance}")