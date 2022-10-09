from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests
import yfinance as yf
import matplotlib.pyplot as plt
import tkinter.messagebox
from functools import partial
from datetime import date

api_key = "21XTTGBDL2CBO627"
base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
Currency_List = ["INR", "USD", "EUR", "RUB", "AUD", "ARS", "EGP", "GBP", "SGD", "TRY", "BTC"]
Stock_ticker_list = ["AAPL", "GOOG", "AMZN", "RS", "IBM", "CAJ", "HMC", "TCS", "MSFT", "FB", "BABA", "JNJ", "INTC", "F", "INFY", "TSLA"]

# UI
root = Tk()
root.geometry("500x500")
root.title("Currency Converter")

# Convert Function
def Convert():
    from_currency = Currency_1.get()
    to_currency = Currency_2.get()
    amount = Amount_1.get()
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    response = requests.get(main_url)
    result = response.json()
    currency_dict = result["Realtime Currency Exchange Rate"]
    roe = currency_dict["5. Exchange Rate"]
    final_result = float(float(amount)*float(roe))
    tkinter.messagebox.showinfo("Answer", str(amount) + " " + from_currency + " is equivalent to " + str(round(final_result,4)) + " " + to_currency)


# Reset Function
def Reset():
    Currency_1.set("USD")
    Currency_2.set("INR")
    Amount_1.delete(0, 'end')

# Plot graph
def Graph(ticker,number):
    print(ticker.get())
    data=yf.download(ticker.get(), "2018-01-01", date.today())
    print(date.today())
    plt.xlabel("Date")
    if(number==1):
        data.Close.plot()
        plt.title("Closing Price Graph ("+ ticker.get() +")")
        plt.ylabel("Closing Price")
    elif(number==2):
        data.Open.plot()
        plt.title("Opening Price Graph("+ ticker.get() +")")
        plt.ylabel("Opening Price")
    elif(number==3):
        data.Volume.plot()
        plt.title("Volume Graph("+ ticker.get() +")")
        plt.ylabel("Volume")

    plt.show()

#Stock Graph Window
def stock_window():
    child_root = Tk()
    child_root.geometry("800x800")
    child_root.title("Stock Tracker")
    mini = Label(child_root, text="STOCK TRACKER", font=("Garamond", "22", "bold"), fg="blue", borderwidth=8, relief=RAISED, padx=30, pady=30)
    mini.pack(pady=30)
    ticker = StringVar(child_root)
    ticker.set("AAPL")
    ticker_drop = OptionMenu(child_root, ticker, *Stock_ticker_list)
    ticker_drop.pack(pady=10)
    close_graph = Button(child_root, text="Show Closing Price Graph", relief=RAISED, width=30, command=partial(Graph,ticker,1))
    close_graph.pack(pady=10)
    open_graph = Button(child_root, text="Show Opening Price Graph", relief=RAISED, width=30, command=partial(Graph,ticker,2))
    open_graph.pack(pady=10)
    volume_graph = Button(child_root, text="Show Volume Graph", relief=RAISED, width=30, command=partial(Graph,ticker,3))
    volume_graph.pack(pady=10)
    stock_quit=Button(child_root, text="Quit", relief=RAISED, width=30, command=child_root.quit)
    stock_quit.pack(pady=10)

# Heading
intro_label = Label(root, text="CURRENCY CONVERTER", font=("Garamond", "22","bold"), relief=RAISED, fg="green", borderwidth=5, padx=30, pady=20)
intro_label.pack(pady=30)

# Dropdown Box 1
Currency_1 = StringVar(root)
Currency_1.set("USD")
drop_1 = OptionMenu(root, Currency_1, *Currency_List)
drop_1.pack(pady=7)

# Dropdown Box 2
Currency_2 = StringVar(root)
Currency_2.set("INR")
drop_2 = OptionMenu(root, Currency_2, *Currency_List)
drop_2.pack(pady=7)

# Entry Box 1
amount_label = Label(root, text="Enter Amount:", font=("Times New Roman", "12", "bold"))
amount_label.pack()
Amount_1 = Entry(root, width=25)
Amount_1.pack(pady=7)

# Convert Button
convert_button = Button(root, text="Convert", relief=RAISED, width=10, command=Convert)
convert_button.pack(pady=7)

# Reset Button
reset_button = Button(root, text="Reset", relief=RAISED, width=10, command=Reset)
reset_button.pack(pady=7)

# Quit Button
quit_button = Button(root, text="Quit", relief=RAISED, width=10, command=root.quit)
quit_button.pack(pady=7)

# Stock Button
stock_button = Button(root, text="Stock Tracker",relief=RAISED, width=10, command=stock_window)
stock_button.pack(pady=7)

root.mainloop()