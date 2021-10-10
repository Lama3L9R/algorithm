function isPrime(number) {
	if(number <= 1) {
		return false
	}

	if(number <= 3) {
		return true
	}

	if(number % 2 === 0 || number % 3 === 0) {
		return false
	}

	for(let i = 5; i*i <= number; i += 6) {
		if(number % i === 0 || number % (i + 2) === 0) {
			return false
		}
	}

	return true
}

/**
 * author: real186526
 * 
 * quick isPrime
 */ 
function Q_iprime(num) {
    return new Promise(async(resolve, reject) => {
        if (num <= 3) resolve(true);
        else if (num % 2 === 0 || num % 3 === 0) resolve(false);
        await Promise.all(Array.from({ length: num }, (item, index) => 3 + index * 2 <= num ? 3 + index * 2 : null).map(e => {
            if (e === null) return;
            else if (num % e) resolve(false);
        }))
        resolve(true)
    })
}

function nextPrime(start) {
	let num = ++start
	while(!isPrime(num)) {
		num ++
	}

	return num
}

/**
 * example: 
 * 
 * (async () => {
 *	let factors = await searchFactors(1003)
 *	console.log(toEquationString(1003, factors))
 * })()
 * 
 * @param number a input number 
 * @param divided input undefined or null or [] for the first call
 * @return a list contains all of the numbers
 */
async function searchFactors(number, divided) {
	if(!divided) {
		return searchFactors(number, [])
	}

	if(divided.reduce((a, b) => a + b, 0) === number) {
		return divided
	}

	let factor = 2

	if(number === 1) {
		return divided
	}

	while(number % factor != 0) {
		factor = nextPrime(factor)
		if(factor > number) {
			throw new Error(`Failed to search! number overflow! curr: ${number} but divide is: ${factor}`)
		}
	}

	return searchFactors(number / factor, [...divided, factor])
}

/**
 * create a equation string like a = b * c * d * e
 * 
 * @param number the input number
 * @param result the result of searchFactors
 * @param mutiplyOperator override the default * operator, can be undefined or null
 * @return the equation string
 */
function toEquationString(number, result, mutiplyOperator) {
	let operator = mutiplyOperator
	if(!mutiplyOperator) {
		mutiplyOperator = "*"
	}

	let outStr = `${number} = `
	result.forEach((it) => { outStr += `${it} ${mutiplyOperator} ` })

	return outStr.substring(0, outStr.length - 3)
}

(async () => {
	console.log(toEquationString(1003, await searchFactors(1003)))
})()