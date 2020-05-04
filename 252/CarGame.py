#Using the while function to use a command multiple times
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started stoooopid")
        else:
            started = True
            print("Car Started...! ")
    elif command == "stop":
        if not started:
            print("Car is already stopped dummy")
        else:
            started = False
            print("Car Stopped! ")
    elif command == "help":
        print("""
start - to start the car
stop - to stop car
help - to show commands
quit - to quit
""")
    elif command == "quit":
        break
else:
    print("Sorry I don't understand that! ")