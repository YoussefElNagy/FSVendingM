import time
# from main import runGUI
class VendingMachine:
    # defining the states
    IDLE_STATE = "Idle"
    WAITING_STATE = "Waiting"
    GETTINGCHANGE_STATE = "Getting Change"
    DISPENSING_STATE = "Dispensing"



    # defining the valid transitions
    VALID_TRANSITIONS = {
        IDLE_STATE: [WAITING_STATE, IDLE_STATE],
        WAITING_STATE: [GETTINGCHANGE_STATE, DISPENSING_STATE, WAITING_STATE],
        GETTINGCHANGE_STATE: [IDLE_STATE],
        DISPENSING_STATE: [GETTINGCHANGE_STATE, IDLE_STATE]
    }

    # money inputs
    VALID_AMOUNTS = {
        "5$": 5,
        "10$": 10,
        "20$": 20,
        "50$": 50,
        "100$": 100,

    }

    def __init__(self):

        self.state = self.IDLE_STATE
        self.items = {}
        self.balance = 0

    def transition(self, new_state):  # will check if a transition is valid, then make the transition

        # state is the same: valid transition, no need for print statement
        if self.state == new_state:
            return True

        # valid transition
        if new_state in self.VALID_TRANSITIONS[self.state]:
            self.state = new_state

            print("State switched to " + new_state + "\n")
            return True

        # invalid transition
        else:
            print("Invalid transition: " + self.state + " to " + new_state)
            return False

    def refill(self):  # will restore original quantities of all items

        if not self.transition(self.IDLE_STATE):
            return

        self.items = {

            "Pepsi": {
                "price": 10.00,
                "quantity": 6
            },

            "Redbull": {
                "price": 30.00,
                "quantity": 5
            },

            "Sprite": {
                "price": 10.00,
                "quantity": 5
            },

            "Fanta": {
                "price": 14.00,
                "quantity": 2
            },

            "Sun Top": {
                "price": 10.00,
                "quantity": 10
            },

            "Protein Bar": {
                "price": 50.00,
                "quantity": 6
            }

        }

        print("Machine refilled.")
        time.sleep(1)

    def insert_amount(self,coin):  # user inserts coin into machine
        if not self.transition(self.WAITING_STATE):
            return

            # processing coin input
        # while True:
        #     try:
                # coin = input("Please insert money into the machine (5$, 10$, 20$, 50$, 100$).") #eltextbox

            # except:
            #     print("Please insert a valid coin.")
            #     continue

        if coin not in self.VALID_AMOUNTS:
            print("Please insert a valid coin.")
            # continue

        else:
            self.balance += self.VALID_AMOUNTS[coin]
            # break

        print("Coin inserted. Your balance is " + str(self.balance) + "$")


    def make_selection(self,selected_item):
        # user selects item from machine

        # checking if user has inserted money
        if self.state != self.WAITING_STATE:

            print("Invalid transition: You must insert money before making a selection.")
            self.transition(self.IDLE_STATE)
            return

        self.show_items()

        # processing item input

        #selected_item = str(input("Please enter the name of your selected item."))  #elradiobutton

        if selected_item not in self.items:
            print("Please select a valid item.")


        price = self.items[selected_item]['price']
        quantity = self.items[selected_item]['quantity']

        if self.balance < price:

            print("You have not inserted enough coins to purchase this item. \
                This item costs " + str(price) + "$ ,You have inserted " + str(self.balance) + "$")
            return

        if quantity == 0:
            print("Please select an item that is in stock.")
            return
        # dispensing item and getting change
        self.dispense(selected_item)
        time.sleep(1)
        self.process_change(selected_item)

    def calc_change(self, selected_item):  # calculates change amount based on price of item and current balance
        # if selected_item == None:
        #     return self.balance

        price = self.items[selected_item]['price']
        if self.balance < price:
            return self.balance

        return self.balance - price

    def process_change(self, selected_item):  # gives change, resets balance
        change_amount = self.calc_change(selected_item)

        if not self.transition(self.GETTINGCHANGE_STATE):
            return

        if change_amount != 0:
            print("A total of" + str(change_amount) + "$ in change...")
            self.balance = 0
            time.sleep(1)

        print("Your transaction is complete.")
        self.transition(self.IDLE_STATE)


    def dispense(self, selected_item):  # gives item to user, updates count of items in machine
        if not self.transition(self.DISPENSING_STATE):
            return

        time.sleep(1)
        print("Purchasing "+selected_item+"...")
        self.items[selected_item]['quantity'] -= 1

    def show_items(self):  # displaying the menu of items in the machine
        print("--------------------\nCurrent Selection:")

        for item, info in self.items.items():
            #print("{} | Price: {}, Quantity: {}".format(item, info['price'], info['quantity']))
            print(item+" Price: " + str(info['price']) + ", Quantity: " + str(info['quantity']))


    def cancel(self):
        my_change=0
        # cancels transaction, gets any money in machine
        if self.balance != 0:
            if not self.transition(self.GETTINGCHANGE_STATE):
                return

            time.sleep(1)
            print("Returned " + str(self.balance) + " dollars.")
            # my_change = self.balance ############
            self.balance = 0
        else:
            print("No money to return.")
        time.sleep(1)

        self.transition(self.IDLE_STATE)


