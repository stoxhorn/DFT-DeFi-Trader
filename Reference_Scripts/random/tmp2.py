import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.pack()

def get_coordinates(event):
    canvas.itemconfigure(tag, text='({x}, {y})'.format(x=event.x, y=event.y))

canvas.bind('<Motion>', get_coordinates)
canvas.bind('<Enter>', get_coordinates)  # handle <Alt>+<Tab> switches between windows
tag = canvas.create_text(10, 10, text='', anchor='nw')

root.mainloop()