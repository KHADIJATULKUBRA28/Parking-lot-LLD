"""
package org.nailyourinterview.lld.parking_lot.factory;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;
import org.nailyourinterview.lld.parking_lot.model.*;

public class VehicleFactory {
    public static Vehicle create(String number, VehicleType type) {
        return switch (type) {
            case CAR -> new Car(number);
            case BIKE -> new Bike(number);
            case TRUCK -> new Truck(number);
        };
    }
}
"""
from enums.VehicleType import VehicleType
from model.Vehicle import Vehicle
from model.Car import Car
from model.Bike import Bike
from model.Truck import Truck


class VehicleFactory:
    @staticmethod
    def create(number: str, type: VehicleType) -> Vehicle:
        if type == VehicleType.CAR:
            return Car(number)
        elif type == VehicleType.BIKE:
            return Bike(number)
        elif type == VehicleType.TRUCK:
            return Truck(number)
        raise ValueError(f"Unsupported vehicle type: {type}")
