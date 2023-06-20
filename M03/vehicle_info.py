"""
Vehicle Info

Author: Charles Jones
Description: Receives vehicle info provided by the user and outputs this info, formatted nicely :)
"""

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type) # begin initialization through the Vehicle super class

        # set provided data for this Automobile
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        # Used statement continuation ('\') instead of triple quotes
        return f"Vehicle type: {self.vehicle_type}\n" \
               f"Year: {self.year}\n" \
               f"Make: {self.make}\n" \
               f"Model: {self.model}\n" \
               f"Number of doors: {self.doors}\n" \
               f"Type of roof: {self.roof}"

def main():

    while (vehicle_type := input("Enter a type of vehicle (options: car): ")) != "car":
        print("\tSorry, car is the only accepted vehicle type!")

    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")

    doors = ""
    while True:
        try:
            doors = int(input("Enter the number of doors (options: 2, 4): "))
            # Input was a valid integer
            if doors in (2,4):
                break
            else:
                raise(ValueError)
        except ValueError:
            print("\tNumber of doors must be 2 or 4!")

    while (roof := input("Enter the type of roof (options: solid, sunroof): ")) not in ("solid", "sunroof"):
        print("\tRoof must be solid or sunroof!")

    automobile = Automobile(vehicle_type, year, make, model, doors, roof)
    print(automobile)

# Call main only if the script was executed directly
if __name__ == "__main__":
    main()