//+ Dada una lista, devuelve verdadero si algún valor aparece al menos dos veces y falso si todos elementos son distintos.

//* Complejidad de tiempo:
//* Complejidad de espacio: 

function detectDuplicate(colection) {

  const conjunto = new Set(colection)

  return colection.length > conjunto.size ? "contiene duplicados": "no contiene duplicados" 

}