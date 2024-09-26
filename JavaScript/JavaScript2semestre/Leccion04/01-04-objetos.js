let x = 10; //Variable de tipo primitivo
console.log(x.length);
console.log("TiposPrimitivos");

//objeto
let persona = {
  nombre: "Carlos",
  apellidos: "Gil",
  email: "cgas@gmail.com",
  edad: 28,
  idioma: "ES",
  get lang() {
    return this.idioma.toUpperCase(); //Convierte las minúsculas a mayúsculas
  },
  set lang(lang) {
    this.idioma = lang.toUpperCase();
  },
  nombreCompleto: function () {
    //Este es el método get
    return this.nombre + " " + this.apellidos;
  },
  get nombreEdad() {
    return "El nombre es: " + this.nombre + ", edad: " + this.edad;
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

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el método get y set para idiomas");
persona.lang = "en";
console.log(persona.lang);

function Persona3(nombre, apellido, email) {
  //Constructor
  this.nombre = nombre;
  this.apellido = apellido;
  this.email = email;
  this.nombreCompleto = function () {
    return this.nombre + " " + this.apellido;
  };
}

let padre = new Persona3("Leo", "Lopez", "lopezzjfa@gmail.com");
padre.nombre = "Luis"; //modificamos el nombre
padre.telefono = "523587239"; //Unapropiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //utilizamos la función
let madre = new Persona3("Laura", "Contrera", "contreral@gmail.com");
console.log(madre);
console.log(madre.nombreCompleto());

//Diferentes formasde crear objetos
//Casó número 1

let miObjeto = new Object(); //Esta es una opción formal

//caso objeto 2
let miObjeto2 = {}; //Esta opcion es breve y recomendada

//Caso String 1
let miCadena1 = new String("Hola"); //Sintaxis formal
//Caso String 2
let miCadena2 = "Hola"; //Esta es la sintaxis simplificada y recomendada

//caso con números 1
let miNumero = new Number(1);
//Caso con número 2
let miNumero2 = 1; //Sintaxis recomendada

//caso boolean 1
let miBoolean1 = new Boolean(false); //Forma1
//caso boolean 2
let miBoolean2 = false; //Sintaxis recomendad

//Caso Arreglos 1
let miArreglo1 = new Array(); //Formal
let miArreglo2 = []; //Sintaxis recomendada

//caso function 1
let miFuncion1 = new (function () {})(); //Todo despues de new es considerado un objeto
//caso funtion 2
let miFuncion2 = function () {}; //Notacion simplificada

//uso de prototype
Persona3.prototype.telefono = "1214124345";
console.log(padre);
console.log(madre.telefono);
madre.telefono = "21412441";
console.log(madre.telefono);

//Uso del call
let persona4 = {
  nombre: "Franco",
  apellido: "Morales",
  nombreCompleto2: function (titulo, telefono) {
    return this.nombre + " " + this.apellido + " " + telefono;
    //return this.nombre+' '+this.apellido;
  },
};

let persona5 = {
  nombre: "Sebastian",
  apellido: "Loro",
};

console.log(persona4.nombreCompleto2("Lic", "5283792873529"));
console.log(persona4.nombreCompleto2.call(persona5, "Ing", "23576237587235"));

//Metodo Apply
let arreglo = ["Ing", "8537892"];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
