import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantApp:
    def __init__ (self, root):
        self.root = root
        root.title("Restaurant Order")
        root.geometry("500x450")
        root.configure(bg="light blue")

        self.menu = {
            "Fries Meal": 2,
            "Lunch Meal": 2,
            "Burger Meal": 3,
            "Pizza Meal" : 4,
            "Cheese Burger": 2.5,
            "Drinks": 1
        }

        self.entries = {}

        tk.Label(
            root,
            text="Restaurant Order Managment",
            font=("Arial", 18, "bold"),
            bg = "#E8F4F8",
            fg = "black"


        ).pack(pady=20)

        frame = tk.Frame(root, bg = "White", padx = 20, pady=15)
        frame.pack()

        for i, (item,price) in enumerate(self.menu.items()):
            tk.Label(
                frame,
                text=f"{item} - ${price}",
                font=("Arial", 11),
                bg = "white"
            
            ).grid(row = i, column=0, padx=10, pady = 6)

            entry = tk.Entry(frame, width=5)
            entry.grid(row=i, column=1, padx=10)

            self.entries[item] = entry

        tk.Button(
            root,
            text="Place Order",
            command=self.place_order,
            bg="#2E86C1",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=8
        ).pack(pady=20)

    def place_order(self):
        total = 0
        order = "Order Summary:\n\n"

        for item, entry in self.entries.items():
            if entry.get().isdigit():
                quantity = int(entry.get())

                if quantity > 0:
                    price = self.menu[item]
                    cost = quantity * price
                    total += cost

                    order += f"{item}: {quantity} x ${price} = ${cost}\n"

        if total > 0:
            order += f"\nTotal Cost: ${total}"
            messagebox.showinfo("Order Placed", order)
        else:
            messagebox.showerror(
                "Error",
                "Please order at least one item."
            )


root = tk.Tk()
RestaurantApp(root)
root.mainloop()