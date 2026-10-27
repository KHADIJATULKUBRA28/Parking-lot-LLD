"""
package org.nailyourinterview.lld.parking_lot.model;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

public class Truck extends Vehicle {
    public Truck(String number) { super(number, VehicleType.TRUCK); }
}"""
from enums.VehicleType import VehicleType
from model.Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.TRUCK)
