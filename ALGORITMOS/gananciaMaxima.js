//+ Escribe un algoritmo que tome una lista de precios diarios de un stock (como S&P500), y retorne la ganacia máxima que se puede obtener al comprar el stock una vez y venderlo en el mejor momento. En caso de que no haya una ganacia, retorna 0.

//* Complejidad de tiempo :
//* Complejidad de espacio:

function calcularGanacia(accion) {
	if (accion.length === 0) {
		return undefined;
	}

	const maximo = Math.max(...accion);

	const minimo = Math.min(...accion);

	const validacion = accion.some(precio => typeof precio !== 'number' || precio < 0);

	if (validacion) {
		return 'Algun precio es erroneo ';
	}

	if (maximo - minimo === 0) {
		return 0;
	} else {
		return `ganancia maxima:-> $${maximo - minimo}`;
	}
}

console.log(calcularGanacia([45, 23, -30])); /// Algun precio es erroneo

console.log(calcularGanacia([45, '4', 8])); /// Algun precio es erroneo

console.log(calcularGanacia([45, {}, 8])); /// Algun precio es erroneo

console.log(calcularGanacia([45, 45])); /// 0

console.log(calcularGanacia([6, 23, 99, 75])); /// ganancia maxima:-> $93
