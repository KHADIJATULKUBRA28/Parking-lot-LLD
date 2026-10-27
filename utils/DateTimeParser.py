"""
package org.nailyourinterview.lld.parking_lot.utils;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class DateTimeParser {
    public static LocalDateTime parse(String input) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d MMM h:mm a yyyy", Locale.ENGLISH);
        return LocalDateTime.parse(input, formatter);
    }
}
"""
from datetime import datetime


class DateTimeParser:
    @staticmethod
    def parse(input: str) -> datetime:
        # Java pattern: "d MMM h:mm a yyyy"
        return datetime.strptime(input, "%d %b %I:%M %p %Y")