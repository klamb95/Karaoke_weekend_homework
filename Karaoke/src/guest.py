class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def customer_can_afford(self, room):
        return self.wallet >= room.entry_fee

    def pay_entry_fee(self, room):
        if self.customer_can_afford(room):
            self.wallet -= room.entry_fee
            
         

    # def put_money_in_till(self, room):
    #     rooms.till += room.entry_fee
        

    



