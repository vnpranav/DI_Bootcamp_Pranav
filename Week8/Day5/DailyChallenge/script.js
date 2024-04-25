function allTruthy(...param){
    let parameterList = [...param];
    
    return parameterList.reduce((acc, val) => acc && Boolean(val), true)
}

console.log(allTruthy(0,1,2,3,4))

// console.log(Boolean(4))