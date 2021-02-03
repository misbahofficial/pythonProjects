"""
This is a very simple Car game Engine without any kind of GUI and complex system.
This is a beginner friendly small project to demonstrate the learnings.

This Game Engine is Created by Misbah Ahmed

"""


#for comparing user input
command = ""

#to avoid starting or stopping a car twice
started = False

#for running the loop untill user input quit
while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop -  to stop the car
help - for help
quit - for exit
        """)
    elif command == "quit":
        break #for immediately exit the loop
    else:
        print("Sorry, Invalid command")