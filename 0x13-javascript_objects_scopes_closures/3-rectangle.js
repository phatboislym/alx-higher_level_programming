#!/usr/bin/node
/* class Rectangle that defines a rectangle
* the constructor takes 2 arguments w and h
* - initializes the instance attribute width with the value of w
* - initializes the instance attribute height with the value of h
* - if w or h is equal to 0 or not a positive integer, it creates an empty object
* instance method print prints the rectangle using the character 'X'
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
}
module.exports = Rectangle;
