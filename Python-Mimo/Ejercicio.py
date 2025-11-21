#Pedir el nivel de bateria 
def show_battery_color(level):
    if level <= 10:
        print("Color: red")
    elif level <= 20:
        print("Color: yellow")
    else:
        print("Color: green")

level = float(input("Ingrese el level battery: "))
show_battery_color(level)