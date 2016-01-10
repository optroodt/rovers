class Rover(object):

    DIRECTIONS = 'NESW'
    MOVEMENTS = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, init_string, plateau_dimensions):
        '''
            x = current x coordinate
            y = current y coordinate
            o = current orientation
        '''
        x, y, o = init_string.split(' ')
        self.x = int(x)
        self.y = int(y)
        self.o = o

        max_x, max_y = plateau_dimensions
        self.max_x = int(max_x)
        self.max_y = int(max_y)

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
        if not 0 <= self.x + x <= self.max_x:
            pass
        else:
            self.x += x

        if not 0 <= self.y + y <= self.max_y:
            pass
        else:
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
                plateau_dimensions = line.split(" ")
            elif (i % 2) == 1:
                rover = Rover(line, plateau_dimensions)
            else:
                state = rover.control(line)
                rover_states.append(state)

        return "\n".join(rover_states)

if __name__ == "__main__":
    from test_cases import tests
    for test_input, test_output in tests:
        cc = ControlCenter(test_input)
        assert cc.run() == test_output
