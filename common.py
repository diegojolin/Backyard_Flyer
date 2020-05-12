from enum import IntEnum

class States(IntEnum):
    MANUAL = 0
    ARMING = 1
    TAKEOFF = 2
    WAYPOINT = 3
    LANDING = 4
    DISARMING = 5


class LCoord(IntEnum):
    NORTH = 0,
    EAST = 1,
    DOWN = 2


class GCoord(IntEnum):
    LONGITUDE = 0,
    LATITUDE = 1,
    ALTITUDE = 2
