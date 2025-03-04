import random


class EngineSystem:
    def __init__(self):
        self.state = False

    def on(self):
        assert not self.state, 'Engine is already on'
        self.state = True

    def off(self):
        assert self.state, 'Engine is already off'
        self.state = False


class FuelSystem:
    def __init__(self):
        self._capacity_range = range(200)
        self.current_fuel_level = random.randint(10, 30)

    def calculate_fuel_change(self, speed):
        # TODO: output msg "No fuel"
        self.change_fuel_level(-speed*0.6)

    def change_fuel_level(self, diff_amount: float):
        new_fuel_level = self.current_fuel_level + diff_amount
        assert new_fuel_level in self._capacity_range, 'Invalid fuel level'
        self.current_fuel_level = new_fuel_level


class TransmissionSystem:
    def __init__(self):
        self.flow_rate = 0
        self.flow_direction = 1
        self.current_speed = 0
        self._speed_range = range(51)

    def change_flow_direction(self, new_direction):
        assert self.flow_direction * new_direction != 1, 'This direction already used'
        self.flow_direction = new_direction

    def change_flow_rate(self, new_speed):
        self.flow_rate = new_speed * 4

    def set_current_speed(self, new_speed):
        assert new_speed in self._speed_range, 'This speed is out of range'
        self.current_speed = new_speed
        self.change_flow_rate(new_speed)


class HydraulicSystem:
    def __init__(self):
        pass


class ElectricalSystem:
    def __init__(self):
        pass


class SteeringSystem:
    def __init__(self):
        self.current_angle = 0
        self._angle_range = range(-360, 361)

    def change_angle(self, angle_diff):
        new_angle = self.current_angle + angle_diff
        if new_angle > 360 or new_angle < -360:
            self.current_angle = -360 if new_angle < 0 else 360
            print('Impossible to turn steering more')
        else:
            self.current_angle = new_angle


class CoolingSystem:
    def __init__(self):
        pass


class Tractor:
    def __init__(self):
        self.engine = EngineSystem()
        self.steering = SteeringSystem()
        self.transmission = TransmissionSystem()
        self.fuel = FuelSystem()

    def _check_engine(self):
        assert self.engine.state, 'Engine is off'

    def enable(self):
        self.engine.on()
        self.fuel.change_fuel_level(-3)

    def disable(self):
        self.engine.off()

    def move(self, direction: str):
        # TODO: change initial speed when tractor start moving
        self._check_engine()
        directions = {
            'forward': 1,
            'backward': -1,
        }
        try:
            direction_int = directions[direction]
            self.transmission.change_flow_direction(direction_int)
        except KeyError:
            print('Invalid direction')

    def turn(self, angle: int):
        self.steering.change_angle(angle)

    def set_speed(self, speed: int):
        self._check_engine()
        self.transmission.set_current_speed(speed)
        self.fuel.calculate_fuel_change(speed)

    def refuel(self, litres_amount):
        self.fuel.change_fuel_level(litres_amount)


tractor = Tractor()
tractor.enable()
tractor.enable()

print(tractor.fuel.current_fuel_level)
tractor.set_speed(40)
print(tractor.fuel.current_fuel_level)

