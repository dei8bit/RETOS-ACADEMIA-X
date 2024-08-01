//+ Elaborar un algoritmo que remueva los duplicados de una coleccion


//* Complejidad de tiempo: O(n) !
//* Complejidad de espacio: 



const removeDuplicate = (colection) => new Set(colection)

console.log(removeDuplicate([1,2,3,3,4,5])); /// Set(5) { 1, 2, 3, 4, 5 }