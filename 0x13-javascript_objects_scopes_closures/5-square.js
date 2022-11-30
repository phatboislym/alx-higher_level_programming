#!/usr/bin/node
/*
* class Square that defines a square and inherits from class Rectangle
* the constructor take one argument: size
*/

class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
