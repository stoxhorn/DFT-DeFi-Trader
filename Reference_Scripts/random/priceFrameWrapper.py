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
from Buy_Order import Buy_Order
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)


class priceFrameWrapper:
    def __init__(self, main_frame, ui, dapp):
        self.ui = ui
        self.dapp = dapp
        self.main_frame = main_frame

        self.frame = tk.Frame(master = self.main_frame)
        self.frame.configure(background='black')
        self.frame.pack(fill = tk.X, side=tk.LEFT)
        
        self.graph_data = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.graph_main_frame = tk.Frame(master = self.main_frame, background = "black")
        self.graph_main_frame.pack(fill=tk.Y, side=tk.RIGHT)
        self.labels_and_entries()
        self.graph()
        self.frame.pack()



    def labels_and_entries(self):
        self.labels = []
        self.entries = []
        self.widgets = []

    

            
            

        self.ui.bind("<Return>", self.calculate_graph)

        
        labels = ["Buy Price", "Total USD", "Total amount of Coins", "Coin Name"]
        for i in labels:
            self.labels.append(tk.Label(master = self.frame, text = i, fg="white", bg="black"))    
            self.entries.append(tk.Entry(master = self.frame, fg="white", bg="black"))
   
        

        for i in self.entries:
            i.insert(0,"0")
        
        d = 0
        for i in self.labels:
            self.widgets.append(i)
            self.widgets.append(self.entries[d])
            d += 1
        
        for i in self.widgets:
            i.pack()
        
        self.buy_button = tk.Button(master = self.frame, width = 20, fg = "blue", bg = "black", command = self.dapp.make_sell_order, text = "Make Buy Order")
        self.buy_button.pack()
        
        self.sell_label = tk.Label(master = self.frame, text = "Sell Price", fg = "yellow", bg = "black")
        self.sell_label.pack()
        self.sell_entry = tk.Entry(master = self.frame, fg="white", bg="black")
        self.sell_entry.pack()
        self.sell_button = tk.Button(master = self.frame, width = 20, fg = "white", bg = "black", command = self.dapp.make_sell_order, text = "Make Sell Order")
        self.sell_button.pack()
        # i can insert text by using .insert(), delete with delete('index'), and get the text with .get()

        # final button to calculate graph
        self.labels.append(tk.Button(master = self.frame, text="Calc", bg = "black", fg = "white"))

    def calculate_graph(self, event):
        buy_price = self.entries[0].get()
        total_USD = self.entries[1].get()
        total_coins = self.entries[2].get()
        coin_name = self.entries[3].get()
        
        if len(coin_name) < 2:
            return None
        
        self.new_order = Buy_Order(buy_price, total_USD, total_coins, coin_name)

        if self.new_order == None:
            return
        elif self.new_order.shit == True:
            return
        else:
            self.graph_data = self.new_order.profit_graph
            tmp = tk.Label(master = self.frame, text = "Min. Sell Price:\n" + str(self.new_order.min_sell_price), fg = "white", bg = "black")
            tmp.pack()


            self.graph_frame.destroy()
            self.graph()
            return
        
        

    def graph(self):
        # Default data, data with no input
        self.graph_frame = tk.Frame(master = self.graph_main_frame, background = "black")
        
        
       
        
        np1 = np.array([self.graph_data[0],
                       self.graph_data[1]
        ])
        
        pos_np1 = [[],[]]
        for i in range(len(np1[0])):
            if np1[0][i] > 0:
                pos_np1[1].append(np1[1][i])
                pos_np1[0].append(np1[0][i])

        neg_np1 = [[],[]]
        for i in range(len(np1[0])):
            if np1[0][i] <= 0:
                neg_np1[1].append(np1[1][i])
                neg_np1[0].append(np1[0][i])


        fig = plt.Figure(figsize=(5,4), dpi=100)
        # fig.add_subplot(111).plot(pos_np1[0], pos_np1[1], color='g')
        # fig.add_subplot(111).plot(neg_np1[0], neg_np1[1], color='r')

        

        ax = fig.add_subplot(111)
        
        ax.plot(pos_np1[0], pos_np1[1], color='g')
        ax.plot(neg_np1[0], neg_np1[1], color='r')
        ax.grid(True, linestyle='-', color = "w")
        ax.grid(b = True, linestyle='--', color = "grey", which = "minor")
        

        x_dif = abs(np1[0][1] - np1[0][0])
        y_dif = abs(np1[1][1] - np1[1][0])
        
        if x_dif or y_dif != 0:
            x_maj_dif = x_dif * 10
            x_min_dif = x_dif * 5

            y_maj_dif = y_dif * 10
            y_min_dif = y_dif * 5

            ax.yaxis.set_major_locator(MultipleLocator(x_maj_dif))
            ax.yaxis.set_minor_locator(MultipleLocator(x_min_dif))
            
            ax.xaxis.set_major_locator(MultipleLocator(y_maj_dif))
            ax.xaxis.set_minor_locator(MultipleLocator(y_min_dif))
        
        
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)


        canvas.get_tk_widget().pack(fill=tk.BOTH, side=tk.TOP, expand=1)



        cursor = FollowDotCursor(ax,np1[0], np1[1], fig, tolerance = 20)

       
        self.graph_frame.pack(fill=tk.Y, side=tk.RIGHT)
       
        hover_label = tk.Label(master = self.graph_frame, text = "price: 0\nprofit: 0", fg="white", bg="black", anchor = "nw")
        hover_label.pack(fill = tk.X, side = tk.LEFT)
        price_label = tk.Label(master = self.graph_frame, text = "price: 0\nprofit: 0", fg="white", bg="black", anchor = "nw")
        price_label.pack(fill = tk.X, side = tk.RIGHT)




        def set_price(event):
            x = event.xdata
            y = event.ydata
            sell_ratio, sell_price, profit = get_results(self, x,y)    
            price_label['text'] = "sell price: " + str(sell_price) + "\nratio: "+ str(sell_ratio) + "\nprofit: " + str(profit)

        def set_hover(event):
            x = event.xdata
            y = event.ydata
            sell_ratio, sell_price, profit = get_results(self, x,y)
            hover_label['text'] = "sell price: " + str(sell_price) + "\nratio: "+ str(sell_ratio) + "\nprofit: " + str(profit)

        fig.canvas.mpl_connect('motion_notify_event', set_hover)
        fig.canvas.mpl_connect('button_press_event', set_price)
        
        def get_results(self, x, y):
            tmp = cursor.snap(x,y)[1]
            if y < 1:
                b = "%e" % y
                z = int(str.partition(b, '-')[2])
                z += 4
            elif y < 10:
                z = 3
            elif y < 100:
                z = 2
            elif y < 1000:
                z = 1
            else: 
                z = 0
            sell_ratio = round(self.graph_data[0][tmp], 2)
            sell_price = round(self.graph_data[1][tmp], z)
            profit = round(self.graph_data[2][tmp], 2)
            return (sell_ratio, sell_price, profit)
        # the lines from the mouse hovering over the graph won't work if mainloop is called elsewhere
        
