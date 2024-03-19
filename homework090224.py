#1
from gen import gen_consumer_basket

def payment(account: str, consumer_basket: list[dict]) -> dict:
    if not account:
        return ValueError("Account cannot be empty.")
    if not (set(account) <= {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'}) and account.count('.') != 1:
        return ValueError("Not correct price format. Example: XXX.XX")
    if not consumer_basket:
        return ValueError("Consumer basket cannot be empty.")
    total_price = 0
    account_floal = float(account)
    for position in consumer_basket:
        total_price += position['price'] * position['count']
    if total_price <= account_floal:
        return {"status": "Success",
                "comment": "Покупки оплачены"}
    else:
        return {"status": "Fail",
                "comment": f"Недостаточно средств. Внесите {total_price - account_floal} сумму"}

print(gen_consumer_basket(3))
print(payment("1000.0", consumer_basket=gen_consumer_basket(3)))


#2
def create_phone(number: list[int]) -> str:
    return "({}{}{}) {}{}{}-{}{}-{}{}".format(*number)

print(create_phone([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))