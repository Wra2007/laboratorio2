class Resipiente:
    def __init__(self,tamaño,color,capacidad): # corrected method name to __init__
        self.tamaño = tamaño
        self.color = color
        self.capacidad = capacidad
        # self.arrancado = false
        
pocillo = Resipiente("mediano", "blanco", "100ml")
plato = Resipiente("grande" , "blanco" , "150ml")

print(type(pocillo))
print(type(plato))

print(pocillo.tamaño, pocillo.color , pocillo.capacidad)
print(plato.tamaño, plato.color, plato.capacidad)



      




