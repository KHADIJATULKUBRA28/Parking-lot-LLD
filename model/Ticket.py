"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Builder;
import lombok.Data;
import org.nailyourinterview.lld.parking_lot.enums.PaymentStatus;

import java.time.LocalDateTime;

@Data
@Builder
public class Ticket {
    private String ticketId;
    private LocalDateTime entryTime;
    private Vehicle vehicle;
    private String floorId;
    private String spotId;
    private PaymentStatus paymentStatus = PaymentStatus.PENDING;
}
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from enums.PaymentStatus import PaymentStatus
from model.Vehicle import Vehicle


@dataclass
class Ticket:
    ticketId: Optional[str] = None
    entryTime: Optional[datetime] = None
    vehicle: Optional[Vehicle] = None
    floorId: Optional[str] = None
    spotId: Optional[str] = None
    paymentStatus: PaymentStatus = PaymentStatus.PENDING

    def getTicketId(self) -> str:
        return self.ticketId

    def setTicketId(self, ticketId: str) -> None:
        self.ticketId = ticketId

    def getEntryTime(self) -> datetime:
        return self.entryTime

    def setEntryTime(self, entryTime: datetime) -> None:
        self.entryTime = entryTime

    def getVehicle(self) -> Vehicle:
        return self.vehicle

    def setVehicle(self, vehicle: Vehicle) -> None:
        self.vehicle = vehicle

    def getFloorId(self) -> str:
        return self.floorId

    def setFloorId(self, floorId: str) -> None:
        self.floorId = floorId

    def getSpotId(self) -> str:
        return self.spotId

    def setSpotId(self, spotId: str) -> None:
        self.spotId = spotId

    def getPaymentStatus(self) -> PaymentStatus:
        return self.paymentStatus

    def setPaymentStatus(self, paymentStatus: PaymentStatus) -> None:
        self.paymentStatus = paymentStatus
