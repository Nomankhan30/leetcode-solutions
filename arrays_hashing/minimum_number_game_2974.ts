function minimumNumberGame(nums: number[]): number[] {
    const arr: number[] = [];
    nums.sort((a, b) => a - b); //Sort ascending
    
    for (let i = 0; i < nums.length; i += 2) {
        const alicePick = nums[i];       //smaller
        const bobPick = nums[i + 1];     //larger
        arr.push(bobPick, alicePick);    //Bob first then Alice second
    }
    
    return arr;
}

