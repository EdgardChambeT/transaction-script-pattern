class Reservation:
    def __init__(self, guest_name, date):
        self.guest_name = guest_name
        self.date = date
        self.status = "Pending"

    def confirm(self):
        self.status = "Confirmed"
        return f"Reservation confirmed for {self.guest_name} on {self.date}"

    def cancel(self):
        self.status = "Cancelled"
        return f"Reservation cancelled for {self.guest_name} on {self.date}"


class ReservationScript:
    def create_reservation(self, guest_name, date):
        reservation = Reservation(guest_name, date)
        return reservation

    def confirm_reservation(self, reservation):
        if reservation.status == "Pending":
            return reservation.confirm()
        return f"Cannot confirm. Current status: {reservation.status}"

    def cancel_reservation(self, reservation):
        if reservation.status == "Pending":
            return reservation.cancel()
        return f"Cannot cancel. Current status: {reservation.status}"
