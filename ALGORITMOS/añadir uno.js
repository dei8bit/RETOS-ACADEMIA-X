//+ Recibes un entero representado como una lista de dígitos enteros del 0 al 9. por ejemplo 128 es [1,2,8]
//+ Crea un algoritmo que retorne este nùmero + 1 en forma lista:
//+ por ejemplo : si fuese [1,2,8], resultaria en  [1,2,9]

//* Complejidad de tiempo:
//* Complejidad de espacio: 

function aumentarEnUno(lista) {
  // Transformar numeros a una cadena
  let numeroComoCadena = lista.join('');
  
  // transformar cadena a un entero en base 10
  let numeroEntero = parseInt(numeroComoCadena, 10);
  
  // aumentar el numero
  let aumentado = numeroEntero+1
  
  // volvero a convertir en cadena 
  const cadena = aumentado.toString()

  // crear un array con cada caracter de la cadena y usar el constructor Number para crear un numero.
  let listaAumentada = cadena.split('').map(Number);

  return listaAumentada;
}


