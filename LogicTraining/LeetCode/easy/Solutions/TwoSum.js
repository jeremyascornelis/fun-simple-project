/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    let result = new Array();
    for(let i = 0; i < nums.length; i++) {
        for(let j = i + 1; j < nums.length; j++) {
            if(nums[i] + nums[j] === target) {
                let idx1 = nums.indexOf(nums[i]);
                let idx2 = nums.indexOf(nums[j]);
                if(idx1 === idx2) {
                    idx2 = nums.indexOf(nums[j], idx1 + 1);
                }
                result.push(idx1, idx2);
            }
        }
    }
    return result;
};