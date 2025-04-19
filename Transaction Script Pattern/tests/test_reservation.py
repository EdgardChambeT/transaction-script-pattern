import pytest
from reservation.scripts import ReservationScript

def test_create_reservation():
    script = ReservationScript()
    reservation = script.create_reservation("John Doe", "2025-04-13")
    assert reservation.guest_name == "John Doe"
    assert reservation.date == "2025-04-13"
    assert reservation.status == "Pending"
    print(f"Reservation created: {reservation.guest_name} for {reservation.date} with status {reservation.status}")

def test_confirm_reservation():
    script = ReservationScript()
    reservation = script.create_reservation("Jane Doe", "2025-04-14")
    script.confirm_reservation(reservation)
    assert reservation.status == "Confirmed"
    print(f"Reservation confirmed for {reservation.guest_name} on {reservation.date} with status {reservation.status}")

def test_cancel_reservation():
    script = ReservationScript()
    reservation = script.create_reservation("Mark", "2025-04-15")
    reservation.cancel()
    assert reservation.status == "Cancelled"
    print(f"Reservation cancelled for {reservation.guest_name} on {reservation.date} with status {reservation.status}")
