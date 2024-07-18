class CuentaBancaria:
    
    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance
                
    def generar_balance(self):
        print(self.balance)

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto

mi_cuenta = CuentaBancaria("105-356-643", "Nora Smith", 5600)

mi_cuenta.generar_balance() # Nora tiene 5600 en su sueldo
mi_cuenta.depositar(400) # Nora deposita unos 400 y ahora tiene 6000
mi_cuenta.generar_balance() # Nota tiene 6000 en su sueldo

