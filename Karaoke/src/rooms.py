
class Rooms:
    def __init__(self, room_name, capacity, till):
        self.room_name = room_name
        self.occupants = []
        self.song_queue = []
        self.capacity = capacity
        self.till = till
        self.entry_fee = 1


    def number_in_room(self):
        return len(self.occupants)

    def add_person_to_room(self, guest):
        #if not self.room_has_space
        self.occupants.append(guest)

    def remove_person(self, guest):
        self.occupants.remove(guest)

    def songs_in_queue(self):
        return len(self.song_queue)

    def add_song_to_queue(self, song):
        self.song_queue.append(song)

    def remove_songs_from_queue(self, song):
        self.song_queue.remove(song)

    def room_has_space(self):
        if len(self.occupants) < self.capacity:
            return "Room has space"
        else: 
            return "Room is full"

    # def increase_till(self):
    #      self.till += self.entry_fee        
    

     

    


    

   


       




