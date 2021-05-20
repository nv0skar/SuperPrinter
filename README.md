# SuperPrinter 🌈
#### SuperPrinter is pretty much like `print()`, but with superpowers 🚀

### Features
- Print with colors 🎨
- Push notifications in macOS 📌
- Save into a log file 📖
- Make post requests 🙋‍♂️ | **⚠️ Not extensively tested**

## Quick Guide
```python
import superPrinter # Import superPrinter
sp = superPrinter.printer() # Set the var with the object
sp.sprint("Calendar", "Event added!", level=superPrinter.levels.info) # Call sprint() method
```
**Output:** `Calendar: Event added! | At: 2021-01-01 00:00:00.000` (As you can see In the output, it prints the caller followed by the message)
```python
import superPrinter # Import SuperPrinter
sp = superPrinter.printer(logFile="logging.log") # Set the var with the object
sp.sprint("Calendar", "New event could not be added!", log=True, level=superPrinter.levels.error) # Call sprint() method
```
The above code will print the message as an error, also the message will be saved in a log file.

**Easy, doesn't it? 😀**

## Usage
1. `superPrinter.printer(logFile, url, port)`
- `logFile` : Pass the logging file name **(Not required)**
- `url` : Set the url for the post request **(Not required)**
- `port` : Set the port for the post request **(Not required)**

2. `superPrinter.printer.sprint(caller, message, end, level, log, show, colored, time, post, postPath, notify, catch)`
- `caller` : Set the caller
- `message` : Set the message
- `show` : Set if you want to `print()` the string **(Not required)**
- `end` : Set the end of the `print()` (The default Is a new line) **(Not required)**
- `level` : Set the level of the log and the color of the caller **(Not required)**
- `log` : Set If you want to save It into a logging file **(Not required)**
- `colored` : Set if you want colors when `print()` **(Not required)**
- `time` : Set if you want to include the time, if you set `False` the time will not be included: in the log file, in the post request and in when `print()` **(Not required)**
- `post` : If you want to make a post request **(Not required)**
- `postPath` : Set the path of the post request **(Not required)**
- `notify` : If you want to push a notification (macOS) **(Not required)**
- `catch` : If you want the message string returned **(Not required)**

3. `superPrinter.levels`
- info: `superPrinter.levels.info` (Level number: 0) 💁‍♂️
- warning: `superPrinter.levels.warning` (Level number: 1) 🤷‍♂️
- error: `superPrinter.levels.error` (Level number: 2) 🙅‍♂️
- critical: `superPrinter.levels.critical` (Level number: 3) 🙇‍♂️

## Installation
That's a good question...
1. Simply, copy `superPrinter` to your projects directory and import it.

Or maybe you could...
1. Generate a wheel and install it.

**And it's done! 🎉**
