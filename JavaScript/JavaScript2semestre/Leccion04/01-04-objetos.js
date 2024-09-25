let x = 10; //Variable de tipo primitivo
console.log(x.length);
console.log("TiposPrimitivos");

//objeto
let persona = {
  nombre: "Carlos",
  apellidos: "Gil",
  email: "cgas@gmail.com",
  edad: 30,
  nombreCompleto: function () {
    return this.nombre + " " + this.apellidos;
  },
};

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");

let persona2 = new Object(); //Debe crea un objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Calle Sin Nombre 23";
persona2.telefono = "2193817481";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]); //accedemos como si fuera un arreglo
console.log("Usamos elciclo for in");
//for in y accedemos al objeto como si fuera un arreglo
for (propiedad in persona) {
  console.log(propiedad);
  console.log(persona[propiedad]);
}
console.log("Cambiamos y eliminamos un error");
persona.apellida = "Morales"; //Cambiamos diamicamente u valor del objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: la mas sencilla de concatenar cada valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: forma 1");
console.log(persona.nombre + ", " + persona.apellido);

//Numero 2:A traves del ciclo for in
console.log("Distintas formas de imprimir un objeto: forma 2");
for (nombrePropiedad in persona) {
  console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Objet.values()
console.log("Distintas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
console.log("Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);
