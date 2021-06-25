const str1 = "Hello World";
const rotateAmnt1 = 0;
const expected1 = "Hello World";

const str2 = "Hello World";
const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const str3 = "Hello World";
const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const str4 = "Hello World";
const rotateAmnt4 = 4;
const expected4 = "orldHello W";

function rotateStr(str, n) {
  var newStr = ""
  for (var i = str.length - n; i < str.length; i++){
    newStr += str[i]
  }for (var i = 0; i < str.length - n; i++){
    newStr += str[i]
  }return newStr
}
console.log(rotateStr(str4, 4))