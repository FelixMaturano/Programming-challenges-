
#FUNTIONS
#------------------

# modificando el valor de la variable local 
def add_to_saving(amount):
    total_saving = 70
    total_saving = 80
    print(f"Savings: {total_saving + amount}")

add_to_saving(20)


def has_red(rgb_values):
    if rgb_values[0] > 0:
        print("Red is in the mix!")
rgb = [153, 255, 51]
has_red(rgb)

def change_battery_color(level):
    if level <= 10:
        print("Color: red")
    elif level <= 20:
        print("Color: yellow")
    else:
        print("Color: green")

change_battery_color(15)


def show_notifications(message):
    for i in range (message):
        print(f"notificar{i}")

show_notifications(3)
