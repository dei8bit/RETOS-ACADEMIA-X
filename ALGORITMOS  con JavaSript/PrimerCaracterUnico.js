//+ Dado un texto, devuelve el índice del primer caracter que no se repite y devuelve -1 si todos los caracteres se repiten al menos una vez. Por ejemplo, 'elefante' tiene un caracter que se repite al menos 3 veces. Es la letra 'e'. El primer caracter que no se repite es la letra 'l' en el índice 1.

//i! La expresion regular evalua la cantidad de veces que existe un caracter en una cadena
//. Version legible:
function primerCaracterUnico(palabra) {
	for (let caracter of palabra) {
		let longitudDeCaracteres = (palabra.match(new RegExp(caracter, 'g')) || []).length;
		if (longitudDeCaracteres == 1) {
			return caracter;
		}
	}
}


console.log(primerCaracterUnico('llanta')); /// n
console.log(primerCaracterUnico('elefante')); /// l
console.log(primerCaracterUnico('$Cualquier Caracter')); /// $


//. Version compacta:

function primerCaracterUnico(palabra) {
	for (let caracter of palabra) {
		if ((palabra.match(new RegExp(caracter, 'g')) || []).length == 1) return caracter;
	}
}
