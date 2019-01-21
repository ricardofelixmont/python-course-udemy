from typing import List
"""
Flight Leg:

GLA -> LHR -> CAN

2 segments (GLA -> LHR, LHR -> CAN)
"""

class Segment:
    def __init__(self, departure, destination):
        self.departure = departure    # GLA
        self.destination = destination  # LHR


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments


    def __repr__(self):
        """
        return: string in the format of GLA -> LHR -> CAN
        """
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return '->'.join(stops)


    @property
    def departure_point(self) -> str:   # Se eu tentar fazer isso: flight.departure_point = 'EDI' não vou conseguir, pois departure_point é um método,
                                        # para poder fazer isso precisamos criar um setter com o decorator abaixo(pode ter qualquer nome, porém é
                                        # mais comum colocar o nome do método que queremos fazer o setter.
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):   # agora posso fazer: flight.departure_point = 'EDI'
        # self.segments[0].departure = val
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)



flight = Flight([Segment('GLA', 'LHR')])
print(flight)

flight.departure_point = 'EDI'
print(flight)

