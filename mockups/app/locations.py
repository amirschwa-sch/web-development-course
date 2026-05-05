class Location:
   def __init__(self):
       self.x = 0
       self.y = 0


   def move_right(self):
       self.x += 1
       return self.x


   def move_left(self):
       self.x -= 1
       return self.x


   def move_up(self):
       self.y += 1
       return self.y


   def move_down(self):
       self.y -= 1
       return self.y

if __name__ == "__main__":
 location = Location()
 print(f"(x={location.x}, y={location.y})")
