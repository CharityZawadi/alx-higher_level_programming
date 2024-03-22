#!/usr/bin/node
// 6-square.js

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    // Print the square using the character c
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
