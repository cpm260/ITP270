# This is a sample Python script.

from decimal import Decimal

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_daily_sales_location ():
    daily_sales = str(input("Enter Location of Daily_Sales file: "))
    return daily_sales

def open_daily_sales ():
    daily_sales_location = "/home/drivebox/Documents/message.txt"
    prefix = 'daily_sales = \ ' + '\n"""'
    daily_sales = open(daily_sales_location, "r").read()
    return daily_sales[len(prefix)-1:]

def clean_daily_sales():
    daily_sales = open_daily_sales()
    run1 = daily_sales.replace(";,;", ":").replace("\n", "").replace('"""', '')
    run2 = run1.split(",")
    run3 = []
    for transaction in run2:
        run3.append(transaction.split(":"))

    transactions_clean = []
    for transaction in run3:
        transactions_clean.append(str(transaction).replace(" ",""))
    return transactions_clean

def build_customer_list(cleaned_sales):
    c = []
    for transaction in cleaned_sales:
        c.append(str(transaction.split(",")[0]).replace("[", "").replace("]", "").replace("'", ""))
    return c

def build_sales_list(cleaned_sales):
    s = []
    for transaction in cleaned_sales:
        s.append(str(transaction.split(",")[1]).replace("[", "").replace("]", "").replace("'", ""))
    return s

def build_threads_list(cleaned_sales):
    t = []
    for transaction in cleaned_sales:
        t.append(str(transaction.split(",")[2]).replace("[", "").replace("]", "").replace("'", ""))
    return t

def build_dates_list(cleaned_sales):
    d = []
    for transaction in cleaned_sales:
        d.append(str(transaction.split(",")[3]).replace("[", "").replace("]", "").replace("'", ""))
    return d

def print_total_sales(cleaned_sales):
    sales = build_sales_list(cleaned_sales)
    total_sales = 0
    tab = '\t'
    for sale in sales:
        total_sales += round(Decimal(float(sale.replace("$", ""))), 2)
    print(f"Total Sales:{tab}${total_sales}")


def count_color(color, thread_sold):
    count = 0
    thread_sold_split = []

    for thread in thread_sold:
        if "&" in thread:
            temp_array = thread.split("&")
            for t in temp_array:
                thread_sold_split.append(t)
        else:
            thread_sold_split.append(thread)
    for thread in thread_sold_split:
        if str(thread) == str(color):
            count += 1
    return int(count)

def print_color_count(cleaned_sales):
    thread_sold = build_threads_list(cleaned_sales)
    tab = '\t'
    colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']
    print("Colors Sold Today:")
    for color in colors:
        count = count_color(color, thread_sold)
        print(f"{tab}{color}: {count}")

def print_daily_report(cleaned_sales):
    customers = build_customer_list(cleaned_sales)
    sales = build_sales_list(cleaned_sales)
    thread_sold = build_threads_list(cleaned_sales)
    date_sold = build_dates_list(cleaned_sales)
    newline = '\n'
    tab = '\t'

    print(f"Daily Sales Report: {date_sold[0]}")
    for i in range(len(customers) - 1):
        print(f"{tab}{sales[i]}{tab}{customers[i]}:")
        if "&" in thread_sold[i]:
            temp_array = thread_sold[i].split("&")
            for t in temp_array:
                print(f"{tab*2}{t}")
        else:
            print(f"{tab*2}{thread_sold[i]}")
        i += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cleaned_sales = clean_daily_sales()
    print_total_sales(cleaned_sales)
    print_daily_report(cleaned_sales)
    print_color_count(cleaned_sales)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/