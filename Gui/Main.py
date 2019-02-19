import threading
from tkinter import messagebox, filedialog
from tkinter.ttk import Treeview
from Environment import *
from tkinter import *


class Gui(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.gui = parent
        self._initializeUserInterface()  # Инициализируем интерфейс

    def _initializeUserInterface(self):
        self.gui.title("Main")  # Устанавливаем название окна
        self.gui.minsize(width=WIDTH, height=HEIGHT)
        self.gui.resizable(width=0, height=0)
        self.gui.overrideredirect(False)
        self.gui.call("wm", "attributes", ".", "-topmost", "1")
        # tk.Tk.iconbitmap(self, default="")
        self.fps = DoubleVar(value=999)  # Переменная fps
        self.visible_others = DoubleVar(value=False)  # Переменная видимости остальных
        self.env = Environment()  # Инициализируем среду

        self.slider = PanedWindow(self.gui)
        self.slider.pack(fill=BOTH, expand=True)  # Создаю слайдер
        self.environment_board = Canvas(self.slider, width=WIDTH_MAP, height=HEIGHT_MAP, bg="black")
        self.options_board = LabelFrame(self.slider, text="", width=250, relief=FLAT)
        self.settings_board = LabelFrame(self.options_board, text="Настройки")
        self.settings_board.pack(fill="both")
        self.statistic_board = LabelFrame(self.options_board, text="Статистика")
        self.statistic_board.pack(fill="both")
        soon = LabelFrame(self.options_board, text="Скоро!")
        soon.pack(fill="both", expand="yes")
        Label(self.settings_board, text="Fps: ") \
            .grid(row=0, column=0, sticky=W, padx=5, pady=0)
        Label(self.settings_board, text="Эпоха:") \
            .grid(row=1, column=0, sticky=W, padx=5, pady=0)
        Label(self.settings_board, text="Дамп:") \
            .grid(row=2, column=0, sticky=W, padx=5, pady=0)
        Label(self.settings_board, text="Боты видят других: ") \
            .grid(row=3, column=0, sticky=W, padx=5, pady=0)
        Label(self.settings_board, text="0") \
            .grid(row=1, column=1, sticky=W, padx=4, pady=0)
        Label(self.settings_board, text="Дамп не используют!") \
            .grid(row=2, column=1, sticky=E, padx=4, pady=0)
        Spinbox(self.settings_board, from_=1, to=10000, textvariable=self.fps) \
            .grid(row=0, column=1, columnspan=4, sticky=W, padx=5)
        Checkbutton(self.settings_board, text="(Y/N)", variable=self.visible_others) \
            .grid(row=3, column=1, sticky=W, padx=0, pady=0)

        _headers = ['#', 'Счёт']
        self.scores = Treeview(self.statistic_board, columns=_headers, show="headings", selectmode='browse')
        self.scores.place(x=0, y=0)
        vsb = Scrollbar(self.statistic_board, orient="vertical", command=self.scores.yview)
        vsb.place(x=90, y=0, height=220)

        self.scores.configure(yscrollcommand=vsb.set)
        self.scores.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.scores.heading(_headers[0], text=_headers[0].title(),
                            command=lambda c=_headers[0]: self._listSort(self.scores, c, 0))
        self.scores.column(_headers[0], minwidth=5, width=20, stretch=NO)
        self.scores.heading(_headers[1], text=_headers[1].title(),
                            command=lambda c=_headers[1]: self._listSort(self.scores, c, 0))
        self.scores.column(_headers[1], minwidth=5, width=62, stretch=NO)

        self.statistic_board.columnconfigure(0)

        self.slider.add(self.environment_board)
        self.slider.add(self.options_board)
        self._load()
        for bot in self.env.bots:
            self.scores.insert('', 'end', values=[bot.id, bot.energy])

    def update(self):
        threading.Thread(target=self._update()).start()

    def _update(self):
        while True:
            print(len(self.env.bots))
            self.env.update()
            for bot in self.env.bots:
                objBot = self.environment_board.create_oval(6, 6, bot.diameter, bot.diameter, fill=bot.color)
                objText = self.environment_board.create_text(0, 0, fill="darkblue", font="Times 8 italic bold",
                                                             text=bot.id)
                self.environment_board.move(objText, bot.x + bot.diameter / 2 - 6, bot.y - bot.diameter / 2 + 3)
                self.environment_board.move(objBot, bot.x - bot.diameter / 2, bot.y - bot.diameter)
                self.gui.update()
            self.environment_board.delete('all')

    def _load(self):
        MsgBox = messagebox.askquestion('Загрузка из дампа.', 'Загрузить из дампа?', icon='warning')
        if MsgBox == 'yes':
            filename = filedialog.askopenfilename(title="Выбор файла.", filetypes=(("Файл дампа", "*.json"),))
            if filename:
                Label(self.settings_board, text=filename).grid(row=2, column=1, sticky=W, padx=0, pady=0)
                self.env.setup(filename)
            else:
                self.env.setup()
        else:
            self.env.setup()

    def _listSort(self, tree, col, descending):
        data = [(tree.set(child, col), child) \
                for child in tree.get_children('')]
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        tree.heading(col, command=lambda col=col: self._listSort(tree, col, int(not descending)))


def main():
    root = Tk()
    d = Gui(root)
    d.update()
    root.mainloop()


if __name__ == "__main__":
    main()
