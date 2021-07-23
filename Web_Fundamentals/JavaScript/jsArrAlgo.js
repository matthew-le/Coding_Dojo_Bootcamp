
var testArr = [6,3,5,1,2,4]
var sum = 0;

for (i=0; i < testArr.length; i++) {
    console.log("num:"+ testArr[i]);
    sum = testArr[i] + sum;
    console.log("sum:"+ sum);
}

var newArr=[];
var result=0;

for (i=0; i<testArr.length; i++) {
    result =i * testArr[i];
    newArr.push(result);
}

console.log(newArr);
