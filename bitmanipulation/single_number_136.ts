//approach is simple: we will use Xor operator as it cancels every element which comes twice.
function singleNumber(nums: number[]): number {
    let ans: number = 0;

    for (const num of nums) {
        ans ^= num;
    }

    return ans;
}
