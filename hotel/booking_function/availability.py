
from hotel.models import Booking,Room
def check_availabilty(room, check_in, check_out):
    avail_list = []
    booking_list = booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)