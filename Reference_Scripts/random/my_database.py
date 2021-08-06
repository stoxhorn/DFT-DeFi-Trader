from Buy_Order import Buy_Order
from Sell_Order import Sell_Order
from coin import coin

class my_database:

    def __init__(self):
        self.start_balance = 0
        self.start_balance_today = 0
        
        self.balance_increase_today = 0
        self.balance_increase_total = 0

        self.open_buy_orders = []
        self.open_sell_orders = []
        
        self.new_closed_buy_orders = []
        self.new_closed_sell_orders = []

        self.old_closed_sell_orders = []
        self.old_closed_buy_orders = []
        
        self.total_usd = 0
        self.current_buy_power = 0
        self.buy_power_in_open_orders = 0
        self.usd_in_open_sell_orders = 0

        self.holding = {}


    def open_order(self, order):
        if order.type == "sell":
            self.open_sell_orders.append(order)
            order.index = len(self.open_sell_orders) -1
            self.usd_in_open_sell_orders += order.net_sell_value
        elif order.type == "buy":
            self.open_buy_orders.append(order)
            order.index = len(self.open_buy_orders) -1
            self.buy_power_in_open_order += order.total_USD


    def close_sell_order(self, order):
        order.close()
        self.new_closed_sell_orders.append(order)
        order.index = len(self.new_closed_sell_orders) -1
        self.holding[order.coin_name].add_sell(order)
        
        self.total_usd += order.net_profit
        self.current_buy_power += order.net_sell_value
        self.usd_in_open_sell_orders -=order.net_sell_value
        


    def close_buy_order(self, order):
        self.new_closed_buy_orders.append(order)
        order.index = len(self.new_closed_buy_orders) -1
        self.current_buy_power -= order.total_USD
        self.buy_power_in_open_order -= order.total_USD
        self.total_usd

        if self.holding[order.coin_name] != None:
            self.holding[order.coin_name].add_buy(order)
        else:
            self.holding[order.coin_name] = coin(order.coin_name)
            self.holding[order.coin_name].add_buy(order)

    def update_history(self):
        with open("DAYTABAYSE.txt", "a",encoding = 'utf-8') as f:
            while len(self.new_closed_sell_orders) > 0:
                tmp = self.new_closed_sell_orders.pop()
                self.balance_increase_today += tmp.profit
                self.balance_increase_total += tmp.profit
                f.write(str(tmp))
                self.old_closed_sell_orders.append(tmp)

            
            while len(self.new_closed_buy_orders) > 0:
                tmp = self.new_closed_buy_orders.pop()
                f.write(str(tmp))
                self.old_closed_buy_orders.append(tmp)
        with open("test.txt", "r+",encoding = 'utf-8') as f:
            f.write(self.balance_increase_today)
            f.write(self.balance_increase_total)
        
    
    def readFile(self):
        try:
            f = open("DAYTABAYSE.txt")
            

        except FileNotFoundError:
            file = open("DAYTABAYSE.txt", "w")
            file.write("-|-")
            return
        finally:
            f.close()
        
        with open("DAYTABAYSE.txt", "r",encoding = 'utf-8') as f:
            check = True
            for line in f:
                if check:
                    self.balance_increase_total = int(line)
                    check = False
                if line.startswith("Buy_Order"):
                    self.read_buy_order(line)
                elif line.startswith("Sell_Order"):
                    self.read_sell_order(line)

    def add_old_buy_order(self, order):
        
        self.old_closed_buy_orders.append(order)
        order.index = len(self.old_closed_buy_orders) -1

        if self.holding[order.coin_name] != None:
            self.holding[order.coin_name].add_buy(order)
        else:
            self.holding[order.coin_name] = coin(order.coin_name)
            self.holding[order.coin_name].add_buy(order)

    def add_old_sell_order(self, order):
        order.index = len(self.new_closed_sell_orders) -1
        self.holding[order.coin_name].add_sell(order)


    def read_buy_order(self, str):
        str = line.split(" - ")
        status = str[1]
        shit = bool(str[2])
        buy_price = float(str[3])
        total_USD = float(str[4])
        coin_name = str[5]
        
        order = Buy_Order(buy_price, total_USD, "n/a", coin_name)
        order.status = status
        order.shit = shit
        self.add_old_buy_order(order)

    def read_sell_order(self, str):
        str = line.split(" - ")
        status = str[1]
        coin_name = str[2]
        profit_ratio = float(str[3])
        profit = float(str[4])
        sell_price = float(str[6])
        total_usd = float(str[7])

        order = Sell_Order(status, coin_name, profit_ratio, profit, sell_price, total_usd)
        order.status = status
        self.add_old_sell_order(order)
        
        




    
    
