//+ Se entrega un texto con parentesis, corchetes, y/o llaves.

//+ Para que este sea valido debe cumplir con que  si o si TODOS los parentesis, corchetes, y/o llaves. esten cerrados!!

//+ Ejemplos validos:    "()[]{}" o  "{[()]}" o "()[{}]"

//+ Ejemplos invalidos:  ")([]{}}" o "(}][{)" o "{([])"


//* Complejidad de tiempo :
//* Complejidad de espacio:

const caracterEspejo = {
	'(': ')',

	'[': ']',

	'{': '}',
};

function validarEquilibrio(texto) {
	const pila = [];

	for (let index = 0; index < texto.length; index++) {
		if (texto.length % 2 != 0) {
			return 'la expresion nunca puede ser impar';
		}

		if (texto.charCodeAt(0) === 41 || texto.charCodeAt(0) === 93 || texto.charCodeAt(0) === 125) {
			return 'es imposible que el primer caracter sea cerrado';
		}

		const caracter = texto[index];

		if (caracter in caracterEspejo) {
			// Si es un carácter de apertura

			pila.push(caracter);
		} else if (caracterEspejo[pila[pila.length - 1]] === caracter) {
			// Si es un carácter de cierre y coincide con el último de la pila

			pila.pop();
		} else {
			return false; // Si no coincide o es un carácter de cierre inesperado, el texto no es válido
		}
	}

	return pila.length === 0; // El texto es válido si la pila está vacía al final
}

const textoValido = '()[{}]';

const textoInvalido = '(([]{}';

console.log(validarEquilibrio(textoValido)); // Devuelve true

console.log(validarEquilibrio(textoInvalido)); // Devuelve false
