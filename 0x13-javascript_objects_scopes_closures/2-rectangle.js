#!/usr/bin/node
/* class Rectangle that defines a rectangle
* the constructor must take 2 arguments w and h
* initialize the instance attribute width with the value of w
* initialize the instance attribute height with the value of h
* If w or h is equal to 0 or not a positive integer, create an empty object
*/
class Rectangle {
  constructor (w, h) {
    if (w > 1 & h > 1) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
