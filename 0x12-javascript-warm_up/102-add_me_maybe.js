#!/usr/bin/node
function carlieRaeJepsen(number, theFunction)
{
	number += 1;
	theFunction(number);
}
exports.addMeMaybe = carlieRaeJepsen
