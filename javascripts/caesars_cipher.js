function rot13(str) {
    let input     = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let output    = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm';
    return str.split('').map(item => {
      return input.indexOf(item) > -1 ? output[input.indexOf(item)] : item;
    }).join('');
  }
  
  console.log(rot13("SERR PBQR PNZC"));