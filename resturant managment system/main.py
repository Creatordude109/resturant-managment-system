import tkinter as tk
from tkinter import ttk,messagebox

class ResturantOrderManagment:
    def __init__(self,root):
        self.root=root
        self.root.title("Resturant management app")
        self.menu_items={
            "fries meal":2,
            "lunch meal":2,
            "burger meal":3,
            "pizza meal":4,
            "cheese burger":2.5,
            "drinks":1
        }
        self.exchange_rate=82
        self.setup_background(root)

        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        ttk.Label(frame,text="resturant order management",font=("Arial",20)).grid(row=0,columnspan=2,pady=10,padx=10)
        self.menu_labels={}
        self.menu_quantities={}

        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item} (${price})")
            label.grid(row=i,column=0,pady=5,padx=10)
            self.menu_labels[item]=label

            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,pady=5,padx=10)
            self.menu_quantities[item]=quantity_entry

        self.currency_var=tk.StringVar()
        ttk.Label(frame,text="Select currency:").grid(row=len(self.menu_items)+1,column=0,pady=5,padx=10)

        currency_dropdown=ttk.Combobox(frame,textvariable=self.currency_var,values=["USD","INR"],state="readonly")
        currency_dropdown.grid(row=len(self.menu_items)+1,column=1,pady=5,padx=10)
        currency_dropdown.current(0)
        self.currency_var.trace("w",self.update_menu_prices)
        order_button=ttk.Button(frame,text="Place Order",command=self.place_order)
        order_button.grid(row=len(self.menu_items)+2,columnspan=3,pady=10,padx=10)


    def setup_background(self,root):
        bg_width,bg_height=800,600
        canvas=tk.Canvas(root,width=bg_width,height=bg_height)
        canvas.pack()

        orignal_bg=tk.PhotoImage(file="pexels-french-fries-1846083_p5a8vv.jpg")
        background_image=orignal_bg.subsample(int(orignal_bg.width()/bg_width),int(orignal_bg.height()/bg_height))

        canvas.create_image(0,0,image=background_image,anchor=tk.NW)
        canvas.image=background_image


    def update_menu_prices(self,*args):
        currency=self.currency_var.get()
        symbol="$" if currency=="USD" else "₹"
        rate=self.exchange_rate if currency=="INR" else 1

        for item,label in self.menu_labels.items():
            price=self.menu_items[item]*rate
            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        total_cost=0
        order_summary="order summary:\n"
        currency=self.currency_var.get()
        rate=self.exchange_rate if currency=="INR" else 1
        symbol="$" if currency=="USD" else "₹"

        for item,entry in self.menu_quantities.items():
            quantity=entry.get()
            if quantity.isddigit():
                quantity=int(quantity)
                price=self.menu_items[item]*rate
                cost=quantity*price
                total_cost+=cost

                if quantity>0:
                    order_summary+=f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"

        if total_cost>0:
            order_summary+=f"\ntotal cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Summary",order_summary)

        else:
            messagebox.showerror("No items selected","Please select at least one item to place an order.")
if __name__=="__main__":
    root=tk.Tk()
    app=ResturantOrderManagment(root)
    root.geometry("800x600")
    root.mainloop()



    
    