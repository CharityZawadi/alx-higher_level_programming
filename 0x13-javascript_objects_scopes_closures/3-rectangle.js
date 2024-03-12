#!/usr/bin/node
// 3-rectangle.js

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is less than or equal to 0, create an empty object
      this.width = undefined;
      this.height = undefined;
    } else {
      // Otherwise, initialize width and height attributes
      this.width = w;
      this.height = h;
    }
  }

  print() {
    // Check if width and height are undefined (empty object)
    if (this.width === undefined || this.height === undefined) {
      return;
    }
    // Print the rectangle using 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
