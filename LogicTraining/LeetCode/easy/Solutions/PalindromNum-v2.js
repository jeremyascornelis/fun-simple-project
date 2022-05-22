//More Faster
/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    let num1 = x;
    let num2 = 0;
    num2 = Number(String(num1).split('').reverse().join(''));
    if(num1 === num2) {
        return true;
    } else {
        return false;
    }
};