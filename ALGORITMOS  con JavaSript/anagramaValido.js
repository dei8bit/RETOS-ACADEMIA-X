
//+ Un anagrama es una palabra formada al reordenar las letras de otra. 
//+ Dados 2 textos, devuelve verdadero si un texto es un anagrama del otro y falso si no es un anagrama válido.

//* Complejidad de tiempo :
//* Complejidad de espacio:

function validarAnagramas(palabra1, palabra2) {
	minuscula1 = palabra1.toLowerCase();

	minuscula2 = palabra2.toLowerCase();

	if (minuscula1.length != minuscula2.length) {
		return 'dos palabras deben poseer la misma longitud para ser anagramas';
	} else {
		for (let index = 0; index < minuscula1.length; index++) {
			if (minuscula2.includes(minuscula1[index])) {
				return `${minuscula1} y ${minuscula2} son posibles anagramas`;
			} else {
				return null;
			}
		}
	}
}

console.log(validarAnagramas('abcd', 'dcba')); // abcd y dcba son posibles anagramas

console.log(validarAnagramas('amor', 'roma')); // amor y roma son posibles anagramas

console.log(validarAnagramas('amor', 'romaa')); // dos palabras deben poseer la misma longitud para ser anagramas

console.log(validarAnagramas('aabbcc', 'abbcca')); // aabbcc y abbcca son posibles anagramas
