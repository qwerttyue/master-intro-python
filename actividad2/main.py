
from entidades.cliente import Cliente
from entidades.cuenta import Cuenta

from generar_infomes import print_cliente, print_cuenta


cuenta1 = Cuenta("0001", -5.25, 500.19, .0)
cuenta2 = Cuenta("0002", 10254.25, 222.45, .0)
cuenta3 = Cuenta("0003", 122.25, 20.25, 145.85)
cuenta4 = Cuenta("0004", 332.05, 251.04, .0)
cuenta5 = Cuenta("0005", 5454.19, 2251.04, 3510.44)
cuenta6 = Cuenta("0006", -164.01, 211.15, 200.00)
cuenta7 = Cuenta("0007", 15456.25, 1554.24, 2200.52)
cuenta8 = Cuenta("0008", 1245.47, 24.44, 500.00)
cuenta9 = Cuenta("0009", 15164.23, .0, 4200.92)
cuenta10 = Cuenta("0010", 4226.25, 25251.26, .0)
cuenta11 = Cuenta("0011", 14242.25, 656.74, 2520.14)
cuenta12 = Cuenta("0012", 2546.25, 1215.08, 1200.82)
cuenta13 = Cuenta("0013", 2425.26, 1250.04, .0)

cliente1 = Cliente("0001", "Juan", "Garcia", 38, [cuenta1, cuenta2])
cliente2 = Cliente("0002", "Laura", "Jimenez", 13, [cuenta3])
cliente3 = Cliente("0003", "Pedro", "Rodriguez", 17, [cuenta4])
cliente4 = Cliente("0004", "Andres", "Gomez", 56, [cuenta5, cuenta6])
cliente5 = Cliente("0005", "Gema", "Sanchez", 89, [cuenta7])
cliente6 = Cliente("0006", "Ana", "Jimenez", 16, [cuenta8])
cliente7 = Cliente("0007", "Jesus", "Perez", 55, [cuenta9, cuenta10])
cliente8 = Cliente("0008", "Jose", "Garcia", 26, [cuenta11])
cliente9 = Cliente("0009", "Angel", "Perez", 24, [cuenta12])
cliente10 = Cliente("00010", "Maria", "Gomez", 21, [cuenta13])

print_cliente(cliente1)
print_cuenta(cuenta1)
