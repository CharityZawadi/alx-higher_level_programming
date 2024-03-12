#!/usr/bin/node
// 2-rectangle.js

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
}

module.exports = Rectangle;
