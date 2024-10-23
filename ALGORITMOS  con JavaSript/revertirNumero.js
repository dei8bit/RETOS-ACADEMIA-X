// + Dado un número entero, devuelve el mismo número revertido cambiando el orden de cada dígito. Por ejemplo, el valor revertido de 123 es 321. Si el número es negativo, mantenlo negativo. 
//+ Si el número sale del rango de [-2147483648, 2147483647] retorna 0.
//+ si tiene ceros a la izquierda no deberia de contarlos -73200 = 237.


//. Solucion 1: 
function revertirCadena(num) {
  if (num >0) {
    const numCadena = num.toString()
    const stringInvertido = parseInt(numCadena.split('').reverse().join(''));
    return  stringInvertido;
  }
  else{
    const numCadena = num.toString()
    const stringInvertido = parseInt("-" + numCadena.split('').reverse().join(''));
    return  stringInvertido;}
}



//. Solucion 2 : 

function invertirCadena(num) {
  let invertido = "";
  const numeroCadena = num.toString()
  for (let i = numeroCadena.length - 1; i >= 0; i--) {
    invertido += numeroCadena[i];
  }
  let numeroInvertido = parseInt(invertido)
  if (num > 0) {
    return numeroInvertido
  }
  else {
    return "-" + numeroInvertido
  }
}