import random


class User:
    def __init__(self, name, microphone):
        self.name = name
        self.microphone = microphone

    def on(self):
        ...

    def off(self):
        ...

    def connect(self):
        ...

    def disconnect(self):
        ...

    def input_sound(self):
        ...


# class System:
#     def __init__(self):
#         self.state = False
#
#     def switch_state(self, state: bool):
#         self.state = state


class PowerSupplySystem:
    def __init__(self, voltage: int):
        assert voltage in range(12, 48), f'Invalid value: {voltage}, must be between 12 and 48'
        self.voltage = voltage
        self.power_consumption = 0
        self.state = False
        self._consumption_range = range(48, 481)
        self._default_consumption = 200

    def switch_state(self, new_state: bool):
        assert self.state != new_state, f'Already switched to {new_state}'

        self.state = new_state
        if self.state:
            self.power_consumption = self._default_consumption
        else:
            self.power_consumption = 0

    def increase_consumption(self, amount: int):
        new_consumption = self.power_consumption + amount
        assert new_consumption in self._consumption_range, 'Max consumption exceeded'
        self.power_consumption = new_consumption

    def decrease_consumption(self, amount: int):
        new_consumption = self.power_consumption - amount
        assert new_consumption in self._consumption_range, 'Min consumption exceeded'
        self.power_consumption = new_consumption


class LightSystem:
    def __init__(self):
        self.state = False
        self._colors_choice = ('red', 'green', 'blue')
        self.current_color = random.choice(self._colors_choice)
        self.brightness_level = 0
        self._default_brightness_level = 50
        self._brightness_range = range(101)

    def switch_state(self, new_state: bool):
        assert self.state != new_state, f'Already switched to {new_state}'
        self.state = new_state
        if self.state:
            self.brightness_level = self._default_brightness_level
        else:
            self.brightness_level = 0

    def switch_color(self, new_color: str):
        assert new_color in self._colors_choice, f'Invalid value: {new_color}, must be one of {self._colors_choice}'
        self.current_color = new_color

    def increase_brightness(self, amount: int):
        new_brightness = self.brightness_level + amount
        assert new_brightness in self._brightness_range, 'Max brightness exceeded'
        self.brightness_level = new_brightness

    def decrease_brightness(self, amount: int):
        new_brightness = self.brightness_level - amount
        assert new_brightness in self._brightness_range, 'Min brightness exceeded'
        self.brightness_level = new_brightness


class SoundCatchSystem:
    def __init__(self):
        self.state = False
        self.phrase = ''

    def switch_state(self, new_state: bool):
        assert self.state != new_state, f'Already switched to {new_state}'
        self.state = new_state

    def catch_phrase(self, phrase: str):
        self.phrase = phrase


class OutputSystem:
    def __init__(self):
        self.state = False
        self.output_signal = ''
        self._signal_codes = '^_><*$'

    def switch_state(self, new_state: bool):
        assert self.state != new_state, f'Already switched to {new_state}'

    def process_input(self, phrase: str):
        for _ in phrase:
            self.output_signal += random.choice(self._signal_codes)

    def transmit_input(self):
        print(self.output_signal)


class Microphone:
    def __init__(self, voltage: int):
        self.power_supply = PowerSupplySystem(voltage=voltage)
        self.light_system = LightSystem()
        self.sound_catch = SoundCatchSystem()
        self.output_system = OutputSystem()

    def on(self):
        self.power_supply.switch_state(True)
        self.sound_catch.switch_state(True)
        self.output_system.switch_state(True)

    def off(self):
        self.power_supply.switch_state(False)

    def on_light(self):
        self.light_system.switch_state(True)
        self.power_supply.increase_consumption(10)

    def off_light(self):
        self.light_system.switch_state(False)
        self.power_supply.decrease_consumption(10)

    def switch_light_color(self, new_color: str):
        self.light_system.switch_color(new_color)

    def increase_brightness(self, amount: int):
        self.light_system.increase_brightness(amount)

    def decrease_brightness(self, amount: int):
        self.light_system.decrease_brightness(amount)

    def speak(self, phrase: str):
        self.sound_catch.catch_phrase(phrase)
        self.power_supply.increase_consumption(random.randint(1, 11))
        self.output_system.process_input(self.sound_catch.phrase)


microphone = Microphone(voltage=20)
microphone.on()
microphone.speak('Hello World!')
microphone.output_system.transmit_input()

