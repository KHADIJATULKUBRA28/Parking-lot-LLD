"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Getter;
import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.util.HashMap;
import java.util.Map;

@Getter
public class ParkingFloor {
    private final String id;
    private final Map<String, ParkingSpot> spots = new HashMap<>();

    public ParkingFloor(String id) { this.id = id; }

    public void addSpot(ParkingSpot spot) {
        spots.put(spot.getId(), spot);
    }

    public ParkingSpot findAvailableSpot(VehicleType vehicleType) {
        for (ParkingSpot spot : spots.values()) {
            if (spot.getAllowedType() == vehicleType && spot.tryOccupy()) {
                return spot;
            }
        }
        return null;
    }
}"""
from typing import Dict, Optional

from enums.VehicleType import VehicleType
from model.ParkingSpot import ParkingSpot


class ParkingFloor:
    def __init__(self, id: str):
        self._id = id
        self._spots: Dict[str, ParkingSpot] = {}

    def getId(self) -> str:
        return self._id

    def getSpots(self) -> Dict[str, ParkingSpot]:
        return self._spots

    def addSpot(self, spot: ParkingSpot) -> None:
        self._spots[spot.getId()] = spot

    def findAvailableSpot(self, vehicleType: VehicleType) -> Optional[ParkingSpot]:
        for spot in list(self._spots.values()):
            if spot.getAllowedType() == vehicleType and spot.tryOccupy():
                return spot
        return None
