/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
    let sign = Math.sign(x);
    let num1 = Math.abs(x);
    let newNum = 0;
    let lastDigit = num1 % 10;
    if(lastDigit === 0) {
        newNum = Number(String(num1).split('').slice(0, -1).reverse().join(''));
    } else {
        newNum = Number(String(num1).split('').reverse().join(''));
    }
    if(newNum > 0x7FFFFFFF) {
        return 0
    } else {
        if(sign === -1) {
            newNum = newNum.toString();
            newNum = '-' + newNum;
            return newNum;
        }
        return newNum;
    }
};

console.info(reverse(1563847412));

//Note:
//0x7FFFFFFF is a 32-bit integer in hexadecimal
//https://stackoverflow.com/questions/49592995/i-dont-understand-what-is-0x7fffffff-mean-is-there-any-other-way-to-code-gethas#:~:text=The%20constant%200x7FFFFFFF%20is%20a,you%20get%20a%20negative%20value.