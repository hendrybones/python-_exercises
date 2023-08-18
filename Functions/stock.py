import statistics
stocks={
    "info": [600,630,620],
    "ril" : [1430,1490,1567],
    "mtl" : [234,180,160]
}

def print_all():
    for stock, price_list in stocks.items():
        avg=statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg: ",round(avg,2))

def add():
    stock=input("Enter stock name")
    price = input("Enter price")
    price=float(price)
    if stock in stocks.items():
        stocks[stock].append(price)
    else:
        stocks[stock]=[price]
    print_all()
def remove():
    s=input("enter the stock to remove")
    s=s.lower()
    if s not in stocks.items():
        print("Stock does not exist")
        return


        print_all()

def main():
    option=input("Enter operation (print,add or amend,remove: ")
    if option == "print":
        print_all()
    elif option == "add":
        add()
    elif option =="remove":
        remove()
    else:
        print("unsupported operation")
if __name__ =="__main__":
    main()

