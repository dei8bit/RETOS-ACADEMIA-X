function ordenamientoPorFrecuencia(texto) {
  let frecuencias = {};
  const valores = new Set();

  // Contar la frecuencia con que aparece cada carácter:
  for (let i = 0; i < texto.length; i++) {
    let char = texto[i];
    if (frecuencias[char]) {
      frecuencias[char]++;
    } else {
      frecuencias[char] = 1;
    }
    valores.add(frecuencias[char]);  // Agregar cada numero a un set
  }

  // Convertir el objeto de frecuencias en un array de pares [carácter, frecuencia]
  const entradas = Object.entries(frecuencias);

  // Convertir el Set de valores en un array y ordenar los valores del arreglo de forma descendente
  const arregloDeValores = Array.from(valores).sort((a, b) => b - a);


  let result = '';

  // Recorrer los valores de frecuencia ordenados
  for (let value of arregloDeValores) {
    // Para cada valor de frecuencia, encontrar los caracteres correspondientes
    for (let [char, freq] of entradas) {
      if (freq === value) {
        result += char;
      }
    }
  }

  return result

}

console.log(ordenamientoPorFrecuencia("aloha lolo"))  // loah
console.log(ordenamientoPorFrecuencia("alojomora"))   // oaljmr
console.log(ordenamientoPorFrecuencia("hello world")) // lohe wrd