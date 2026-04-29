from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: int
    quantity: int

    # Tells the computer that this is a field that needs to be recalculated
    # Serialized when 
    @computed_field
    #Tells that its a read only property as we have used property
    @property
    #Getter Method
    def total_amount(self) -> int:
        return self.price * self.quantity

buy_product = Product(
    price = 103,
    quantity = 4
        )

# Note that the methods are not called with ()
# Because this is read only properties
print(buy_product.total_amount)

print(buy_product.model_dump())
