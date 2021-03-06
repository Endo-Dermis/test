from tkinter import *


class Window(Frame):
	def __init__(self, master=None):
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("Window")

	@staticmethod
	def main():
		app = Tk()
		app.geometry("500x500")
		window = Window(app)
		app.mainloop()


if __name__ == "__main__":
	Window.main()