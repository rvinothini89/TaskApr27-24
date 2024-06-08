class TV:
    def __init__(self,brand,price,inches):
        self.brand = brand
        self.price = price
        self.inches = inches
        #Channel should be 1 by default. Volume should be 50 by default.
        self.channel = 1
        self.volume = 50
        #Tv will be off by default
        self.onOffStat = False
    def increaseVolume(self,volume):
            self.volume = volume
            #Volume can't never be below 0 or above 100
            if self.volume < 100: 
                self.volume += 1
    def decreaseVolume(self,volume):
            self.volume = volume
            #Volume can't never be below 0 or above 100
            if self.volume > 0: 
                self.volume -= 1
    def channelChange(self,channel):
        #TV has only 50 channels
        if  1 <= channel <= 50:
            self.channel = channel
    # reset TV so it goes back to channel 1 and volume 50
    def resetTV(self):
         self.channel = 1
         self.volume =  50  
    def switchTv(self):
         self.onOffStat = True 
    #  TV status like: "Panasonic at channel 8, volume 75
    def displayStatus(self):
        power_status = "on" if self.onOffStat else "off"
        return f"{self.brand} at channel {self.channel}, volume {self.volume}, {power_status}"
#Inherit a TV class add additional properties like screen thickness etc., 
class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 'Wide'
        self.backlight = 'LED'

    def displayStatus(self):
        details = (
            f"Brand: {self.brand}\n"
            f"Screen Thickness: {self.screen_thickness} inches\n"
            f"Energy Usage: {self.energy_usage} kWh\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
            f"Viewing Angle: {self.viewing_angle}\n"
            f"Backlight: {self.backlight}\n"
            f"Channel: {self.channel}\n"
            f"Volume: {self.volume}"
        )
        print(details)

class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 'Standard'
        self.backlight = 'Plasma'

    def displayStatus(self):
        details = (
            f"Brand: {self.brand}\n"
            f"Screen Thickness: {self.screen_thickness} inches\n"
            f"Energy Usage: {self.energy_usage} kWh\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
            f"Viewing Angle: {self.viewing_angle}\n"
            f"Backlight: {self.backlight}\n"
            f"Channel: {self.channel}\n"
            f"Volume: {self.volume}"
        )
        print(details)

# Example usage
tv = TV('Panasonic', 500, 42)
tv.switchTv()
tv.increaseVolume(74)
tv.channelChange(8)
print(tv.displayStatus())
tv.resetTV()
print(tv.displayStatus())

led_tv = LedTV('Samsung', 700, 55, 1.2, 100, 60000, 120)
led_tv.displayStatus()

plasma_tv = PlasmaTV('LG', 800, 60, 1.5, 200, 50000, 60)
plasma_tv.displayStatus()