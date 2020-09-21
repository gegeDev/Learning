def get_order(order):
    output = [] 
    if "burger" in order:
        for i in range(order.count("burger")): output.append("Burger ")
    if "fries" in order:
        for i in range(order.count("fries")): output.append("Fries ")
    if "chicken" in order:
        for i in range(order.count("chicken")): output.append("Chicken ")
    if "pizza" in order:
        for i in range(order.count("pizza")): output.append("Pizza ")
    if "sandwich" in order:
        for i in range(order.count("sandwich")): output.append("Sandwich ")
    if "onionrings" in order:
        for i in range(order.count("onionrings")): output.append("Onionrings ")
    if "milkshake" in order:
        for i in range(order.count("milkshake")): output.append("Milkshake ")
    if "coke" in order:
        for i in range(order.count("coke")): output.append("Coke ")
    return "".join(i for i in output)[:-1]

def refactored(order):
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    clean_order = ''
    for i in menu:
        clean_order += (i.capitalize() + ' ') * order.count(i)
    return clean_order[:-1]
print(get_order("chickenburgerfriesdupa"))
