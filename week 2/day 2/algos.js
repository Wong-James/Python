const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

function frequencyTableBuilder(arr) {
  let table = {};
  for (let value of arr) {
    if (!table.hasOwnProperty(value)) {
      table[value] = 1;
    } else {
      table[value]++;
    }
  }
  return table;
}

console.log(frequencyTableBuilder(arr2))


const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

function reverseWords(str) {
  var newArr = []
  var newStr = " "
  for (words of newArr)
    for(var i = str.length -1; i >= 0; i--){
      newStr +- str[i]
    }return newStr
}

console.log(reverseWords(str2))