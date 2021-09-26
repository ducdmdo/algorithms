/* Queue */
function Queue() {
    collection = [];

    // print method - will print all values in the queue
    this.print = function() {
        console.log(this.collection);
    }

    // enqueue method - will add element to the queue
    this.enqueue = function(element) {
        collection.push(element);
    }

    // dequeue method  - will remove the front item (the first item getting into the queue) in the queue
    this.dequeue = function() {
        return collection.shift();
    }

    // front method - will return the first front item in the queue
    this.front = function() {
        return collection[0];
    }

    // size method - will return size of the queue
    this.size = function() {
        return collection.length;
    }

    // isEmpty method - check whether the queue is empty
    this.isEmpty = function() {
        return (collection.length === 0);
    }
}

let myQueue = new Queue();
myQueue.enqueue("a");
myQueue.enqueue("b");
myQueue.enqueue("c");
myQueue.print();
myQueue.dequeue();
myQueue.front();
myQueue.print();