AFK Sensor in Python v2.0
==========

This is a simple AFK (Away From Keyboard) sensor in Python. The code can be used to detect if the user is inactive for a certain period of time and log the time spent being inactive. It can be useful in scenarios where the user needs to be present and active, like online classes, meetings, or online exams.

The code uses Python's multiprocessing library to run two processes simultaneously. One process runs the sensor function and the other runs the main function which includes a GUI (Graphical User Interface) using Tkinter.

Installation
------------

The code requires the following packages to be installed:

*   pynput
*   tkinter
*   multiprocessing



To install these packages, open the terminal and type the following command:



```bash
pip install sys pynput time tkinter multiprocessing
```
OR
--
```bash
pip install -r requirements.txt 
```

How it works
------------

The program consists of two functions: `main_` and `sensor`.

### The main\_ function

The `main_` function is responsible for the GUI. It creates a Tkinter window with a clock that updates every second. The function also creates a `loop` function that updates the clock every second. The `loop` function uses the `after` method from Tkinter to call itself every second. This creates a loop that updates the clock every second.

The `main_` function also creates a `close_assistant` function that is called when the user closes the window. This function writes the total time spent being inactive to a log file and sets a flag in a communication file to signal the `sensor` function to stop. Finally, the function closes the Tkinter window and terminates the program.

### The sensor function

The `sensor` function is responsible for detecting if the user is inactive for a certain period of time. The function starts by initializing the time to zero and creating a `checker` function that checks if the `wannaquit` flag is set to True. If the flag is set, the function terminates. Otherwise, the function continues to check if the communication file contains a True flag. If the flag is True, the function writes the time spent being inactive to a log file and terminates the program.

The `sensor` function creates a `timer` function that counts the time spent being inactive. The function starts by initializing a counter to zero and creating a `breakloop` function that is used to break out of the `while` loop if the user presses a key. The `timer` function updates the time every second using the `time.sleep` method.

The `sensor` function also creates a `pretimer` function that runs before the `timer` function. The `pretimer` function counts the time spent being inactive before the `timer` function starts. If the user presses a key during the `pretimer` function, the function resets and starts again. If the user doesn't press a key during the `pretimer` function, the function starts the `timer` function.

The `sensor` function also creates a `conector` function that is called when the user presses a key. The function sets the `breakloop` function to True, which breaks out of the `while` loop in the `timer` function and starts the `pretimer` function again.

Finally, the `sensor` function uses the multiprocessing library to create a process for the `sensor` function and a process for the `main_` function. The `if __name__ =="__main__":` statement starts the two processes.

Conclusion
----------

In conclusion, this code can be useful in scenarios where the user needs to be present and active, like online classes, meetings, or online exams. The code is simple and easy to understand, and it can be modified to suit specific needs.
