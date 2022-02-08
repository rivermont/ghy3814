/* for index.html */
function helloWorld() {
    document.getElementByID("foo").innerHTML = "Hello World!";
}

/* for lab 02 */
console.log("Hello world");

var car = {
    make:  "Tesla",
    model: "Model X",
    year:  2021,
    color: "Red",
    start: function() { console.log("Car started!"); }
};

car.start();

// maths
var x = 13;
var y = 2;
var z = x + y;
z;

// datatypes
var cost = null;
var type = "data";

var cost = x * 1.07;
console.log(cost);

cost <= y;

car.year > x;

var array1 = [car, x, "test", 42];

car.make;
console.log(car.model);

// loops
for (i in array1) {
    console.log(array1[i]);
}

// json parsing
var directory = {
    "employees": [
        {"first": "John",  "last": "Doe"},
        {"first": "Anna",  "last": "Smith"},
        {"first": "Peter", "last": "Jones"}
    ]
};
        
var data = directory.employees;
console.log(data);

for (var i in data) {
    fName = data[i].first;
    lName = data[i].last;
    console.log(fName + ' ' + lName);
}

// more html things
document.body;
