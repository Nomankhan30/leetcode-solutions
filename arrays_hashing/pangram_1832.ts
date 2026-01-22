function checkIfPangram(sentence: string): boolean {
    // Create a Set to store unique letters
    const letters = new Set<string>();

    // Loop through each character in the sentence
    for (const char of sentence) {
        letters.add(char); //Add character to the set
    }

    //If the set has 26 letters, it is a pangram
    return letters.size === 26;
}


