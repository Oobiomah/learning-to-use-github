class OnidesCafe:
    def __init__ (self, name, drink, qty, size='small', price=500):
        self.name = name
        self.drink = drink
        self.qty = qty
        self.size = size
        self.price = price

    def total_price(self):
        return round((self.price*1.075*self.qty), 2)

    def __str__ (self):
        return (
            '------------------------------------------\n'
            f"      ONIDE'S CAFE CUSTOMER RECEIPT\n"       
            '------------------------------------------\n'
            f'Customer Name: {self.name}\n'
            f'Item: {self.drink}\n'
            f'Quantity {self.qty}\n'
            f'Description: {self.qty} {self.size} sized {self.drink}\n'
            f'Total Amount: plus 7.5% vat: N{self.total_price()} \n'
            f' \n'
            f'    THANK YOU FOR YOUR PATRONAGE\n'
            f'------------------------------------------\n'
        )
receipt = OnidesCafe('Confidence', 'Yoghurt', 4, 'medium', 750)
print(receipt)
