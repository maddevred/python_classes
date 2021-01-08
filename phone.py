class Phone:
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.phone_number}"

    def call(self, other_number):
        print (f"Calling number: {other_number}")     

    def text(self, other_number, message):
        print(f'Sending text to {other_number}')
        print(message)

    def open_app(self, app_name):
        print(f"Opening {app_name}")


class iPhone(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50 

    def __str__(self):
        return f"iPhone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode 

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery > 100:    
            self.battery = 100

    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}") 

amari_phone = iPhone('404-604-0791', 'red')

amari_phone.view_battery_life()
amari_phone.charge_phone(40)
amari_phone.view_battery_life()
amari_phone.view_phone_number()

amari_phone.call('678-769-9825')
amari_phone.open_app('Zoom')