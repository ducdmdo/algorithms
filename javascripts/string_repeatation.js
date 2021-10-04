function repeatStringNumTimes(str, num) {
    let result ="";
    if (num <= 0) {
        return result;
    }
    for (let i = 0; i < num; i++) {
        result += str;
    }
    return result;
}

function repeatStringNumTimes(str, num) {
    let result = ""
    while (num > 0) {
        result += str;
        num--;
    }
    return result;
}

/* recursion version */
function repeatStringNumTimes(str, num) {
    if (num < 1) {
        return "";
    } else {
        return str + repeatStringNumTimes(str, num-1);
    }
}

function repeatStringNumTimes(str, num) {
    return num > 0 ? str + repeatStringNumTimes(str, num-1) : "";
}

console.log(repeatStringNumTimes("abc", 3))