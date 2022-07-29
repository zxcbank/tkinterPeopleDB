import tkinter as Tk

NAMES = ['Name:', 'Surname:', 'Adres:', 'City:', 'Phune Number:', 'Post index:']
LABELS = []
FRAMES_LABELS = []
FRAMES_ENTRIES = []
TEXTS = []
BUTTONS = []
window_start = Tk.Tk()
PEOPLE_DB = open("DB.txt", 'w')




def window_start_init():

    window_start.title("пошел нахуй иди нахуй иди в жопу")
    for i in range(len(NAMES)):
        window_start.rowconfigure(i, weight = 1, minsize=30)
        FRAMES_LABELS.append(Tk.Frame(master = window_start, borderwidth=1, relief=Tk.RAISED))
        FRAMES_LABELS[i].grid(row=i, column=0)
        FRAMES_ENTRIES.append(Tk.Frame(master=window_start, borderwidth=1, relief=Tk.RAISED))
        FRAMES_ENTRIES[i].grid(row=i, column=1)
        LABELS.append(Tk.Label(master=FRAMES_LABELS[i], text= NAMES[i], ))
        LABELS[i].grid(sticky=Tk.W)
        TEXTS.append(Tk.Entry(master=FRAMES_ENTRIES[i]))
        TEXTS[i].grid(sticky=Tk.E)

    BUTTON1 = Tk.Button(text="SEND")
    BUTTONS.append(BUTTON1)
    BUTTON1.grid(column=1, sticky=Tk.W)
    BUTTON1.bind("<Button-1>", handle_click)
    window_start.mainloop()

def handle_click(event):
    final_line = ""
    for i in range(len(TEXTS)):
        final_line += NAMES[i] + TEXTS[i].get() + "\n"
    LABELS.clear()
    TEXTS.clear()
    FRAMES_LABELS.clear()
    FRAMES_ENTRIES.clear()
    BUTTONS[0].grid_forget()
    window_start.destroy()
    PEOPLE_DB.write(final_line)
    PEOPLE_DB.write("-------------------------")
    PEOPLE_DB.close()

if __name__ == '__main__':
    window_start_init()