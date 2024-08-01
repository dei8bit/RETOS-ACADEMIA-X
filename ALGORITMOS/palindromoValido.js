//+ Un palíndromo es una palabra o frase que se lee igual al ser revertida por ejemplo 'La ruta natural'. Dado un texto, devuelve verdadero si el texto es un palíndromo y falso si no es un palíndromo válido. El algoritmo debe ignorar símbolos pero no letras ni números.



function verificarPalindromo(palabra){
  // Quitamos todo simbolo a pal palabra y la convertimos en minusculas
  let palabraSinSimbolos = palabra.replace(/[^a-zA-Z]/g, '').toLowerCase(); 
  // Obtenemos la longitud de la palabra sin simbolos:
  let largo = palabraSinSimbolos.length;
  // Obtenemos la mitad y obtenemos su parte entera en caso de que sea un decimal
  let mitad = Math.trunc( largo/2)
  // Evaluamos de extremo a extremo hacia el centro y si uno no coincide YA NO ES PALINDROMA
for (let i = 0; i < mitad; i++) {
  if (palabraSinSimbolos[i] != palabraSinSimbolos[largo-1-i]){
    return false
  }}
  return true
}

console.log(verificarPalindromo("ana")) // true
console.log(verificarPalindromo("anna")) // true
console.log(verificarPalindromo("asd")) // false
console.log(verificarPalindromo("la ruta natural")) // true
console.log(verificarPalindromo("a ti no;;; bon i ta")) // true