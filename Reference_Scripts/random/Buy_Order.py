class Buy_Order:
    # will calculate left out lastly needed data, amont buy_price, total_usd and total_coins, if one is left as a string
    def __init__(self, buy_price, total_USD, total_coins, coin_name, spread = 5):
        self.status = "open"
        self.type = "buy"
        self.index = -1

        def checkVals(x, y):
            try:
                x = float(x)
                y = float(y)
                if x <= 0 or y <= 0:
                    return None
                z = y/x
                return [x, y, z]
            except:
                return None
            
        data = []

        funcs = [checkVals(buy_price, total_USD), checkVals(buy_price, total_coins), checkVals(total_coins, total_USD)]
        for i in funcs:
            if i != None and len(data) < 1:
                data = i.copy()
        self.shit = False
        if data == []:
            self.shit = True
            return None

        self.buy_price = data[0]
        self.total_USD = data[1]
        self.total_coins = data[2]
        self.coin_name = coin_name
    
        self.first_fee = self.total_USD * 0.00075

        self.profit_graph = [[],[],[]]
        itr_price = self.buy_price * 0.97

        for i in range(spread*2*10):
           tmp = self.calc_profit_sell_price(itr_price)
           self.profit_graph[0].append(tmp[0])
           self.profit_graph[1].append(tmp[1])
           self.profit_graph[2].append(tmp[2])
           itr_price += 0.1

        self.min_sell_price = (self.buy_price + self.first_fee) / 0.99925056207844116912315763177617

    def close(self):
        self.status = "closed"

    def __str__(self):
        str = "Buy_Order"
        deli = " - "
        str += deli + self.status
        str += deli + str(self.index)
        str += deli + str(self.shit)
        str += deli + str(self.buy_price)
        str += deli + str(self.total_USD)
        str += deli + self.coin_name
        return str

    def calc_profit_sell_price(self, sell_price):
        sell_usd = sell_price * self.total_coins
        second_fee = sell_usd * 0.00075
        profit = sell_usd - second_fee - self.total_USD - self.first_fee
        return ((profit/self.total_USD)*100, sell_price, profit)

