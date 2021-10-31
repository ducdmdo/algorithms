function checkCashRegister(price, cash, cid) {
    //all money values are multiplied by 100 to deal with precision errors involved with decimals 
    const denomination = [10000, 2000, 1000, 500, 100, 25, 10, 5, 1,];
  
    function transaction(price, cash, cid) {
      let changeNeeded = (cash - price) * 100;
      //money will be pushed to the second value in each array
      let moneyProvided = [
      ["ONE HUNDRED", 0], 
      ["TWENTY", 0], 
      ["TEN", 0], 
      ["FIVE", 0], 
      ["ONE", 0], 
      ["QUARTER", 0], 
      ["DIME", 0], 
      ["NICKEL", 0], 
      ["PENNY", 0],
    ];
    //take the cid, reverse it (like in Roman Numerals exercise), multiply values by 100
    let availCash = [...cid].reverse().map(el => [el[0], el[1] * 100]);
    //get the total sum of all cash and divide by 100
    let sumOfCash = availCash.reduce((a, b) => (a + b[1]),0) / 100;
    //if sumOfCash is exact change needed return
    if (sumOfCash === changeNeeded / 100) {
      return {status: "CLOSED", change: [...cid]};
    }
    //else, run this function
    else for (let i = 0; i < availCash.length; i++) {
      //if denomination values are less than changeNeeded and availableCash values are greater than 0, run the while loop
        while (denomination[i] <= changeNeeded && availCash[i][1] > 0) {
          //1. moneyProvided array is increased by denomination value
          moneyProvided[i][1] += denomination[i];
          //2. changeNeeded is decreased by same denomination value
          changeNeeded -= denomination[i];
          //3. availCash is also decreased by same denomination value
          availCash[i][1] -= denomination[i];
        }
      };
      
     //clean up the moneyProvided array by
      let change = moneyProvided
      //1. resetting the money values by dividing by 100
      .map(el => [el[0], el[1] / 100])
      //2. filtering out all non-empty dollar and value arrays
      .filter(el => el[1] !== 0);
      //calculate the total of the change array
      let changeTotal = change.reduce((a, b) => (a + b[1]),0);
      //if the total change is less than the change needed
      if (changeTotal < changeNeeded) {
          return {status: "INSUFFICIENT_FUNDS", change: []};
      }
      return {status: "OPEN", change};
    }
  
    //this is where the transaction function is called
    let answer = transaction(price, cash, cid);
    //here the final answer is provided if the 2 if statements don't catch it first
    return answer;
  };

const checkCashRegister = (price, cash, cid) => {
    const AMOUNT = {
      "PENNY": .01,
      "NICKEL": .05,
      "DIME": .10,
      "QUARTER": .25,
      "ONE": 1.00,
      "FIVE": 5.00,
      "TEN": 10.00,
      "TWENTY": 20.00,
      "ONE HUNDRED": 100.00
    }
    let valueInDrawer = (cid[0][1] + cid[1][1] 
          + cid[2][1] + cid[3][1] + cid[4][1] 
          + cid[5][1] + cid[6][1] + cid[7][1] + cid[8][1]).toFixed(2);
    let changeBack = (cash - price);
    const changeBackArray = [];
    //Insufficient case - when the amount in the drawer is less than the amount need to change back
    if (valueInDrawer < changeBack ) {
      return { status: "INSUFFICIENT_FUNDS", change: changeBackArray };
    //Closed case - when the amount in the drawer equal to the amount need to change back
    } else if (changeBack.toFixed(2) === valueInDrawer) {
      return { status: "CLOSED", change: cid };
    //Open case & Insufficient case - when the amount in the drawer is larger than the amount need to change back OR do not have the right coins to change back
    } else {
      cid = cid.reverse();
      for (let element of cid) {
        let temp = [element[0], 0];
        console.log(element);
        console.log(AMOUNT[element[0]] + "-" + element[1]);
        //calculate number of times each unit should use from the drawer
        while ((changeBack >= AMOUNT[element[0]]) && (element[1] > 0)) {
          console.log("inside while loop: temp[1]:" + temp[1])
          temp[1] += AMOUNT[element[0]];
          element[1] -= AMOUNT[element[0]];
          changeBack -= AMOUNT[element[0]];
          changeBack = changeBack.toFixed(2);
        }
        if (temp[1] > 0) {
          changeBackArray.push(temp);
        }
      }
    }
    if (changeBack > 0) {
      return { status: "INSUFFICIENT_FUNDS", change: [] };
    }
    return { status: "OPEN", change: changeBackArray};
  }
  
  checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
  
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
  
  checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);