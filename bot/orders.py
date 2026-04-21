import random
import time

def place_order(symbol, side, order_type, quantity, price=None):
    time.sleep(1)

    if random.choice([True, True, False]):
        return {
            "orderId": random.randint(10000, 99999),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED",
            "executedQty": quantity,
            "avgPrice": price if price else round(random.uniform(20000, 30000), 2)
        }
    else:
        return {"error": "Simulated API failure"}