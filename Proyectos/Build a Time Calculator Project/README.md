# Time Calculator Project

This project implements a time calculator in Python that adds a duration to a start time and returns the resulting time, optionally including the day of the week.

## Files
- `main.py`: Contains the implementation of the time calculator and an example usage.

## How does it work?
The `add_time` function takes a start time (in 12-hour format with AM/PM), a duration (in hours and minutes), and optionally a starting day of the week. It calculates the new time, adjusts for AM/PM, and can return the new day if provided. It also indicates if the result is the next day or several days later.

### Example usage
```python
def add_time(start_time, duration_time, starting_day=''):
    # ...code...

print(add_time('3:00 PM', '3:10'))  # Output: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Output: 2:02 PM, Monday
```

## Running the program
To run the program, use:

```bash
python main.py
```

## Expected output
```
6:10 PM
```

## Author
- Franco Rossi
- Second proyect: Build a Time Calculator Project
---
You can modify the input values to test different scenarios and days.
