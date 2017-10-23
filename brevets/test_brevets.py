"""
Nose tests for brevet calculator
"""

from acp_times import open_time
from acp_times import close_time

import nose
import arrow
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

# ADD: Add more test cases, edge cases in particular

def test_open_time():
    assert open_time(100, 200, "2017-01-01 00:00") == "2017-01-01 02:56" # Normal case under 200
    assert open_time(0, 200, "2017-01-01 00:00") == "2017-01-01 00:00" # Minimum
    #assert open_time(305, 300, "2017-01-01 00:00") == "2017-01-01 09:00" # Case just over 300
    #assert open_time(335, 300, "2017-01-01 00:00") == "2017-01-01 09:00" # Case over 300 + 10%
    assert open_time(1005, 1000, "2017-01-01 00:00") == "2017-01-02 09:05" # Maximum
    assert open_time(1200, 1000, "2017-01-01 00:00") == "2017-01-02 09:05" # Over maximum

def test_close_time():
    assert close_time(100, 200, "2017-01-01 00:00") == "2017-01-01 06:40" # Normal case under 200
    assert close_time(0, 200, "2017-01-01 00:00") == "2017-01-01 01:00" # Testing for 1 hour after
    assert close_time(305, 300, "2017-01-01 00:00") == "2017-01-01 20:00" # Case just over 300
    assert close_time(335, 300, "2017-01-01 00:00") == "2017-01-01 20:00" # Case over 300 + 10% 
    assert close_time(1005, 1000, "2017-01-01 00:00") == "2017-01-04 03:00" # Maximum
    assert close_time(1200, 1000, "2017-01-01 00:00") == "2017-01-04 03:00" # Over maximum