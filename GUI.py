# from tkinter import *
# from tkinter import ttk
# from visual_automata.fa.nfa import VisualNFA
# from Vending_Machine import VendingMachine
#
#
# def runGUI():
#     root = Tk()
#     root.geometry("600x500")
#     root.title("Vending Machine")
#
#     mylabel1 = Label(root, text="Vending Machine", font=('arial', 40, 'bold'))
#     mylabel1.grid(row=0, column=0, columnspan=3, padx=100, pady=50)
#
#     mylabel2 = Label(root, text="Insert money: ")
#     mylabel2.grid(row=1, column=0, padx=10, pady=10, sticky=E)
#
#     myinput1 = Entry(root, width=20) #amount = eltextbox
#     myinput1.grid(row=1, column=1, padx=10, pady=10)
#
#     mylabel3 = Label(root, text="Change: ")
#     mylabel3.grid(row=2, column=0, padx=10, pady=10, sticky=E)
#
#     myinput2 = Entry(root, width=20) #change=textbox2
#     myinput2.grid(row=2, column=1, padx=10, pady=10)
#
#     select_label = Label(root, text="Select an Item:")
#     select_label.grid(row=3, column=0, padx=10, pady=10)
#
#     mygroup = StringVar()
#     myoption1 = ttk.Radiobutton(root, text="Pepsi 10.00", variable=mygroup, value="check1")
#     myoption1.grid(row=4, column=0, padx=10, pady=10)
#
#     myoption2 = ttk.Radiobutton(root, text="Redbull 30.00", variable=mygroup, value="check2")
#     myoption2.grid(row=4, column=1, padx=10, pady=10)
#
#     myoption3 = ttk.Radiobutton(root, text="Sprite 10.00", variable=mygroup, value="check3")
#     myoption3.grid(row=4, column=2, padx=10, pady=10)
#
#     myoption4 = ttk.Radiobutton(root, text="Fanta 14.00", variable=mygroup, value="check4")
#     myoption4.grid(row=5, column=0, padx=10, pady=10)
#
#     myoption5 = ttk.Radiobutton(root, text="Sun Top 10.00", variable=mygroup, value="check5")
#     myoption5.grid(row=5, column=1, padx=10, pady=10)
#
#     myoption6 = ttk.Radiobutton(root, text="Protein Bar 50.00", variable=mygroup, value="check6")
#     myoption6.grid(row=5, column=2, padx=10, pady=10)
#
#     purchase_button = Button(root, text="Purchase", command=VendingMachine.make_selection)
#     purchase_button.grid(row=6, column=0, padx=10, pady=10)
#
#     refill_button = Button(root, text="Refill", command=VendingMachine.refill)
#     refill_button.grid(row=6, column=1, padx=10, pady=10)
#
#     cancel_button = Button(root, text="Cancel",command=VendingMachine.cancel)
#     cancel_button.grid(row=6, column=2, padx=10, pady=10)
#
#
#
#     root.mainloop()
