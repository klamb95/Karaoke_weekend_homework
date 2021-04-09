class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def customer_can_afford(self, room):
        return self.wallet >= room.entry_fee

    def pay_entry_fee(self, room):
        self.wallet -= room.entry_fee

        