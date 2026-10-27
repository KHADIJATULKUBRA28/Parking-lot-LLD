"""
package org.nailyourinterview.lld.parking_lot.model;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

public class Bike extends Vehicle {
    public Bike(String number) { super(number, VehicleType.BIKE); }
}
"""
from enums.VehicleType import VehicleType
from model.Vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.BIKE)
