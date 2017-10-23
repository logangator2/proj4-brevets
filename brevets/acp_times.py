"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math
import logging

#  Keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.

min_list = [(0, 15), (200, 15), (400, 15), (600, 11.428), (1000, (40/3))]
max_list = [(200, 34), (400, 32), (600, 30), (1000, 28), (1300, 26)]
# Defult times for closing are in minutes for algorithmic consistency in open_time and close_time
default_times = [(200, 810), (300, 1200), (400, 1620), (600, 2400), (1000, 4500)]

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       A date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    brevet_dist_km = float(brevet_dist_km)
    working_cdk = control_dist_km
    working_total_time = 0
    for maxkm, maxspd in max_list:
      if control_dist_km < maxkm:
        total_time = working_total_time + time_calc(working_cdk, maxspd)
        c_open = arrow.get(str(brevet_start_time)) # Make brevet_start_time into an arrow object
        c_open = c_open.shift(minutes=total_time) # Shifting brevet distance by control time difference
        return str(c_open.format('YYYY-MM-DD HH:mm'))
      else:
        working_total_time += time_calc(maxkm, maxspd) # Minutes of this section, dictated by current maxkm and maxspd
        working_cdk = control_dist_km - maxkm

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       A date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    brevet_dist_km = float(brevet_dist_km)
    ten_percent = (brevet_dist_km * 0.1)
    # Case when control is 100%-110% of brevet
    if control_dist_km < (brevet_dist_km + ten_percent) and control_dist_km >= brevet_dist_km:
      for dist, max_time in default_times:
        if dist == brevet_dist_km:
          b_end = arrow.get(str(brevet_start_time)) # Make brevet_start_time into an arrow object
          b_end = b_end.shift(minutes=max_time)
          return str(b_end.format('YYYY-MM-DD HH:mm'))

    # Case where control is < brevet
    else:
      working_cdk = control_dist_km
      working_total_time = 0
      for minkm, minspd in min_list:
        if control_dist_km < minkm:
          total_time = working_total_time + time_calc(working_cdk, minspd)
          c_close = arrow.get(str(brevet_start_time)) # Make brevet_start_time into an arrow object
          c_close = c_close.shift(minutes=total_time) # Shifting brevet distance by control time difference
          return str(c_close.format('YYYY-MM-DD HH:mm'))
        if control_dist_km == minkm:
          c_close = arrow.get(str(brevet_start_time)).shift(minutes=60)
          return str(c_close.format('YYYY-MM-DD HH:mm'))
        else:
          working_total_time += time_calc(minkm, minspd) # Minutes of this section, dictated by current maxkm and maxspd
          working_cdk = control_dist_km - minkm

def time_calc(distance, speed):
  """
  Args:
    distance: entered control distance
    speed: entered min/max speed
  Returns:
    time: total minutes elapsed since brevet start time
  """
  dec = (distance / speed)
  hours = int(math.floor(dec))
  hrs_in_minutes = hours * 60
  minutes = round(((dec - hours) * 60))
  time = hrs_in_minutes + minutes
  return time