#!/usr/bin/node
const fs = require('fs');

// Get file paths from command line arguments
const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

// Read contents of source files asynchronously
fs.readFile(sourceFilePath1, 'utf8', (err1, data1) => {
  if (err1) throw err1;
  fs.readFile(sourceFilePath2, 'utf8', (err2, data2) => {
    if (err2) throw err2;

    // Concatenate contents of both files
    const concatenatedContents = data1 + data2;

    // Write concatenated contents to destination file
    fs.writeFile(destinationFilePath, concatenatedContents, (err3) => {
      if (err3) throw err3;
      console.log(`Concatenation of ${sourceFilePath1} and ${sourceFilePath2} saved to ${destinationFilePath}`);
    });
  });
});

