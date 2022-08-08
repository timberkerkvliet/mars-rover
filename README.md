## Requirements

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers
so that their on board cameras can get a complete view of the surrounding terrain
to send back to Earth.

A rover’s position is represented by a combination of an x and y co-ordinates.
The plateau is divided up into a grid to simplify navigation. An example position
might be (0, 0), which means the rover is in the bottom left corner. An example
heading might be North.

In order to control a rover, NASA sends an instruction. The possible instructions
are: "rotate left", "rotate right" and "move". When rotated, the rover spins 90
degrees left or right respectively, without moving from its current spot. When moved,
the rover moves forward one grid point, maintaining the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

Rovers cannot move outside the grid.

At each grid point, there can be at most one rover.

New rovers are always placed at position (0, 0), heading north.

A rover that receives an instruction that can not be executed, raises an exception
indicating that it can not execute the required instruction and does not do anything.

## Additional requirements: telemetry

Assume that each point in the plateau grid gets assigned a letter A-Z, which the NASA uses
for the type of soil at that point. A rover gets an additional instruction: "get_soil_data", which
sends back the type of soil at the point directly left and right of the current position of the rover.