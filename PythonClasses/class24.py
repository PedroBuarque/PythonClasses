"""
CONSTANT = "Variables" that will not change
Too many conditions on the same if (bad thing, more complex to understand)
    <- complexity count (bad thing, if you have too much blocks of code inside of other block of code)
"""

car_speed = 60 #current speed of the car
car_location = 101 #place where the car is current located on the road

RADAR_1 = 60 #Maximum speed of the radar 1
LOCATION_1 = 100 #Location of the radar 1
RADAR_RANGE = 1 #The distance where the radar can reach

car_speed_higher_than_radar1_limit = car_speed > RADAR_1
car_on_radar1_range = car_location >= (LOCATION_1 - RADAR_RANGE) or car_location <= (LOCATION_1 - RADAR_RANGE)
car_got_ticket = car_speed_higher_than_radar1_limit and car_on_radar1_range

if car_speed_higher_than_radar1_limit:
        print('Car speed is higher than the speed limit from radar')

if car_on_radar1_range:
    print('Car passed through the radar range')

if car_got_ticket:
    print(f'Car speed was higher than the speed limit, you got a ticket')


