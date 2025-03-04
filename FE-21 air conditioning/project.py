import random


ABNORMAL_PRESSURE_MSG = 'Incorrect refrigerant state: abnormal pressure {}'
ABNORMAL_TEMP_MSG = 'Incorrect refrigerant state: abnormal temperature {}'
FAILED_COMPRESSION_PRESSURE = 'Compression failed: abnormal pressure {}'
FAILED_COMPRESSION_TEMP = 'Compression failed: abnormal temperature {}'


class RefrigerationSystem:
    def __init__(self):
        self.state = False
        self.refrigerant_state = 'gas'
        self._evaporator_pressure_range = range(90, 121)
        self._condenser_pressure_range = range(320, 401)
        self._evaporator_temperature_range = range(-10, 6)
        self._condenser_temperature_range = range(40, 61)
        self.refrigerant_temperature = random.randint(-10, 6)
        self.refrigerant_pressure = random.randint(90, 121)


    def enable(self):
        assert not self.state, 'Refrigeration system is already enabled'
        self.state = True

    def disable(self):
        assert self.state, 'Refrigeration system is already disabled'
        self.state = False

    def evaporate(self, temp_change: int):
        self.refrigerant_temperature += temp_change
        self.refrigerant_state = 'liquid'

    def compress(self, input_pressure, input_temperature):
        #assert input_pressure in self._evaporator_pressure_range, ABNORMAL_PRESSURE_MSG.format(input_pressure)
        #assert input_temperature in self._evaporator_temperature_range, ABNORMAL_TEMP_MSG.format(input_temperature)

        pressure_increase = random.randint(210, 330)
        temp_increase = random.randint(35, 70)

        new_refrigerant_pressure = input_pressure + pressure_increase
        #assert new_refrigerant_pressure in self._condenser_pressure_range, FAILED_COMPRESSION_PRESSURE.format(new_refrigerant_pressure)
        self.refrigerant_pressure = new_refrigerant_pressure

        new_refrigerant_temperature = input_temperature + temp_increase
        #assert new_refrigerant_temperature in self._condenser_temperature_range, FAILED_COMPRESSION_TEMP.format(new_refrigerant_temperature)
        self.refrigerant_temperature = new_refrigerant_temperature

    def condense(self):
        pass

    def expansion(self):
        pass

    def work_cycle(self, indoor_temperature: int, desired_temperature: int):
        temp_diff = indoor_temperature - desired_temperature
        while temp_diff > 0:
            self.evaporate(1)
            #self.compress(self.refrigerant_pressure, self.refrigerant_temperature)
            self.condense()
            self.expansion()
            temp_diff -= 1


class AirDistributionSystem:
    def __init__(self):
        pass


class ControlSystem:
    def __init__(self):
        pass


class FiltrationSystem:
    def __init__(self):
        pass


class HeatingSystem:
    def __init__(self):
        pass


class VentilationSystem:
    def __init__(self):
        pass


class AirConditioning:
    def __init__(self):
        self.refrigeration = RefrigerationSystem()

    def on(self, indoor_temperature: int, desired_temperature: int):
        self.refrigeration.enable()
        self.refrigeration.work_cycle(indoor_temperature, desired_temperature)

    def off(self):
        self.refrigeration.disable()

    def start_work(self):
        pass


air_conditioning = AirConditioning()
print(f'start temp: {air_conditioning.refrigeration.refrigerant_temperature}')

air_conditioning.on(25, 22)
print(air_conditioning.refrigeration.refrigerant_temperature)
# air_conditioning.off()
# air_conditioning.on()
# air_conditioning.off()
# air_conditioning.off()

