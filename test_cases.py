'''
Original test case, I removed the extra newlines from the example, but it will
also work if you include them.
'''
test_input = "5 5\n\
1 2 N\n\
LMLMLMLMM\n\
3 3 E\n\
MMRMMRMRRM"

test_output = "1 3 N\n\
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


tests = [
    (test_input, test_output),
    (out_of_bounds_input, out_of_bounds_output)
]
