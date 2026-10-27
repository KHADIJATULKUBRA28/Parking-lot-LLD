"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.util.concurrent.atomic.AtomicBoolean;

@Getter
@Setter
@RequiredArgsConstructor
public class ParkingSpot {
    private final String id;
    private final VehicleType allowedType;

    private AtomicBoolean occupied = new AtomicBoolean(false);

    // t1 t2
    // false false
    // _     true
    // false


    public boolean tryOccupy() {
        return occupied.compareAndSet(false, true);
    }

    public void vacate() {
        occupied.set(false);
    }

    public boolean isOccupied() {
        return occupied.get();
    }
}"""
from threading import Lock

from enums.VehicleType import VehicleType


class AtomicBoolean:
    """Python equivalent of java.util.concurrent.atomic.AtomicBoolean."""

    def __init__(self, value: bool = False):
        self._value = value
        self._lock = Lock()

    def compareAndSet(self, expected: bool, new: bool) -> bool:
        with self._lock:
            if self._value == expected:
                self._value = new
                return True
            return False

    def set(self, value: bool) -> None:
        with self._lock:
            self._value = value

    def get(self) -> bool:
        with self._lock:
            return self._value


class ParkingSpot:
    def __init__(self, id: str, allowedType: VehicleType):
        self._id = id
        self._allowedType = allowedType
        self._occupied = AtomicBoolean(False)

    def getId(self) -> str:
        return self._id

    def getAllowedType(self) -> VehicleType:
        return self._allowedType

    def getOccupied(self) -> AtomicBoolean:
        return self._occupied

    def setOccupied(self, occupied: AtomicBoolean) -> None:
        self._occupied = occupied

    # t1 t2
    # false false
    # _     true
    # false

    def tryOccupy(self) -> bool:
        return self._occupied.compareAndSet(False, True)

    def vacate(self) -> None:
        self._occupied.set(False)

    def isOccupied(self) -> bool:
        return self._occupied.get()
