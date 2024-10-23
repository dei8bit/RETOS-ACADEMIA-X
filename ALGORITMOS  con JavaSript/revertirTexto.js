//+ Escribe una función que invierta texto.


//* Complejidad de tiempo O(n):
//* Complejidad de espacio: 

const reverText = text => {

  chars = [...text];

  return chars.reverse().join('')

}


console.log(reverText("cheese steak jimmy's")); /// s'ymmij kaets eseehc 

console.log(reverText("pepperoni pizza"));      /// azzip inoreppep 