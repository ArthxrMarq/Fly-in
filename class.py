from enum import Enum

class ZoneType(Enum):
    NORMAL = "normal"
    RESTRICTED = "restricted"
    BLOCKED = "blocked"
    PRIORITY = "priority"

    def movement_cost(self) -> int:
        if self == ZoneType.NORMAL:
            return 1
        elif self == ZoneType.RESTRICTED:
            return 2
        elif self == ZoneType.BLOCKED:
            raise BlockedException
        elif self == ZoneType.PRIORITY:
            return 1
        return 0
    
    def is_blocked(self) -> bool:
        return self == ZoneType.BLOCKED:

    def is_priority(self) -> bool:
        return self == ZoneType.PRIORITY:


class ZoneRole(Enum):
    START = "start"
    END = "end"
    REGULAR = "regular"


class FlyInError(Exception):
    pass


class ZoneNotFoundError(FlyInError):
    pass


class Zone:
    def __init__(self, x: int, y: int, name: str, zone_type: ZoneType, zone_role: ZoneRole, color: str | None  = None, max_drones: int = 1) -> None:
        self.name = name
        self.coords: tuple[int,int] = (x,y)
        self.zone_type = zone_type
        self.color = color
        self.max_drones = max_drones
        self.role = zone_role


class Connection:
    def __init__(self, zone_a: Zone, zone_b: Zone, capacity: int = 1) -> None:
        self.zone_a = zone_a
        self.zone_b = zone_b
        self.max_link_capacity = capacity


class Graph:
    def __init__(self) -> None:
        self.zones: dict[str, Zone] = {}
        self.connections: list[Connection] = []

    def get_zone(self, name: str) -> Zone:
        if name in self.zones:
            return self.zones[name]
        raise ZoneNotFoundError("A Zona especificada não existe")


    def add_zone(self, zone : Zone) -> :
        if name in self.zones:
            return None:
        zone = Zone()

    def add_connection(self, connection : Connection) -> :


        
