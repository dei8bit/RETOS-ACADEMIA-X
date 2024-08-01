//+ Asume que en un lenguaje alienígena, el orden de las letras del abecedario es permutado. 👽🛸 Dada una lista de palabras, retorna verdadero si las palabras están ordenadas lexicograficamente y falso si no estan ordenadas de acuerdo a este diccionario.

//* Complejidad de tiempo :
//* Complejidad de espacio:
function diccionarioAlien(lista, diccionario) {
	let ordenIndices = {};

	for (let i = 0; i < diccionario.length; i++) {
		const char = diccionario[i];

		ordenIndices[char] = i;
	}

	for (let i = 0; i < lista.length - 1; i++) {
		const palabra1 = lista[i];

		const palabra2 = lista[i + 1];

		//+ se evalua dentro  del bucle si palabra1 tiene mas longitud que la palabra2.

		if (palabra1.length > palabra2.length) {
			break;
		}

		for (let j = 0; j < Math.min(palabra1.length, palabra2.length); j++) {
			if (palabra1[j] != palabra2[j]) {
				if (ordenIndices[palabra1[j]] > ordenIndices[palabra2[j]]) {
					return false;
				}
			}
		}
	}

	return true;
}
