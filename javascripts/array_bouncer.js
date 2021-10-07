function bouncer(arr){
    let resultArray =[];
    for (let i = 0; i < arr.length; i++){
        if(arr[i]) resultArray.push(arr[i]);
    }
    return resultArray;
}

function bouncer(arr) {
    return arr.filter(Boolean);
}