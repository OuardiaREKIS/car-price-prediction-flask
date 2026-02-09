# List of known car brands used for extraction
BRANDS = [
    "Maruti", "Hyundai", "Honda", "Mahindra", "Mercedes-Benz",
    "Tata", "Toyota", "BMW", "Renault", "Audi", "Ford",
    "Volkswagen", "Skoda", "Chevrolet", "Kia", "Nissan",
    "MG", "Land Rover", "Jeep", "Volvo", "Jaguar", "Datsun",
    "Fiat", "Mini", "Lexus", "Porsche", "Mitsubishi",
    "Maserati", "Isuzu", "Force", "Bentley", "Premier"
]
# Identify the brand by checking the beginning of the car name
def extract_brand(car_name: str) -> str:
    for brand in BRANDS:
        if car_name.startswith(brand):
            return brand
    # Assign 'Other' if no known brand is found
    return "Other"