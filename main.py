import weather

while True:
    print("Menu")
    print("1 - Current Weather")
    print("2 - NOAA Weather Stream")
    print("0 - Quit")
    var = input(">")
    if var == "0":
        break
    if var == "1":
        weather.main()