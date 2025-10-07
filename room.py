class Room():
    def __init__(self):
        self.name = None
        self.description = None

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.locked = False

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description
    
    def set_name(self, room_name):
        self.name = room_name
    
    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character
    
    def get_character(self):
        return self.character

    def get_item(self):
        return self.item
    
    def set_item(self, item_name):
        self.item = item_name

    def lock(self):
        self.lock = True
    
    def unlock(self):
        self.lock = False

    def describe(self):
        print( self.description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        

    def get_details(self):
        print( self.name )
        print( "--------------------" )
        print( self.description )
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction )



    def move(self, direction):
        if direction in self.linked_rooms:
            if not self.linked_rooms[direction].locked:
                return self.linked_rooms[direction]
        
            else:
                print("The room is locked")
                return self
        else:
            print("You can't go that way")
            return self 
        

        
