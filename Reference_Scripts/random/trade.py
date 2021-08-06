from matplotlib.widgets import Cursor
import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import scipy.spatial as spatial
import numpy as np
from priceFrameWrapper import priceFrameWrapper
from Buy_Order import Buy_Order
from Sell_Order import Sell_Order
from my_database import my_database


class dapp:

    def __init__(self):
        mpl.style.use('dark_background')
        self.ui = tk.Tk()
        
        self.ui.configure(background = 'black')
        self.main_frame = tk.Frame(master = self.ui, relief="ridge",background = "black")
        self.main_frame.pack()
        # create price frame
        self.price_wrapper = priceFrameWrapper(self.main_frame, self.ui, self)

        self.holding_frame = tk.Frame(master = self.main_frame)
        self.holding_frame.pack(side=tk.BOTTOM)
        self.my_database = my_database()
        self.openF()
        

    def make_buy_order(self):
        pass
    
    
    # need to transfer data from entries and labels
    def make_sell_order(self):
        sell_price = self.sell_entry
        new_sell_order = Sell_Order()
        new_sell_order.in1(sell_price, self.price_wrapper.new_order)
        self.my_database.open_order(new_sell_order)


    def run(self):
        self.ui.mainloop()

    def openF(self):
        self.my_database.readFile()
        database_labels = []
        database_labels.append(tk.Label(master = self.holding_frame, text = self.my_database.total_usd, fg = "white", bg = "black"))
        database_labels.append(tk.Label(master = self.holding_frame, text = self.my_database.current_buy_power, fg = "white", bg = "black"))
        database_labels.append(tk.Label(master = self.holding_frame, text = self.my_database.buy_power_in_open_orders, fg = "white", bg = "black"))
        database_labels.append(tk.Label(master = self.holding_frame, text = self.my_database.usd_in_open_sell_orders, fg = "white", bg = "black"))
        for i in database_labels:
            i.pack()
    







if __name__ == "__main__":
    a = dapp()
    a.run()    




