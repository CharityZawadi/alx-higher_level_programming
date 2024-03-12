#!/usr/bin/node
// 2-rectangle.js

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {}; // Return an empty object if width or height is not positive integers
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;

