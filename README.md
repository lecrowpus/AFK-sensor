AFK Sensor in Python
====================

Have you ever found yourself inactive for too long at your computer and wanted a way to track your idle time? Look no further! In this tutorial, we will be discussing the AFK (Away From Keyboard) Sensor in Python.

An AFK Sensor is a program that tracks the amount of time a user is inactive on their computer. The program runs in the background and can be triggered by keyboard or mouse movements. In this tutorial, we will be building two Python files that will make up the AFK Sensor.

The first file, named `afksensor.py`, will be responsible for tracking the idle time of the user. The second file, named `main.py`, will be responsible for starting the AFK Sensor and displaying the timer.



Installation and Requirements for Afksenour in Python
-----------------------------------------------------

Installation:
-------------

To install Afksenour, you will need to have Python 3 installed on your system. You can download Python 3 from the official website [https://python.org/](https://python.org/).

Once you have Python 3 installed, you can then download the source code from GitHub by clicking the "Clone or Download" button.

Requirements:
-------------

Afksenour requires the following packages to be installed:

1.  sys
2.  pynput
3.  time
4.  tkinter (for GUI version)

To install these packages, open the terminal and type the following command:



```bash
pip install sys pynput time tkinter
```
OR
--
```bash
pip install -r requirements.txt 
```

Usage:
------

There are two files included in this repository: `afksensour.py` and `main.py`.

The `afksensour.py` file contains the core logic for the Afksenour. It uses the pynput library to detect keyboard inputs and calculate the time spent on the computer.

The `main.py` file contains the GUI for Afksenour. It displays the time spent on the computer and allows you to start and stop the timer.

To run Afksenour, simply open the terminal and run the following command:



```bash
python main.py
```

With Afksenour, you can keep track of how much time you spend on your computer and make sure to take breaks to avoid eye strain and other health problems.

afksensor.py
------------

The `afksensor.py` file uses the `pynput` library to detect keyboard movements. It contains the following functions: `timer`, `pretimer`, and `afk_f`.

The `timer` function starts the actual idle time tracking. It keeps track of the hours, minutes, and seconds the user has been inactive. The `pretimer` function runs for 10 seconds before the `timer` function starts. This gives the user the chance to interrupt the AFK Sensor before it starts tracking their idle time. The `afk_f` function is used to reset the `pretimer` if the user presses a key during the 10 seconds.

The `checker` function is used to check if the main program wants to close the AFK Sensor. The `breakloop` function is used to break the `timer` loop if a key is pressed.

main.py
-------

The `main.py` file uses the `Tkinter` library to create a graphical user interface (GUI) for the AFK Sensor. It contains the following functions: `loop` and `close_assistant`.

The `loop` function starts the timer and updates the timer display in the GUI. The `close_assistant` function is used to close the AFK Sensor and write the end time to a text file named `log-time.txt`.

Conclusion
----------

The AFK Sensor in Python is a great tool for keeping track of your idle time on your computer. By using the `pynput` and `Tkinter` libraries, we were able to create a simple and efficient program. Try building this project yourself and see how you can improve upon it. Happy coding!
