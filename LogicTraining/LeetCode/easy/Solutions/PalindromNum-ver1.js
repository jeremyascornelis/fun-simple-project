/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    let lastDigit;
    let num1 = x;
    let num2 = 0;
    while(num1 != 0) {
        lastDigit = num1 % 10;
        num2 = num2 * 10 + lastDigit;
        num1 = Math.floor(num1 / 10);
    }
    if(x === num2) {
        return true;
    } else {
        return false;
    }
};

//but it will cause Time Limit Exceed