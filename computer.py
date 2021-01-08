class Computer():
    def __init__(OS, processor, color):
        self.OS = OS
        self.processor = processor
        self.color = color

    def __str__(self):
        return {self.OS, self.processor, self.color} 

    def operating_system(self):
       print('Ubuntu')

    def intel_core(self):
        print('i56300U')

    def fav_color(self):
        print('black')

computer1 = Computer('Ubuntu', 'i56300U', 'black')

computer1.OS()
computer1.0S()
computer1.operating_system()
computer1.intel_core()
computer1.fav_color()
