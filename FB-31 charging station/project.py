class PowerSupplySystem:
    def __init__(self, voltage: int):
        self._voltage_range = range(190, 231)
        self._default_power_consumption = 50
        self._power_consumption_range = range(self._default_power_consumption, 301)
        assert voltage in self._voltage_range, f'Invalid voltage {voltage}, must be in range 190 and 230'
        self.voltage = voltage
        self.state = False
        self.current_power_consumption = 0

    def increase_power_consumption(self, amount: int):
        new_power_consumption = self.current_power_consumption + amount
        assert new_power_consumption in self._power_consumption_range, f'Invalid power consumption {new_power_consumption}'
        self.current_power_consumption = new_power_consumption

    def decrease_power_consumption(self, amount: int):
        new_power_consumption = self.current_power_consumption - amount
        assert new_power_consumption in self._power_consumption_range, f'Invalid power consumption {new_power_consumption}'
        self.current_power_consumption = new_power_consumption

    def enable(self):
        assert not self.state, 'Power supply is already enabled'
        self.state = True
        self.current_power_consumption = self._default_power_consumption

    def disable(self):
        assert self.state, 'Power supply is already disabled'
        self.state = False
        self.current_power_consumption = 0


class PowerStorageSystem:
    def __init__(self, battery_level: int):
        self.battery_level = battery_level

    def charge_battery(self):
        self.battery_level += 1

    def drain_battery(self):
        self.battery_level -= 1


class InverterSystem:
    def __init__(self):
        pass


class ProtectionSystem:
    def __init__(self):
        pass


class CoolingSystem:
    def __init__(self):
        pass


class ChargingUnitSystem:
    def __init__(self):
        pass


class SoftwareSystem:
    def __init__(self):
        pass


class Device:
    def __init__(self, name, battery_level, power_consumption):
        self.name = name
        self.battery_level = battery_level
        self.power_consumption = power_consumption


class PortableChargingStation:
    def __init__(self, battery_level, voltage, max_devices_count):
        self.power_supply = PowerSupplySystem(voltage)
        self.power_storage = PowerStorageSystem(battery_level)
        self.connected_devices = []
        self.max_devices_count = max_devices_count
        self.state = False

    def plug_in(self):
        self.power_supply.enable()

    def unplug_in(self):
        self.power_supply.disable()

    def on(self):
        assert not self.state, 'Already on'
        self.state = True

    def off(self):
        assert self.state, 'Already off'
        self.state = False

    def __charge_device(self, device):
        if self.state:
            if self.power_supply.state:
                self.power_supply.increase_power_consumption(device.power_consumption)
            else:
                self.power_storage.drain_battery()
            device.battery_level += 1

    def connect_device(self, device):
        new_count = len(self.connected_devices) + 1
        assert new_count <= self.max_devices_count, f'Max devices connected'
        self.connected_devices.append(device)
        self.__charge_device(device)

    def __discharge_device(self, device):
        self.power_supply.decrease_power_consumption(device.power_consumption)

    def disconnect_device(self, device):
        devices_names = [device.name for device in self.connected_devices]
        assert device.name in devices_names, f'Device {device} is not connected'
        self.connected_devices = [
            existing_device
            for existing_device in self.connected_devices
            if existing_device.name != device.name
        ]


ecoflow = PortableChargingStation(
    battery_level=85,
    voltage=220,
    max_devices_count=1
)
iphone_14 = Device('iphone 14', battery_level=22, power_consumption=20)
ecoflow.plug_in()
ecoflow.on()

print(ecoflow.power_supply.current_power_consumption)
ecoflow.connect_device(iphone_14)
print(ecoflow.power_supply.current_power_consumption)
print(ecoflow.power_storage.battery_level)
print(iphone_14.battery_level)


