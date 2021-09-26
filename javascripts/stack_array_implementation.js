// Create a stack
var Stack = function() {
    this.count = 0;
    this.storage = {};

    // Add a value onto the end of the stack
    // Use Object/Dic to implement the stack 
    this.push = function(value) {
        this.storage[this.count] = value;
        this.count++;
    }

    // Remove and return the value at the end of the stack
    this.pop = function() {
        if (this.count === 0) {
            return undefined;
        }
        this.count--;
        let result = this.storage[this.count];
        delete this.storage[this.count];
        return result;
    }

    // Return size of the stack
    this.size = function() {
        return this.count;
    }

    // Return the value at the end of the stack
    this.peek = function() {
        return this.storage[this.count - 1];
    }
}

var myStack = new Stack();

myStack.push(1);
myStack.push(2);
console.log(myStack.peek());
console.log(myStack.pop())
console.log(myStack.peek())
myStack.push("freeCodeCamp");
console.log(myStack.size());
console.log(myStack.peek());
console.log(myStack.pop());
console.log(myStack.peek());