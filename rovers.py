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
            give the rover a sense of the plateau it's on
        '''
        max_x, max_y = plateau_dimensions
        self.max_x = int(max_x)
        self.max_y = int(max_y)

        '''
            x = current x coordinate
            y = current y coordinate
            o = current orientation
        '''
        x, y, o = init_string.split(' ')
        self.x = min(self.max_x, int(x))
        self.y = min(self.max_y, int(y))
        self.o = o

        self.obstacles = {}
        self.commands = ''

    def __repr__(self):
        return "<Rover x=%d, y=%d, o=%s>" % (self.x, self.y, self.o)

    def get_position(self):
        return self.x, self.y

    def set_obstacles(self, locations):
        for x, y in locations:
            d = self.obstacles.setdefault(x, {})
            d.setdefault(y, 'ROVER')  # could be any value

    def is_location_free(self, x, y):
        column = self.obstacles.get(x)
        if not column:
            ''' nothing in this column '''
            return True
        else:
            row = column.get(y)
            if not row:
                return True

        return False

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
        new_x = self.x + x
        new_y = self.y + y

        if (not 0 <= new_x <= self.max_x) or (not 0 <= new_y <= self.max_y):
            ''' ignore, out of bounds '''
            pass
        elif not self.is_location_free(new_x, new_y):
            ''' there is a rover in my way! '''
            pass
        else:
            self.x += x
            self.y += y

    def set_commands(self, command_string):
        self.commands = command_string

    def execute(self):
        for c in self.commands:
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

    def __init__(self):
        self.input = ''
        self.rovers = []

    def set_input(self, text):
        ''' take the input, split by newline and discard empty lines '''
        self.input = [line for line in text.split('\n') if line]

    def clear_rovers(self):
        self.rovers = []

    def initialize_rover(self, initial_position, plateau_dimensions):
        rover = Rover(initial_position, plateau_dimensions)
        '''
            Initialize a rover and add it to a list of rovers for reference.
        '''
        self.rovers.append(rover)
        return rover

    def run(self):
        rover_states = []

        ''' First setup the rovers, and collect the control statements '''
        for i, line in enumerate(self.input):
            line = line.upper()

            if i == 0:
                plateau_dimensions = line.split(" ")
            elif (i % 2) == 1:
                rover = self.initialize_rover(line, plateau_dimensions)
            else:
                rover.set_commands(line)

        ''' 
            Now that we have all the rovers initialized, we can pass their current
            positions to the one that's going to move in order to avoid collisions.
        '''
        for i, rover in enumerate(self.rovers):
            obstacles = [r.get_position()
                         for r in self.rovers[:i] + self.rovers[i + 1:]]
            rover.set_obstacles(obstacles)
            state = rover.execute()
            rover_states.append(state)

        return "\n\n".join(rover_states)


if __name__ == "__main__":
    from test_cases import tests
    success = 0
    cc = ControlCenter()
    for i, (test_input, test_output) in enumerate(tests, start=1):
        cc.clear_rovers()
        cc.set_input(test_input)

        if cc.run() == test_output:
            success += 1

    print '%d tests out of %d passed' % (success, i)
