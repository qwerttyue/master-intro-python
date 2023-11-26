

from entidades.cliente import Cliente
from entidades.cuenta import Cuenta


def print_cliente(c: Cliente):
    print(f"Cliente(id_cliente={c.id_cliente}, nombre={c.nombre}, " +
          f"apellidos={c.apellidos}, edad={c.edad}, cuentas={c.cuentas})")


def print_cuenta(c: Cuenta):
    print(f"Cuenta(iban={c.iban}, saldo_actual={c.saldo_actual}, " +
          f"gasto_total_ultimo_mes={c.gasto_total_ultimo_mes}, " +
          f"ingreso_total_ultimo_mes={c.ingreso_total_ultimo_mes})")
