from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3
    
class ParkingSpotType(Enum):
    COMPACT = 1
    REGULAR = 2
    LARGE = 3
    
class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: ParkingSpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def is_free(self):
        return self.vehicle is None

    def park(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def unpark(self) -> Vehicle:
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

class ParkingFloor:
    def __init__(self, floor_id: int):
        self.floor_id = floor_id
        self.parking_spots = []

    def add_spot(self, spot: ParkingSpot):
        self.parking_spots.append(spot)

    def find_available_spot(self, vehicle_type: VehicleType) -> ParkingSpot:
        for spot in self.parking_spots:
            if spot.is_free() and spot.spot_type.value >= vehicle_type.value:
                return spot
        return None

class ParkingLot:
    def __init__(self):
        self.floors = []
        self.tickets = {}

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle.vehicle_type)
            if spot:
                spot.park(vehicle)
                ticket = Ticket(vehicle, spot, datetime.now())
                self.tickets[vehicle.license_plate] = ticket
                return True
        return False

    def remove_vehicle(self, license_plate: str) -> float:
        if license_plate not in self.tickets:
            raise ValueError(f"No ticket found for license plate: {license_plate}")

        ticket = self.tickets[license_plate]
        spot = ticket.parking_spot
        spot.unpark()
        del self.tickets[license_plate]
        parking_duration = datetime.now() - ticket.issue_time
        return self.calculate_fee(parking_duration, ticket.vehicle.vehicle_type)

    @staticmethod
    def calculate_fee(duration: timedelta, vehicle_type: VehicleType) -> float:
        hours = duration.total_seconds() # add this in for real use -> `/ 3600`
        base_rate = 6.0 # 6 dollars an hour
        if vehicle_type == VehicleType.MOTORCYCLE:
            return base_rate * hours
        elif vehicle_type == VehicleType.CAR:
            return 1.5 * base_rate * hours
        else:
            return 2.0 * base_rate * hours


class Ticket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot, issue_time: datetime):
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.issue_time = issue_time


# Testing software out
parking_lot = ParkingLot()

floor1 = ParkingFloor(1)
floor1.add_spot(ParkingSpot(1, ParkingSpotType.COMPACT))
floor1.add_spot(ParkingSpot(2, ParkingSpotType.REGULAR))
floor1.add_spot(ParkingSpot(3, ParkingSpotType.LARGE))

parking_lot.add_floor(floor1)

car = Vehicle("ABC123", VehicleType.CAR)
if parking_lot.park_vehicle(car):
    print(f"Car with license plate {car.license_plate} parked successfully")
else:
    print("Parking failed")

import time
time.sleep(4)

fee = parking_lot.remove_vehicle("ABC123")
print(f"Parking fee: ${fee:.2f}")
