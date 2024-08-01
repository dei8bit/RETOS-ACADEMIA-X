//+ Crear una funcion que indica si un numero es perfecto o no
//+ Un número perfecto es aquel igual a la suma de sus divisores
//+ Ejemplo: 6 se puede dividir por 1, 2 y 3; 1+2+3 = 6 


function numeroPerfecto(num) {
  let check = 0
  for (let i = 1; i < num - 1; i++) {
    if (num % i === 0) { check += i }
  }
  return check === num
}

console.log(numeroPerfecto(6))    //  true
console.log(numeroPerfecto(28))   //  true
console.log(numeroPerfecto(496))  //  true
console.log(numeroPerfecto(90))   //  false
