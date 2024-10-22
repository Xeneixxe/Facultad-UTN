class Empleado extends Persona {
  static contadorEmpleados = 0;

  constructor(nombre, apelido, edad, sueldo) {
    super(nombre, apelido, edad);
    this._idEmpleado = ++Empleado.contadorEmpleados;
    this._sueldo = sueldo;
  }

  get idEmpleado() {
    return this._idEmpleado;
  }
  get sueldo() {
    this._sueldo;
  }
  set sueldo(sueldo) {
    this._sueldo = sueldo;
  }

  toString() {
    return `
    ${super.toString()}
    ${this._idEmpleado}
    ${this._sueldo}`;
  }
}
