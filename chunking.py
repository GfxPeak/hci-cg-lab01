let items = ['6', '3', '9', '2', '8', '5', '7', '4'];
console.log("Ungrouped:", items.join(' '));

// Chunked items
let chunked = [['6', '3', '9'], ['2', '8', '5'], ['7', '4']];
console.log("Chunked:", chunked.map(c => c.join('')).join(' '));

// Explanation output
console.log("\nUngrouped is harder to remember.");
console.log("Chunked is easier because items are grouped into meaningful units.");
