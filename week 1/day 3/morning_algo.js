const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;


function bracesValid(str) {
    newString = []
    for(var i = 0; i < str.length; i++){
        if(str[i] == '(' || str[i] == '[' || str[i] == '{'){
            newString.push(str[i]);
        }else if(str[i] == ')' || str[i] == ']' || str[i] == '}'){
            newString.push(str[i]);
        }
    }
    console.log(newString)
}

bracesValid(str3)


var str4 = "oho!";
const expected4 = false;

function isPalindrome(str) {
    for (var i = 0; i < Math.floor(str.length / 2); i++) {
        if (str[i] !== str[str.length - 1 - i]){
            return false;
            }
        }
        return true;
}

isPalindrome(str4)
