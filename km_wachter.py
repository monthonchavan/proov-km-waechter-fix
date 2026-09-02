# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.
# Written in 2013. Modernized 2024.

SERVICE_INTERVAL_KM: int = 15000
WARN_AT_PERCENT: int = 80


def wear_percent(km_since_service: float, interval: int) -> float:
    """Return how much of the service window has been used, as a percentage (0–100+).

    Uses true division so a car at 14,900 of 15,000 km correctly reads ~99.3 %
    instead of being floored to 0 % by integer division.
    """
    return (km_since_service / interval) * 100


def needs_service(car: dict) -> bool:
    """Return True if this car has reached the 80 % wear threshold.

    If the car has no last_service_km reading the wear cannot be calculated,
    so the car is NOT flagged (avoids false positives).
    """
    if "last_service_km" not in car:
        return False
    km_since = car["odometer"] - car["last_service_km"]
    return wear_percent(km_since, SERVICE_INTERVAL_KM) >= WARN_AT_PERCENT


def check_fleet(fleet: list[dict]) -> list[str]:
    """Flag every car in fleet that needs a service; return their ids."""
    flagged = []
    for car in fleet:
        if needs_service(car):
            flagged.append(car["id"])
            print(f"SERVICE DUE: {car['id']}")
    return flagged
