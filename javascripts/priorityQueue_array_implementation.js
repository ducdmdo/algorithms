function priorityQueue () {
    let collection = [];
    
    //printCollection method - will print all the values in the priority queue
    this.printCollection = function() {
        (console.log(collection));
    }

    // enqueue method - will add the item to the queue
    this.enqueue = function(element) {
        if (this.isEmpty()) {
            collection.push(element);
        } else {
            let added = false;
            for (let i = 0; i < collection.length; i++) {
                if (element[1] < collection[i][1]) { // check the priority
                    collection.splice(i,0,element);
                    added = true;
                    break;
                }
            }
            if (!added) {
                collection.push(element);
            }
        }
    }

    // dequeue method - will delete the front item in the queue
    this.dequeue = function() {
        let value = collection.shift();
        return value[0] // return the value only, not the priority
    }

    // front method - will return the front item in the queue
    this.front = function() {
        return collection[0]; // return the value only; not the priority
    }

    // size method - will return the size of the queue
    this.size = function() {
        return collection.length;
    }

    // isEmpty method - check whether the queue is either empty or not
    this.isEmpty = function() {
        return (collection.length === 0);
    }
}

let myPriorityQueue = new priorityQueue();
myPriorityQueue.enqueue(['beau Carnes', 5]);
myPriorityQueue.enqueue(['Quincy Larson', 4]);
myPriorityQueue.enqueue(['Ewa', 3]);
myPriorityQueue.enqueue(['Duc', 2]);
myPriorityQueue.enqueue(['briana Swift', 1]);
myPriorityQueue.printCollection();
//myPriorityQueue.dequeue();
console.log(myPriorityQueue.front());
myPriorityQueue.printCollection();