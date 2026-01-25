function missingNumber(nums: number[]): number {
    let xor = 0;
    
    // XOR all numbers from 0 to n
    for (let i = 0; i <= nums.length; i++) {
        xor ^= i;
    }

    // XOR all elements in nums
    for (let num of nums) {
        xor ^= num;
    }

    return xor;
}
