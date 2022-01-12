function myAtoi(s: string): number {
    let number = 0
    let exp = 0
    let negtiveMark = false
    for(let i = s.length - 1; i >= 0; i--) {
        const char = s.charCodeAt(i)
        if((char > 57 || char < 48) && char != 45) {
            if(number != 0) {
                break
            }
            continue
        }

        if(char == 45) {
            negtiveMark = true
        } else {
            number += (char - 48) * (10 ** exp) 
            exp ++
        }
    }

    return negtiveMark ? -number : number
};
/*
No idea why failed :(
Why is this should return 0???
Reason: Wrong Answer
Input: "words and 987"
Output: 987
Expected: 0
*/
