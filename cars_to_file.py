
# Define a dictionary to store liked cars with their manufacturer

cars = {
    "CT5-V BLACKWING" : "Cadillac",
    "GR86": "Toyota",
    "Defender 110": "Land Rover"
}

# Function to display and write liked cars to a file
def write_cars_to_file(cars, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Favorite Cars: \n")
        for model, manufacturer in cars.items():
            file.write(f"{model} - manufacturer: {manufacturer}\n")


# Write liked cars to a .txt file
cars["M5"] = "BMW"
write_cars_to_file(cars, 'cars.txt')