import tkinter as tk


class MainApplicationWindow(tk.Tk):
    """
    Our main application window
    """
    def __init__(self):
        super().__init__()

        w, h = 500, 500
        x, y = (self.winfo_screenwidth()/2) - (w/2), (self.winfo_screenheight()/2) - (h/2)
        self.title("Tkinter Blank Window")
        self.geometry("%dx%d+%d+%d" % (w, h, x, y))


if __name__ == '__main__':
    root = MainApplicationWindow()
    root.mainloop()
