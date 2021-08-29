function CarController(scanArray){
    let max = Math.max(...scanArray);
    let index = scanArray.indexOf(max);

    let f = index + 1;

    return f - 8;
}
