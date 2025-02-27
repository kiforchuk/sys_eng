# ttp = total thermal power (in MWt)
# epo = electric power output (in MWe)

class ReactorSystem:
    def __init__(self):
        self.epo = 1000
        self.state = False
        self._range_ttp = range(2500, 3300)
        self.current_ttp = 10

    def shutdown(self):
        assert self.state, 'Reactor already shut down'
        self.state = False

    def enable(self):
        assert not self.state, 'Reactor already enabled'
        self.state = True


class HeatTransferSystem:
    def __init__(self):
        pass


class ElectricPowerSystem:
    def __init__(self):
        pass


class AtmosphereCleanupSystem:
    def __init__(self):
        pass


class ProtectionSystem:
    def __init__(self):
        pass


class EmergencyPowerSupplySystem(ProtectionSystem):
    def __init__(self):
        super().__init__()


class RadiationMonitorSystem:
    def __init__(self):
        super().__init__()


class CoolingSystem:
    def __init__(self, water_volume):
        self.state = True
        self._water_volume_range = range(75000, 190001)
        self._waste_heat_range = range(1500, 2301)
        assert water_volume in self._water_volume_range, f'Invalid water volume {water_volume}, must be between 75000 and 190000 m3'
        self.current_water_volume = water_volume

    def pump_water(self, volume: int):
        new_water_volume = self.current_water_volume + volume
        assert new_water_volume in self._water_volume_range, 'Max water volume exceeded'
        self.current_water_volume = new_water_volume

    def discharge_water(self, volume: int):
        new_water_volume = self.current_water_volume - volume
        assert new_water_volume in self._water_volume_range, 'Min water volume exceeded'
        self.current_water_volume = new_water_volume

    def breakdown(self):
        assert self.state, 'Cooling system already broken'
        self.state = False


class EmergencyCoolingSystem:
    def __init__(self):
        self.state = False

    def enable(self):
        assert not self.state, 'Emergency cooling system already enabled'
        self.state = True

    def disable(self):
        assert self.state, 'Emergency cooling system already disabled'
        self.state = False


class NPP:
    def __init__(self, water_volume):
        self.reactor = ReactorSystem()
        self.cooler = CoolingSystem(water_volume)
        self.power = ElectricPowerSystem()
        self.atmosphere_cleanup = AtmosphereCleanupSystem()
        self.emergency_cooling = EmergencyCoolingSystem()

    def enable(self):
        self.reactor.enable()

    def disable(self):
        self.reactor.shutdown()

    def cooler_breakdown(self):
        self.cooler.breakdown()
        self.emergency_cooling.enable()


npp = NPP(90000)
npp.enable()
npp.disable()
npp.cooler_breakdown()
npp.cooler_breakdown()
