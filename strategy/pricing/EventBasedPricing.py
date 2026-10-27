'''
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.Map;

public class EventBasedPricing implements PricingStrategy {
    // Event pricing: Higher per-hour rates
    private static final Map<VehicleType, Double> EVENT_HOURLY_RATES = Map.of(
            VehicleType.CAR, 50.0,
            VehicleType.BIKE, 30.0,
            VehicleType.TRUCK, 70.0
    );

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long hours = (long) Math.ceil(durationMinutes / 60.0); // always round up to next hour

        double ratePerHour = EVENT_HOURLY_RATES.getOrDefault(type, 0.0);
        return ratePerHour * hours;
    }
}
'''
import math

from strategy.pricing.PricingStrategy import PricingStrategy


class EventBasedPricing(PricingStrategy):
    """Flat event rate of 20 per started hour."""

    RATE_PER_HOUR = 20

    def calculate_price(self, duration_hours):
        return math.ceil(duration_hours) * self.RATE_PER_HOUR
