def validate_input(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        return "Invalid side"

    if order_type not in ["MARKET", "LIMIT"]:
        return "Invalid order type"

    if order_type == "LIMIT" and not price:
        return "Price required for LIMIT order"

    return None