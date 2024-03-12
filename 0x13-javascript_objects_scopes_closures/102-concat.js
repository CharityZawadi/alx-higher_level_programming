#!/usr/bin/node
// 102-concat.js

const fs = require('fs');

// Get the file paths from command line arguments
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

// Read the contents of the source files
const fileContents1 = fs.readFileSync(sourceFilePath1, 'utf8');
const fileContents2 = fs.readFileSync(sourceFilePath2, 'utf8');

// Concatenate the contents of the source files
const concatenatedContents = fileContents1 + fileContents2;

// Write the concatenated contents to the destination file
fs.writeFileSync(destinationFilePath, concatenatedContents);

console.log(`Concatenation of ${sourceFilePath1} and ${sourceFilePath2} saved to ${destinationFilePath}`);

