function ages(myAge) {
    console.log(`My mum is twice my age at ${2*myAge}`);
    console.log(`My dad is 1.2 times my mum's age at ${1.2*2*myAge}`);
    return null; 
}

function ageMum(myAge) {
    return (2*myAge)
}
ages(15);
console.log(ageMum(23))