#!/usr/bin/node
/* class Rectangle that defines a rectangle
* the constructor takes 2 arguments w and h
* - initializes the instance attribute width with the value of w
* - initializes the instance attribute height with the value of h
*/
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
