function spinalCase(str) {
    let result = str
                  .split(/[\s_]+|(?=[A-Z])/)
                  .join("-")
                  .toLowerCase();
    return result;
    //console.log(result);
  }