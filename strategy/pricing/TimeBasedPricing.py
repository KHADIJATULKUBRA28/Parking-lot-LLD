'''
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;

public class TimeBasedPricing implements PricingStrategy {
    // Peak period hours (e.g., 8:00 to 17:00)
    private static final LocalTime PEAK_START = LocalTime.of(8, 0);
    private static final LocalTime PEAK_END = LocalTime.of(17, 0);

    private boolean isPeak(LocalTime time) {
        return !time.isBefore(PEAK_START) && !time.isAfter(PEAK_END);
    }

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        if (exitTime.isBefore(entryTime)) throw new IllegalArgumentException("Exit time before entry time");

        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long totalHours = (long) Math.ceil(durationMinutes / 60.0);

        // Count peak hours and non-peak hours by iterating hour by hour
        int peakHours = 0;
        int nonPeakHours = 0;

        LocalDateTime cursor = entryTime.truncatedTo(ChronoUnit.HOURS);
        // If entry time has minutes, consider first hour partially occupied, count as 1 hour anyway (already rounded)
        for (int i = 0; i < totalHours; i++) {
            LocalTime hourStart = cursor.toLocalTime();
            if (isPeak(hourStart)) peakHours++;
            else nonPeakHours++;
            cursor = cursor.plusHours(1);
        }

        double peakRate = switch (type) {
            case CAR -> 30.0;
            case BIKE -> 15.0;
            case TRUCK -> 50.0;
        };

        double nonPeakRate = switch (type) {
            case CAR -> 20.0;
            case BIKE -> 10.0;
            case TRUCK -> 30.0;
        };

        return peakHours * peakRate + nonPeakHours * nonPeakRate;
    }
}
'''
import math

from strategy.pricing.PricingStrategy import PricingStrategy


class TimeBasedPricing(PricingStrategy):
    """Slab pricing: first 2 hours at 10/hr, next 3 at 15/hr, rest at 20/hr."""

    SLABS = [(2, 10), (3, 15)]
    DEFAULT_RATE = 20

    def calculate_price(self, duration_hours):
        remaining = math.ceil(duration_hours)
        total = 0

        for slab_hours, rate in self.SLABS:
            hours = min(remaining, slab_hours)
            total += hours * rate
            remaining -= hours
            if remaining <= 0:
                return total

        return total + remaining * self.DEFAULT_RATE
