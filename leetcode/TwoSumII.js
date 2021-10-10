/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
    Array.prototype.nextMid = (start, end) => {
        const mid = end - start
        if(mid % 2 === 0) {
            return mid / 2 + start
        } else {
            //console.warn(`next: ${Math.floor(mid / 2) + start + 1} ${Math.floor(mid / 2) + start + 1 === end} ${Math.floor(mid / 2) + start + 1 === start}`)
            return Math.floor(mid / 2) + start + 1
        }
    }
    
    for(let i = 0; i < nums.length; i++) {
        if(i === nums.length - 1) {
            throw new Error("Where is your promise?")
        }
        
        const bCurr = nums[i]
        for(let start = i, end = nums.length - 1, j = nums.nextMid(start, end); start !== end; j = nums.nextMid(start, end)) {
            //console.error(`curr: ${start === end} ${start} ${end} mid: ${j} i: ${i}`)
            const sum = bCurr + nums[j]
            if(sum > target) {
                if(j === nums.length - 1) {
                    break
                }
               end = j
            } else if(sum < target) {
               start = j
            } else if(sum === target) {
                return [++i, ++j]
            }

            if(end - start === 1) {
                if(nums[start] + bCurr !== target && nums[end] + bCurr !== target) {
                    break
                }
            } 
        }
        
    }
}
//                  0 1 2 3 4 5 6  7
console.log(twoSum([1,2,3,4,4,9,56,90], 8))