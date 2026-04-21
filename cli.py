from bot.orders import place_order
from bot.validators import validate_input
import logging
import bot.logging_config

def main():
    symbol = input("Enter symbol (e.g BTCUSDT): ")
    side = input("BUY or SELL: ")
    order_type = input("MARKET or LIMIT: ")
    quantity = float(input("Quantity: "))

    price = None
    if order_type == "LIMIT":
        price = input("Price: ")

    error = validate_input(symbol, side, order_type, quantity, price)

    if error:
        print("Error:", error)
        return

    result = place_order(symbol, side, order_type, quantity, price)

    if "error" in result:
        print("Failed:", result["error"])
        logging.error(result["error"])
    else:
        print("Order placed successfully!")
        print(result)
        logging.info(result)

if __name__ == "__main__":
    main()