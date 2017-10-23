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
    assert open_time(100, 200, "2017-01-01 00:00") == "2017-01-01 02:56"
    assert open_time(0, 200, "2017-01-01 00:00") == "2017-01-01 00:00"
    assert open_time(305, 300, "2017-01-01 00:00") == "2017-01-01 09:00"

def test_close_time():
    assert close_time(100, 200, "2017-01-01 00:00") == "2017-01-01 06:40"
    assert close_time(0, 200, "2017-01-01 00:00") == "2017-01-01 01:00"
    assert close_time(305, 300, "2017-01-01 00:00") == "2017-01-01 20:00"