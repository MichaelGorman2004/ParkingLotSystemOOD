# Parking Lot System

## Overview

This project implements a simple Parking Lot System using Object-Oriented Design principles in Python. The system simulates a multi-story parking lot that can accommodate different types of vehicles in various types of parking spots.

## Features

- Support for multiple types of vehicles (Motorcycle, Car, Truck)
- Different sizes of parking spots (Compact, Regular, Large)
- Multiple floors in the parking lot
- Automated ticket generation upon parking
- Fee calculation based on parking duration and vehicle type

## Classes

1. `VehicleType`: Enum for different types of vehicles
2. `ParkingSpotType`: Enum for different types of parking spots
3. `Vehicle`: Represents a vehicle with a license plate and type
4. `ParkingSpot`: Represents a single parking spot
5. `ParkingFloor`: Represents a floor in the parking lot with multiple spots
6. `ParkingLot`: Main class that manages the entire parking lot system
7. `Ticket`: Represents a parking ticket

## How to Use

1. Create a `ParkingLot` instance
2. Add `ParkingFloor`(s) to the parking lot
3. Add `ParkingSpot`(s) to each floor
4. Use `park_vehicle()` method to park a vehicle
5. Use `remove_vehicle()` method to remove a vehicle and get the parking fee

## Example Usage

```python
# Create a parking lot
parking_lot = ParkingLot()

# Create a floor
floor1 = ParkingFloor(1)

# Add parking spots to the floor
floor1.add_spot(ParkingSpot(1, ParkingSpotType.COMPACT))
floor1.add_spot(ParkingSpot(2, ParkingSpotType.REGULAR))
floor1.add_spot(ParkingSpot(3, ParkingSpotType.LARGE))

# Add the floor to the parking lot
parking_lot.add_floor(floor1)

# Create a vehicle
car = Vehicle("ABC123", VehicleType.CAR)

# Park the vehicle
if parking_lot.park_vehicle(car):
    print(f"Car with license plate {car.license_plate} parked successfully")
else:
    print("Parking failed")

# Remove the vehicle (and calculate fee)
fee = parking_lot.remove_vehicle("ABC123")
print(f"Parking fee: ${fee:.2f}")
```

## Future Enhancements

1. Implement a user interface (CLI or GUI)
2. Add persistence (database integration)
3. Implement more complex fee structures (e.g., hourly rates, daily maximums)
4. Add support for reservations
5. Implement a display system for available spots

## Contributing

Contributions to improve the system are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
