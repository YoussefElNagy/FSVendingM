from Vending_Machine import VendingMachine
from visual_automata.fa.nfa import VisualNFA
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import sys


def insert_amount_handler():
    my_amount = myinput1.get()
    vending_machine.insert_amount(my_amount)
    # print(my_amount)


def make_selection_handler():
    vending_machine.make_selection(str(mygroup.get()))


def refill_button_handler():
    vending_machine.refill()


def cancellationhandler():
    vending_machine.cancel()

def create_state_diagram():
    nfa = VisualNFA(
        states={"Idle", "Waiting", "Refunding", "Dispensing"},
        input_symbols={"Refilled", "Amount In", "Insufficient Money", "Insert More", "Out of Stock",
                       "Enough Money","Cancel" ,"No Refund" ,"Completed" },
        transitions={
            "Idle": {"Refilled": {"Idle"}, "Amount In": {"Waiting"}},
            "Waiting": {"Insufficient Money": {"Waiting"}, "Insert More": {"Waiting"}, "Out of Stock": {"Waiting"},
                        "Enough Money": {"Dispensing"} ,"Cancel": {"Refunding"}},
            "Refunding": {"Completed": {"Idle"}},
            "Dispensing": {"Completed": {"Refunding"}, "No Refund": {"Idle"}},
        },
        initial_state="Idle",
        final_states={"Idle"},
    )
    nfa.show_diagram(filename='Digraph', format_type="png", path="test-graphs", view=False)
    # photo1 = ImageTk.PhotoImage(Image.open('test-graphs/Digraph.png'))
    # photo1.show()

if __name__ == '__main__':
    vending_machine = VendingMachine()
    vending_machine.refill()

    root = Tk()
    root.geometry("600x500")
    root.title("Vending Machine")

    mylabel1 = Label(root, text="Vending Machine", font=('arial', 40, 'bold'))
    mylabel1.grid(row=0, column=0, columnspan=3, padx=100, pady=50)

    mylabel2 = Label(root, text="Insert money: ")
    mylabel2.grid(row=1, column=0, padx=10, pady=10, sticky=E)

    myinput1 = Entry(root, width=20)  # amount = eltextbox
    myinput1.grid(row=1, column=1, padx=10, pady=10)

    mylabel3 = Label(root, text="Change: ")
    mylabel3.grid(row=2, column=0, padx=10, pady=10, sticky=E)

    # myinput2 = Entry(root, width=20)  # change=textbox2
    # myinput2.grid(row=2, column=1, padx=10, pady=10)
    mylabel4 = Label(root)
    mylabel4.grid(row=2, column=3, padx=10, pady=10, sticky=E)

    select_label = Label(root, text="Select an Item:")
    select_label.grid(row=3, column=0, padx=10, pady=10)

    mygroup = StringVar()
    myoption1 = ttk.Radiobutton(root, text="Pepsi 10.00", variable=mygroup, value="Pepsi")
    myoption1.grid(row=4, column=0, padx=10, pady=10)

    myoption2 = ttk.Radiobutton(root, text="Redbull 30.00", variable=mygroup, value="Redbull")
    myoption2.grid(row=4, column=1, padx=10, pady=10)

    myoption3 = ttk.Radiobutton(root, text="Sprite 10.00", variable=mygroup, value="Sprite")
    myoption3.grid(row=4, column=2, padx=10, pady=10)

    myoption4 = ttk.Radiobutton(root, text="Fanta 14.00", variable=mygroup, value="Fanta")
    myoption4.grid(row=5, column=0, padx=10, pady=10)

    myoption5 = ttk.Radiobutton(root, text="Sun Top 10.00", variable=mygroup, value="Sun Top")
    myoption5.grid(row=5, column=1, padx=10, pady=10)

    myoption6 = ttk.Radiobutton(root, text="Protein Bar 50.00", variable=mygroup, value="Protein Bar")
    myoption6.grid(row=5, column=2, padx=10, pady=10)

    purchase_button = Button(root, text="Purchase", command=make_selection_handler)
    purchase_button.grid(row=6, column=0, padx=10, pady=10)

    refill_button = Button(root, text="Refill", command=refill_button_handler)
    refill_button.grid(row=6, column=1, padx=10, pady=10)

    cancel_button = Button(root, text="Cancel", command=cancellationhandler)
    cancel_button.grid(row=6, column=2, padx=10, pady=10)

    insert_button = Button(root, text="Insert", command=insert_amount_handler)
    insert_button.grid(row=1, column=2, padx=10, pady=10)


    class IORedirector(object):
        def __init__(self, text_area):
            self.text_area = text_area

        def write(self, str):
            self.text_area.insert(END, str)
            self.text_area.see(END)  # Scroll to the end

        def flush(self):
            pass


    text_area = Text(root, height=10, width=70)
    text_area.grid(row=9, column=0, columnspan=3)

    sys.stdout = IORedirector(text_area)

    root.geometry("650x600")

    root.mainloop()
# create_state_diagram()

