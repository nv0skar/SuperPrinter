# SuperPrinter
#### SuperPrinter Is like `print()`, but with added features 🚀

### Features
- Prints with colors 🤖
- Push notifications in macOS 🍎
- Save into log file ⭐️
- Make post requests **(Unstable)** **(Could make exceptions)** 🪄

## Quick Guide
```python
import SuperPrinter # Import SuperPrinter
sp = SuperPrinter.SuperPrinter() # Set the var with the object
sp.print("Calendar", "Event added!") # Call print() method
```
**Output:** `Calendar: Event added! | At: 2021-01-28 20:17:54.108129`\
As you can see In the output, It prints the caller followed by the message.\
When we add a caller we can specify from which part of the code the text was printed, this could be useful to debug a big project with lots of functions.
```python
import SuperPrinter # Import SuperPrinter
import logging # Import logging
logging.basicConfig(filename='logging.log', level=logging.INFO) # Set logging basic config
sp = SuperPrinter.SuperPrinter(log_object=logging) # Set the var with the object
sp.print("Calendar", "Event added!") # Call print() method
```
The above code will print a message, and also, the message will be saved in a log file.



## API
1. `SuperPrinter(self, log_object=None, url=None, port=None, api=None)`
- `log_object` : Pass the logging object as showed in the *Quick Quide*
- `url` : Pass the url for the post request
- `port` : Set the port for the post request 
2. `SuperPrinter.print(caller, message, show=True, end="\n", log=False, level="info", colors=True, time=True, post=False, postPath=None, notify=False, catch=False)`
- `caller` : Set the caller
- `message` : Set the message
- `show` : Set if you want to `print()`
- `end` : Set the end of the `print()` (the default Is a new line)
- `log` : Set If you want to save It into the logging file
- `level` : Set the level of the log
- `colors` : Set If you want colors at `print()`
- `time` : Set if you want to include the time, If you set `False` the time will not be included: In the log file, In the post request and in the terminal.
- `post` : If you want to make a post request
- `postPath` : Set the path of the post request
- `notify` : If you want to push a notification (macOS)
- `catch` : If you want to make SuperPrinter return a string

## Installation
1. Firstly you have to copy `SuperPrinter` and import it.
#### That's all! 🙂 
