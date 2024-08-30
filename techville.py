# Helper functions
def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

# Main navigation function
def navigate(destination):
    start_engine()
    
    # Ask the user for their desired destination
    print(f"Navigating to {destination}...")
    
    if destination == "library":
        move_forward()
        turn("left")
        print("Arrived at the library.")
    elif destination == "tech park":
        move_forward()
        turn("right")
        print("Arrived at the tech park.")
    elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
        move_forward()
        print("Entering the roundabout...")
        
        if destination == "hospital":
            follow_roundabout(1)
            print("Arrived at the hospital.")
        elif destination == "mall":
            follow_roundabout(2)
            move_forward()
            turn("right")
            print("Arrived at the mall.")
        elif destination == "airport":
            follow_roundabout(3)
            print("Arrived at the airport.")
        elif destination in ["university", "stadium"]:
            follow_roundabout(4)
            move_forward()
            if destination == "university":
                turn("left")
                print("Arrived at the university.")
            elif destination == "stadium":
                turn("right")
                print("Arrived at the stadium.")
    else:
        print("Error: Destination not recognized.")
    
    stop_engine()

# Example usage
if __name__ == "__main__":
    # You can replace 'mall' with any other destination to test
    navigate("mall")
