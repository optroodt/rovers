# NASA Rovers

To run the program:

```
python rovers.py
```

## Assumptions

I have made the following assumptions

- X and Y coordinates will always be integers, or at least strings that can be cast to integers (base 10).
- The orientation given will always be one of N E S W (or n e s w, for that matter)
- The command string for a rover cannot be empty. If you want a rover to do nothing, set it to 'RRRR'
- If an unknown letter appears in the command string, it will be ignored.
