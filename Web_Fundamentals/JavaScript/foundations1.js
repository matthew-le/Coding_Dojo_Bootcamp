function counter() {
    var newArr = [];
    for (var i = 1; i <= 255; i++) {
        newArr.push(i);
    }
    return newArr;
}
var result = counter();

console.log(result);

function even() {
    var y = 0;
    for (var i = 1; i<=1000; i++){
        if (i % 2 == 0) {
            y = y + i;
        }
    }
    return y;
}

var result = even();

console.log(result);

function odd() {
    var y = 0;
    for (var i = 1; i<=5000; i++){
        if (i % 2 != 0) {
            y = y + i;
        }
    }
    return y;
}

var result = odd();

console.log(result);


function sumArr(arr) {
    var sum = 0;
    for (var i = 0; i<arr.length; i++) {
        sum = sum + arr[i];
    }
    return sum;
}

console.log(sumArr([1,2,3]));

function max(arr) {
    var max = arr[0];
    for (var i = 0; i<arr.length; i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

console.log(max([2,20,100, -1, 330]));


function avg(arr) {
    var sum = 0;
    var avg = 0;
    for (var i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    }
    avg = sum / arr.length;
    return avg;
}
console.log(avg([1,2,3,4,5,6,7,8,9,10]));

function oddArr(){
    var newArr = [];
    for (var i=0; i<=50; i++){
        if (i % 2 != 0){
            newArr.push(i);
        }
    } return newArr;
}

console.log(oddArr());

function greatY(num){
    var y = 6;
    var counter = 0;
    for (var i = 0; i < num.length; i++){
        if (num[i] > y){
            counter++;
        }
    }   return counter;
}
console.log(greatY([3,5,10,20,4,-10]));

function square(num) {
    for (var i = 0; i < num.length; i++){
        num[i] = num[i]*num[i]; 
    }   return num;
}   

console.log(square([1,2,4,10,1]));

