class Product:
  def __init__ (self, name, price, amount):
    self.name = name
    self.price = price
    self.amount = amount
  def calculate(self):
    total = self.price * self.amount
    print(total)
  def apply_discount(self, discount):
    new_price = self.price * discount
    print(new_price)
