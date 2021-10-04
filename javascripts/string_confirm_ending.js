    function confirmEnding(str, target) {
        console.log(str.substr(str.length - target.length));
        return (str.substr(str.length - target.length) === target) ? true: false;
    }

    function confirmEnding(str, target) {
    // "Never give up and good luck will find you."
    // -- Falcor

    return str.slice(str.length - target.length) === target;
    }

    function confirmEnding(str, target) {
    // "Never give up and good luck will find you."
    // -- Falcor

        let re = new RegExp(target + "$", "i");

        return re.test(str);
    }

    function confirmEnding(str, target) {
        return str.slice(-target.length) === target
    }


console.log(confirmEnding("Open sesame", "same"));
