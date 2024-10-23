//+ Obtener todos los elementos que se intersectan entre dos listas:




function interseccion(lista1,lista2){
  if (!lista1===lista2){
  let conjunto1 = new Set(lista1);
  let conjunto2 = new Set(lista2);
    return conjunto1.intersection(conjunto2)
  }
  else return lista1 || lista2
}

console.log(interseccion([1,3],[1,3]))