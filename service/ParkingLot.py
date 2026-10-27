'''
package org.nailyourinterview.lld.parking_lot.service;

import lombok.Getter;
import lombok.Setter;
import org.nailyourinterview.lld.parking_lot.enums.PaymentMode;
import org.nailyourinterview.lld.parking_lot.enums.*;
import org.nailyourinterview.lld.parking_lot.factory.*;
import org.nailyourinterview.lld.parking_lot.model.*;
import org.nailyourinterview.lld.parking_lot.strategy.payment.*;
import org.nailyourinterview.lld.parking_lot.strategy.pricing.*;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@Getter
public class ParkingLot {
    private static final ParkingLot INSTANCE = new ParkingLot();

    private final Map<String, ParkingFloor> floors = new HashMap<>();
    private final Map<String, Ticket> activeTickets = new HashMap<>();
    @Setter
    private PricingStrategy pricingStrategy;

    private ParkingLot() {
        this.pricingStrategy = PricingStrategyFactory.get(PricingStrategyType.TIME_BASED);
    }

    public static ParkingLot getInstance() {
        return INSTANCE;
    }

    public void addFloor(ParkingFloor floor) {
        floors.put(floor.getId(), floor);
    }

    // b1, b2 (one spot)
    // car, bike

    public Ticket parkVehicle(Vehicle vehicle, LocalDateTime entryTime) {
        for (ParkingFloor floor : floors.values()) {
            ParkingSpot spot = floor.findAvailableSpot(vehicle.getType());

            if (spot != null) {
                // Successfully reserved the spot via atomic operation
                String ticketId = UUID.randomUUID().toString();
                Ticket ticket = Ticket.builder()
                        .ticketId(ticketId)
                        .entryTime(entryTime)
                        .vehicle(vehicle)
                        .floorId(floor.getId())
                        .spotId(spot.getId())
                        .build();

                activeTickets.put(ticketId, ticket);
                System.out.println("Vehicle parked. Ticket: " + ticketId);
                return ticket;
            }
        }

        System.out.println("No spot available for vehicle type: " + vehicle.getType());
        return null;
    }

    public void unparkVehicle(String ticketId, LocalDateTime exitTime, PaymentMode paymentMode) {
        Ticket ticket = activeTickets.get(ticketId);
        if (ticket == null) {
            System.out.println("Invalid ticket ID.");
            return;
        }

        double fee = pricingStrategy.calculateFee(
                ticket.getVehicle().getType(),
                ticket.getEntryTime(),
                exitTime
        );

        PaymentStrategy strategy = PaymentStrategyFactory.get(paymentMode);
        PaymentProcessor processor = new PaymentProcessor(strategy);
        boolean paid = processor.pay(ticket, fee);

        if (!paid) {
            System.out.println("Vehicle cannot exit. Payment unsuccessful.");
            return;
        }

        ParkingSpot spot = floors.get(ticket.getFloorId()).getSpots().get(ticket.getSpotId());
        spot.vacate();
        activeTickets.remove(ticketId);

        System.out.println("Vehicle exited. Fee charged: ₹" + fee);
    }

    public void printStatus() {
        floors.forEach((floorId, floor) -> {
            System.out.println("Floor: " + floorId);
            floor.getSpots().values().forEach(spot -> {
                System.out.println(" Spot " + spot.getId() + " [" + spot.getAllowedType() + "] - " + (spot.isOccupied() ? "Occupied" : "Free"));
            });
        });
    }
}
'''
import uuid
from datetime import datetime
from typing import Dict, Optional

from enums.PaymentMode import PaymentMode
from enums.PricingStrategyType import PricingStrategyType
from factory.PaymentStrategyFactory import PaymentStrategyFactory
from factory.PricingStrategyFactory import PricingStrategyFactory
from model.ParkingFloor import ParkingFloor
from model.Ticket import Ticket
from model.Vehicle import Vehicle
from service.PaymentProcessor import PaymentProcessor
from strategy.pricing.PricingStrategy import PricingStrategy


class ParkingLot:
    _INSTANCE: Optional["ParkingLot"] = None

    def __init__(self):
        self._floors: Dict[str, ParkingFloor] = {}
        self._activeTickets: Dict[str, Ticket] = {}
        self._pricingStrategy: PricingStrategy = PricingStrategyFactory.get(PricingStrategyType.TIME_BASED)

    @staticmethod
    def getInstance() -> "ParkingLot":
        return ParkingLot._INSTANCE

    def getFloors(self) -> Dict[str, ParkingFloor]:
        return self._floors

    def getActiveTickets(self) -> Dict[str, Ticket]:
        return self._activeTickets

    def getPricingStrategy(self) -> PricingStrategy:
        return self._pricingStrategy

    def setPricingStrategy(self, pricingStrategy: PricingStrategy) -> None:
        self._pricingStrategy = pricingStrategy

    def addFloor(self, floor: ParkingFloor) -> None:
        self._floors[floor.getId()] = floor

    # b1, b2 (one spot)
    # car, bike

    def parkVehicle(self, vehicle: Vehicle, entryTime: datetime) -> Optional[Ticket]:
        for floor in list(self._floors.values()):
            spot = floor.findAvailableSpot(vehicle.getType())

            if spot is not None:
                # Successfully reserved the spot via atomic operation
                ticketId = str(uuid.uuid4())
                ticket = Ticket(
                    ticketId=ticketId,
                    entryTime=entryTime,
                    vehicle=vehicle,
                    floorId=floor.getId(),
                    spotId=spot.getId(),
                )

                self._activeTickets[ticketId] = ticket
                print("Vehicle parked. Ticket: " + ticketId)
                return ticket

        print("No spot available for vehicle type: " + vehicle.getType().name)
        return None

    def unparkVehicle(self, ticketId: str, exitTime: datetime, paymentMode: PaymentMode) -> None:
        ticket = self._activeTickets.get(ticketId)
        if ticket is None:
            print("Invalid ticket ID.")
            return

        fee = self._pricingStrategy.calculateFee(
            ticket.getVehicle().getType(),
            ticket.getEntryTime(),
            exitTime,
        )

        strategy = PaymentStrategyFactory.get(paymentMode)
        processor = PaymentProcessor(strategy)
        paid = processor.pay(ticket, fee)

        if not paid:
            print("Vehicle cannot exit. Payment unsuccessful.")
            return

        spot = self._floors[ticket.getFloorId()].getSpots()[ticket.getSpotId()]
        spot.vacate()
        del self._activeTickets[ticketId]

        print("Vehicle exited. Fee charged: ₹" + str(fee))

    def printStatus(self) -> None:
        for floorId, floor in self._floors.items():
            print("Floor: " + floorId)
            for spot in floor.getSpots().values():
                print(" Spot " + spot.getId() + " [" + spot.getAllowedType().name + "] - "
                      + ("Occupied" if spot.isOccupied() else "Free"))


ParkingLot._INSTANCE = ParkingLot()