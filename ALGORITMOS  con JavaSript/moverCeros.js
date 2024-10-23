//+ Dada una lista de números que pueden contener el número 0, 
//+ devuelve la misma lista con los ceros recorridos hacia el final de la lista.


const numeros1 = [0,3,4,0,9];
const numeros2 = [0,0,0,8];
const numeros3 = [8,0,0,0];
const numeros4 = [0,0,0,0]; //i! no deberia hacer nada aqui

function moverCeros(listaNumerica) {
  if  (!listaNumerica.every(c=>c ==0)){
    return listaNumerica.sort((a, b) =>  b-a);  // ordenar lista usando compare function.
  }
  else return listaNumerica
}


console.log(moverCeros(numeros1)); 
console.log(moverCeros(numeros2)); 
console.log(moverCeros(numeros3)); 
console.log(moverCeros(numeros4)); 

