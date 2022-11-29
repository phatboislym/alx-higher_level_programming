#!/usr/bin/node
function repeat (x, thefunction) {
  for (let i = 0; i < x; i++) {
    thefunction();
  }
}
exports.callMeMoby = repeat;