def fmt(x, y):
    return 'x: {x:0.2f}\ny: {y:0.2f}'.format(x=x, y=y)

class FollowDotCursor(object):
    """Display the x,y location of the nearest data point.
    https://stackoverflow.com/a/4674445/190597 (Joe Kington)
    https://stackoverflow.com/a/13306887/190597 (unutbu)
    https://stackoverflow.com/a/15454427/190597 (unutbu)
    """
    def __init__(self, ax, x, y, fig, tolerance=5, formatter=fmt, offsets=(-20, 20)):
        try:
            x = np.asarray(x, dtype='float')
        except (TypeError, ValueError):
            x = np.asarray(mdates.date2num(x), dtype='float')
        y = np.asarray(y, dtype='float')
        mask = ~(np.isnan(x) | np.isnan(y))
        x = x[mask]
        y = y[mask]
        self._points = np.column_stack((x, x))
        self._truepoints = np.column_stack((x, y))
        self.offsets = offsets
        y = y[np.abs(y-y.mean()) <= 3*y.std()]
        self.scale = x.ptp()
        self.scale = y.ptp() / self.scale if self.scale else 1
        self.tree = spatial.cKDTree(self.scaled(self._points))
        self.formatter = formatter
        self.tolerance = tolerance
        self.ax = ax
        self.fig = ax.figure
        self.ax.xaxis.set_label_position('top')
        self.dot = ax.scatter(
            [x.min()], [y.min()], s=130, color='white', alpha=0.7)
         #self.annotation = self.setup_annotation()
        fig.canvas.mpl_connect('motion_notify_event', self)
        #plt.connect('motion_notify_event', self)

    def scaled(self, points):
        
        points = np.asarray(points)
        if points.all() == None:
            return [None,None]
        else:
            return points * (self.scale, 1)

    def __call__(self, event):
        ax = self.ax
        # event.inaxes is always the current axis. If you use twinx, ax could be
        # a different axis.
        if event.inaxes == ax:
            x, y = event.xdata, event.ydata
        elif event.inaxes is None:
            return
        else:
            inv = ax.transData.inverted()
            x, y = inv.transform([(event.x, event.y)]).ravel()
        #annotation = self.annotation
        x, y = self._truepoints[self.snap(x, y)[1]]
        if x != None:
            self.dot.set_offsets(np.column_stack((x, y)))

        #annotation.xy = x, y
        #annotation.set_text(self.formatter(x, y))
        #bbox = self.annotation.get_window_extent()
        #self.fig.canvas.blit(bbox)
        self.fig.canvas.draw_idle()

    def setup_annotation(self):
        """Draw and hide the annotation box."""
        annotation = self.ax.annotate(
            '', xy=(0, 0), ha = 'right',
            xytext = self.offsets, textcoords = 'offset points', va = 'bottom',
            bbox = dict(
                boxstyle='round,pad=0.5', fc='yellow', alpha=0.75),
            arrowprops = dict(
                arrowstyle='->', connectionstyle='arc3,rad=0'))
        return annotation

    def snap(self, x, y):
        """Return the value in self.tree closest to x, y."""
        tmp = self.scaled((x, x))
        if tmp[0] == None:
            return (None,None)
        else:
            idx = self.tree.query(tmp, k=1, p=1)
            try:
                return idx
            except IndexError:
                # IndexError: index out of bounds
                return self._points[0]
        
