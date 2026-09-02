# test_fleet_report.py
from fleet_report import fleet_summary

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]


def test_summary_counts_due_cars():
    # Only VOS-4471 is nearly worn (~99.3%), so exactly one car is due.
    assert fleet_summary(SAMPLE)["due"] == 1


def test_summary_does_not_crash_on_missing_reading():
    """fleet_summary must not raise KeyError when a car has no last_service_km."""
    fleet_with_gap = [
        {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
        {"id": "VOS-7788", "odometer": 92000},   # no last_service_km
    ]
    result = fleet_summary(fleet_with_gap)   # must not raise
    assert "average_wear" in result
    assert result["count"] == 2
