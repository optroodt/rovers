class Rover(object):

    DIRECTIONS = 'NESW'
    MOVEMENTS = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, init_string):
        '''
            x = current x coordinate
            y = current y coordinate
            o = current orientation
        '''
        x, y, o = init_string.split(' ')
        self.x = int(x)
        self.y = int(y)
        self.o = o

    def __repr__(self):
        return "<Rover x=%d, y=%d, o=%s>" % (self.x, self.y, self.o)

    def _rotate(self, direction):
        i = self.DIRECTIONS.index(self.o)
        i = i + direction
        if i == len(self.DIRECTIONS):
            self.o = self.DIRECTIONS[0]
        elif i < 0:
            self.o = self.DIRECTIONS[-1]
        else:
            self.o = self.DIRECTIONS[i]

    def rotate_right(self):
        self._rotate(1)

    def rotate_left(self):
        self._rotate(-1)

    def move(self):
        x, y = self.MOVEMENTS.get(self.o)
        self.x += x
        self.y += y

    def control(self, control_string):
        for c in control_string:
            if c == 'L':
                self.rotate_left()
            elif c == 'R':
                self.rotate_right()
            elif c == 'M':
                self.move()
            else:
                print 'unknown command: %s' % c

        return "%d %d %s" % (self.x, self.y, self.o)


class ControlCenter(object):

    def __init__(self, text):
        # take the input, split by newline and discard empty lines
        self.input = [line for line in text.split('\n') if line]


    def run(self):
        rover_states = []
        for i, line in enumerate(self.input):
            if i == 0:
                # print 'grid size %s' % line
                pass
            elif (i % 2) == 1:
                # print 'initialize rover %s' % line
                rover = Rover(line)
            else:
                # print 'control rover %s' % line
                state = rover.control(line)
                rover_states.append(state)
        
        return "\n".join(rover_states)

test_input = "5 5\n\
1 2 N\n\
LMLMLMLMM\n\
3 3 E\n\
MMRMMRMRRM"

test_output = "1 3 N\n\
5 1 E"

cc = ControlCenter(test_input)
assert cc.run() == test_output

