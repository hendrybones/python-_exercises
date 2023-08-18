population={"china:": 143,"india": 136,"pakistan": 32,"usa ": 32}
def add():
    country = input("Enter country name to add: ")
    country = country.lower()

    if country in population:
        print("Country already exists in our dataset. Terminating.")
        return

    p = input(f"Enter population for {country}: ")
    p = float(p)

    population[country] = p  # Adds new key value pair to dictionary
    print_all()
def remove():
    country = input("Enter country name to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f" {country}==>{p}")

def main():
    option=input("Enter the operation(add,query,print,remove)")
    if option.lower()== "add":
        add()
    elif option.lower() == "query":
        query()
    elif option.lower() =="print":
        print_all()
    elif option.lower() =='remove':
        remove()
if __name__=="__main__":
    main()