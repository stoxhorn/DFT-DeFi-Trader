
class coin:
    
    def __init__(self, name):
        self.amount = -1
        self.avg_buy_price = -1
        self.net_buy_value = -1
        self.name = name

    def add_buy(self, Buy_Order):
        if self.avg_buy_price < 0:
            self.avg_buy_price 
        else:
            self.avg_buy_price = (self.avg_buy_price + buy_order.buy_price)/2
        
        if net_buy_price < 0:
            self.net_buy_price 
        else:
            self.net_buy_price += buy_order.buy_price
        
        self.amount += Buy_Order.total_coins
    
    def add_sell(Sell_Order):
        self.net_buy_value -= Sell_Order.total_USD
        self.amount -= Sell_Order.total_coins
        self.net_buy_value -= Sell_Order