function isDivisible(divisor) {
    let sum = 0;
    let divisibles = [];
    
    for (let i = 0; i < 501; i++){
        if (i % divisor == 0) {
            divisibles.push(i)
            sum += i
        }
    }
    
    console.log(`Numbers divisible by ${divisor}: ${divisibles.join(" ")}` );
    console.log(`Sum: ${sum}`)
}

isDivisible(23)