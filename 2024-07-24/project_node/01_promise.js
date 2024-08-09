// Example 1: Program with a Promise
// Let's suppose that the program below is an asynchronous program.
// Then the program can be handled by using a promise.

const count = true;

let countValue = new Promise(function (resolve, reject) { // Background Thread

if (count) {
// Call api, call db, call file system
	resolve("I have completed all the operations.");
} else {
	reject("There is no count value");
}

});
console.log(countValue);