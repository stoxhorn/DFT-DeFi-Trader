from Buy_Order import Buy_Order
from coin import coin
class Sell_Order:
    
    def __init__(self):
        self.type = "sell"
        self.index = -1

    def in1(self, sell_price, coin_name, total_usd):
        self.status = "open"
        
        self.coin_name = coin_name
        self.sell_price = sell_price
        self.total_usd = total_usd
        self.fee = total_usd * 0.00075

    def calculations(self, Coin):
        self.profit_ratio = self.sell_price/((self.sell_price*0.00075) + Coin.avg_buy_price + (Coin.avg_buy_price*0.00075))
        self.profit = self.profit_ratio * Coin.net_buy_value
    
    def in2(self, status, coin_name, profit_ratio, profit, sell_price,  total_usd):
        self.status = status
        self.coin_name = coin_name
        self.buy_order = None
        self.total_usd = total_usd

    def __str__(self):
        str = "Sell_Order"
        deli = " - "
        
        str += deli + self.status
        str += deli + self.coin_name

        str += deli + str(self.profit_ratio)
        str += deli + str(self.profit)
        str += deli + str(self.sell_price)

        str += deli + str(self.total_usd) + "\n"
        return str


    def close(self):
        self.status = "closed"
