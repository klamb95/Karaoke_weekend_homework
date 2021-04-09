
class Rooms:
    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []
        self.song_playing = []

    def number_in_room(self):
        return len(self.occupants)

    

    def add_person_to_room(self, guest):
        self.occupants.append(guest)
       




