from fan import Fan

# Test program
if __name__ == "__main__":
    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    print("Fan 1 - Speed:", fan1.get_speed(), ", Radius:", fan1.get_radius(), ", Color:", fan1.get_color(), ", On:", fan1.is_on())
    print("Fan 2 - Speed:", fan2.get_speed(), ", Radius:", fan2.get_radius(), ", Color:", fan2.get_color(), ", On:", fan2.is_on())