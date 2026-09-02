# fleet_utils.py
# Utility helpers for Vossberg Mobility fleet data.
# Originally a catch-all since 2013. Modernized 2024: dead code removed, wrong constant fixed.

KM_PER_MILE: float = 1.60934      # 1 mile = 1.60934 km
MILES_PER_KM: float = 1 / KM_PER_MILE   # ≈ 0.621371


def km_to_miles(km: float) -> float:
    """Convert a distance in kilometres to miles.

    Used by the nightly run for the UK partner report.
    """
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a float to one decimal place."""
    return f"{value:.1f}"
