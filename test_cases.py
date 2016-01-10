'''
Original test case, I removed the extra newlines from the example, but it will
also work if you include them.
'''
test_input = "5 5\n\
1 2 N\n\
LMLMLMLMM\n\
3 3 E\n\
MMRMMRMRRM"

test_output = "1 3 N\n\n\
5 1 E"

'''
Testing out of bounds movement.
Place a rover on 3x3 grid (x=2,y=2) and move off the grid. Rover will ignore
the offending command because it will be hard to recover if it's on Mars ;).
'''
out_of_bounds_input = "2 2\n\
1 2 N\n\
MRRMM"

out_of_bounds_output = "1 0 S"

'''
Testing out of bounds placement, we wouldn't want the rover to drop off a cliff
as soon as it's deployed.
'''
out_of_bounds_placement_input = "2 2\n\
3 3 N\n\
RRRR"

out_of_bounds_placement_output = "2 2 N"

'''
Testing rover collisions.
Have 3 rovers bump into eachother. Well, actually prevent collisions by
ignoring moves that would lead to a collision.
'''
collision_input = "2 2\n\
0 0 N\n\
M\n\
0 1 S\n\
R\n\
2 1 W\n\
MM"

collision_output = "0 0 N\n\n\
0 1 W\n\n\
1 1 W"

'''
Empty input
'''
empty_input = ""
empty_output = ""

tests = [
    (test_input, test_output),
    (out_of_bounds_input, out_of_bounds_output),
    (out_of_bounds_placement_input, out_of_bounds_placement_output),
    (collision_input, collision_output),
    (empty_input, empty_output)
]
