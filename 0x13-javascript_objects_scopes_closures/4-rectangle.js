#!/usr/bin/node
/* class Rectangle that defines a rectangle
* the constructor takes 2 arguments w and h
* - initializes the instance attribute width with the value of w
* - initializes the instance attribute height with the value of h
* - if w or h is equal to 0 or not a positive integer, it creates an empty object
* instance method print prints the rectangle using the character 'X'
* instance method rotate that exchanges the width and the height of the rectangle
* instance method double that multiples the width and the height of the rectangle by 2
*/
class Rectangle {
  constructor (w, h) {
    if (w > 1 & h > 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let k = '';
    for (let i = 0; i < this.height; i++) {
      k = '';
      for (let j = 0; j < this.width; j++) {
        k += 'X';
      }
      console.log(k);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
