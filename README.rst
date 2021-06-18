Menu Maker
==========

Menu Maker is a menu generator for python code that runs in the shell.

.. image:: /images/example.png
    :width: 668
    :height: 448
    :alt: Example


* Github - https://github.com/Agentnumber47/menu_maker
* PyPi - https://pypi.org/project/menu-maker/

Contents
--------
.. contents::

Installation
------------
Menu Maker can be copied from source (at the GitHub link), or installed through pip::

    pip install menu-maker

Using the library
-----------------

In order to use Menu Maker, a 'Menu' must be constructed and then it must be deployed.

Constructing
............

First, import the library, then define a variable that uses ``.Menu()``.

.. code-block:: python

    # Import the library
    from maker import maker

    # Define a variable that uses .Menu()
    menu_object = maker.Menu()


To build out a Menu, you have several options:

1. Heading: ``menu_object.heading(text)``
2. Repeat: ``menu_object.repeat("*")``
3. Text Line: ``menu_object.line_text(text)``
4. Blank Line: ``menu_object.blank()``
5. Option: ``menu_object.selection(text, function)``

After the menu code is constructed, use ``.deploy(menu_object)``. By default, the program will present your construction in a pleasing way for you. It's that simple to get started! And if you never need more than this, then groovy.

Here's a working example of how to build and deploy a functional program with a menu

.. code-block:: python

  from maker import maker

  def main():
      # Construct the menu
      hello_menu = maker.Menu() # Initialize
      hello_menu.repeat("=[]=X") # Create a line of the repeated text "=[]=X"
      hello_menu.heading("Hello World") # Create a heading that says "Hello World"
      hello_menu.blank() # Insert a blank line
      hello_menu.line_text("For when you want to say, 'Hello, World!'") # Insert a line of text
      hello_menu.selection("Hello!", say_hi) # Create an option that says hello > execute say_hi()

      # Generate and deploy the menu
      hello_menu.deploy(auto_clear=True)

  def say_hi():
      input("Hello World!")

  if __name__ == '__main__':
      main()

If something is not working with the menu you made, troubleshoot by enabling one of the debug modes.

.. code-block:: python

    # Deploy the menu object with debug set to logging
    menu_object.deploy(debug='LOG')

1. ``debug='CRASH'`` If it receives a non-fatal error, crash the program.
2. ``debug='LOG'`` Copy all library behavior in a log, where errors will be detailed.
3. ``debug='MIXED'`` Do both 1 and 2.

Don't forget to disable it before launch, or you're gonna have a bad time.

API Documentation (Plain English Edition)
=========================================

If you wish to see the 'hello world' example in action, run the maker as a program.

This documentation is more technically a quick tutorial to tell you about proper use, what it's capable of, and where to look if you want to do something specific. It's fairly intuitive and lenient, so feel free to try to stretch its limits and forgiveness. We will be breaking down the "Hello World" example.

1. Thinking in Menus
2. The Components...
3. ... and Their Uses

1. Thinking in Menus
--------------------

So you've installed it, now what?

Now you use it! After you learn to, and learning is fun. So it wasn't really now, more like soon. My delete keys don't work, which you'd know if you saw the current state of my code.

Anyway, a menu obviously enables your user to interact with your code. Therefore, it needs to present the information to the user and give them a way to choose how they engage. Menu Maker allows you to sequentially compile your menu as you see it while reducing the hassle in doing so manually. It's a CLI menu engine. Not much, but it serves its purpose.

We'll get more detailed later, but the blueprint - what the program automates - is contained in the ``Menu()`` class that needs to be called first. If the cookie cutter format that can be seen in the 'Hello World' example works for you - it's functional and pretty as-is - then you never have to read beyond this tutorial.

As always, import the library into your code.

.. code-block:: python

    # Import the library
    from maker import maker

There are only 3 elements that must be included in each implementation. In order:

1. You need to declare a menu. Name it anything. ``anything = maker.Menu()``
2. You need to offer a selection. ``anything.selection("Selection", selection_function)``
3. You need to run the menu. ``anything.deploy()``

That's the minimum to run a program (as long as the selection directs to a valid function). What's left is the information you want to present and how you want to present it.

2. The Components...
--------------------

The library breaks down a menu screen line by line. By default it will take care of presentation; you just need to tell it what you want it to say. There are no requirements to how you want to arrange things. Use a header as a footer, the world is your oyster. The only requirement as of this version (stay tuned!) is that the user prompt must come at the bottom/end. I could see this easily being abused to make bad design choices, but I trust you.

``menu_object.heading(text)``
.........................

The first component is the ``heading``. The ``heading`` is basically a line with text in the center, surrounded by (optionally) whitespace, then a repeating character to go to the edge of the field of display. It's symmetrical and pretty, and breaks up what you're looking at.

.. code-block:: python

    # Create a heading line
    hello_menu.heading("Hello World")

    # Output:
    # *****     Hello World     *****

``menu_object.repeat("*")``
.......................

``.repeat`` is simply a modified ``heading``. It's the repeating character(s) minus the text and whitespace.

.. code-block:: python

    # Create a line of repeating character(s)
    hello_menu.repeat("=[]=X")

    # Output:
    # =[]=X=[]=X=[]=X=[]=X=[]=X


``menu_object.line_text(text)``
...........................

``.line_text`` is simply a string of text.

.. code-block:: python

    # Create a line of text
    hello_menu.line_text("For when you want to say, 'Hello, World!'")

    # Output:
    # For when you want to say, 'Hello, World!'

``menu_object.blank()``
...................

``.blank`` is simply a blank line.

.. code-block:: python

    # Create a blank line
    hello_menu.blank()

    # Output:
    #

``menu_object.selection(text, function)``
.....................................

``.selection`` is the heart of any menu. This will allow the user to choose which function your program executes.

.. code-block:: python

    # Create a menu selection
    hello_menu.selection("Hello!", say_hi)

    # Output
    #   [1] Hello!


3. ... and Their Uses
---------------------

The default settings, the blueprint, the way you want Menu Maker to automatically format your creation, can be defined via two methods. Either (1) when you first declare it, or (2) elsewhere in your code. Let's say you want to set the selection indentation a notch higher from 3 spaces to 4:

.. code-block:: python

  # 1
  menu_object = maker.Menu(x_indent=4)

  # 2
  menu_object.x_indent = 4

A benefit of 2 is the ability to change a setting based upon what the user does. The purpose of using these as a default is just to make things uniform more easily, but you may change any setting for any individual component you wish, as long as it applies.

.. code-block:: python

    # 3
    hello_menu.selection("Hello!", say_hi, x_indent=4)

**If you ever want to change more than one setting, separate them by commas.**

You can effect more than just the formatting with ``Menu()``.

You can change how the maker exits the program, how the exit is labeled, how the menu prompts the user, and how it indexes ``selection``.

All settings and options are fully and extensively detailed in the Technical Edition of this documentation. If you have an idea, just check the applicable section. Note that some settings may be incompatible.

If anything isn't working properly, use the debug mode in ``.deploy()``.

The last essential element is ``.deploy()`` and runs your construction. You have a few ways to set this up different as well. Beyond the ``debug`` setting, you can set it to automatically clear the screen before it attempts to execute the user input with ``auto_clear``. If you don't want Menu Maker to automatically format the blank lines added for whitespace, switch ``manual_format`` to True.

Lastly, by default, the maker determines the size of the shell window and uses it to format to those specifications. This space is referred to as the 'field.' Technically speaking, the horizontal ``x_field`` is the amount of characters from the leftmost to rightmost, and the vertical ``y_field`` is the amount of lines. If you wish to override the automatic calculation (for instance, if you want to ensure the same display for every field larger than a certain size) this is the place.


API Documentation (Technical Edition)
=====================================

**NOTE** Optional arguments are to be separated by commas.

1. ``maker.Menu()``
---------------

* Purpose: Create a menu object to be later deployed.

* **Note**: to modify the following settings, either pass an argument in the class call (Ex. ``menu_object = Menu(selection_style="open")``) or edit the variable using the format ``var.setting = setting`` . (Ex. ``menu_object.selection_style = 'open'``)

``Menu()`` selections are intended to create formatting standards for your menus.

Changing these settings will not stop you from customizing the format of individual menu elements.

Optional Arguments
..................
(as set to their defaults)

``close_program_command="X"``
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

* Purpose: When the user enters this at the menu prompt, the program closes. May use a list (first will be displayed) or string.

``close_program_text="Exit"``
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

* Purpose: The label for the selection to exit the program.

``filler = " "``
,,,,,,,,,,,,,,
* Purpose: The default filler when you want something to be blank.

``flanks=("[", "]")``
,,,,,,,,,,,,,,,,,,,,,

* Purpose: Define the characters that compose the enclosure of a selection index.

Ex. Using the default settings would produce "[1]".

``selection_format="A"``
,,,,,,,,,,,,,,,,,,,,,,,,
* Purpose: Decide the format for selection entries.

* Choices::

    1. "A": Use the format: "[Index] Text"
    2. "B": Use the format: "[T]ext"

``selection_option ="num"``
,,,,,,,,,,,,,,,,,,,,,,,,,,,

* Purpose: Set the default selection indexing option.

* **NOTE** You may specify custom indexes when constructing the menu. See ``.selection`` below for more details.

* Choices::

    1. "num"  | Index sequentially by number. (Ex. 1, 2, 3...)
    2. "char" | Index sequentially by character. (Ex. A, B, C...)
    3. "yn"   | Index "Yes" and "No". Requires 2 selections exactly ("Yes" first).
              | Additionally, (Y or 1) and (N or 0) both work to execute functions.
    4. "bool" | Index "True" and "False". Requires 2 selections exactly ("True" first).
              | Additionally, (T or 1) and (F or 0) both work to execute functions.

``selection_style="enclosed"``
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
* Purpose: Define the styling for ``selection`` entries.

* Choices::

    1. "Enclosed": A character (or string of characters) that precede and follow a selection index.
          In the example "[1]", the brackets ("[]") enclose the index (the number 1).
          NOTE: If you select enclosure, you may choose to only specify characters on one side.
          See 'flanks' below for more details.

    2. "Open": No characters enclose the selection index. Ex. 2

``repeater="*"``
,,,,,,,,,,,,,,,,

* Purpose: Set the default repeating character[s] for ``heading`` elements.

* NOTE: You may specify more than one character in the string.

``user_prompt="Select option: "``
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
* Purpose: Define how the menu prompts user for input.

``x_indent=3``
,,,,,,,,,,,,,,
* Purpose: Set the default amount of spaces when indenting.

* NOTE: Options indent using this value by default, and lines may be set to indent by this value.

``x_indent`` requires an ``int``

``x_white=5``
,,,,,,,,,,,,,,
* Purpose: In the ``heading``, set the amount of spaces between the ``repeater`` and ``heading`` ``text``.

* The default value of ``5`` makes up the two blocks of five spaces in the example ``****     Head     ****``

``x_white`` requires an ``int``

2. ``menu_object.deploy()``
------------------------
* Purpose: Deploys (generates and instantiates) your constructed menu.

Optional Arguments
..................

``auto_clear=False``
,,,,,,,,,,,,,,,,
* Purpose: Force the menu to clear the screen before executing the function.

* Choices::

    1. False
    2. True

``debug=False``
,,,,,,,,,,,
* Purpose: Set the debug mode.

* Choices::

    1. False: Debug mode off.
    2. 'LOG': Record library activity to a log.
    3. 'CRASH': Crash the program if it runs into an error.
    4. 'MIXED': Both 2 and 3.

``manual_format=False``
,,,,,,,,,,,,,,,,,,,
* Purpose: When off (``False``), the library will automatically add blank lines to fill out the interface.

* Choices::

    1. False
    2. True

``no_close_gap=False``
,,,,,,,,,,,,,,,,
* Purpose: When off (``False``), the program will automatically add a blank line between your last option and the close program option.

* Choices::

    1. False
    2. True


``x_field=False``
,,,,,,,,,,,,,,
* Purpose: Specify the amount of characters to format the menu within. Will query the terminal display size by default.

* Choices::

    1. False
    2. int

``y_field=False``
,,,,,,,,,,,,,
* Purpose: Specify the amount of lines to format the menu within. Will query the terminal display size by default.

* Choices::

    1. False
    2. int

Menu Constructor Objects
-------------------------
NOTE: All menu components will follow the style settings (referred to as the 'default').
Use optional arguments if you want to override those settings, for the component you are using.

3. ``menu_object.heading(text)``
----------------------------
* Purpose: Create a ``heading`` line.

Optional Arguments
..................

``repeater="*"``
,,,,,,,,,,,,
* Purpose: Specify the repeating character(s) for the ``heading``.

**NOTE** Using too many characters will cause a bug in the formatting.

``x_white=3``
,,,,,,,,,,,,,,,
* Purpose: Amount of whitespace (quantified in characters) between the ``heading`` ``text`` and the border/repeating character.

4. ``menu_object.repeat("*")``
------------------------------
* Purpose: Create a line entirely of repeating character(s).

5. ``menu_object.line_text(text)``
-------------------------------
* Purpose: Create a line of text.

Optional Arguments
...................
``filler=" "``
,,,,,,,,,,,,,,
* Purpose: Set the whitespace filler.

``justify="left"``
,,,,,,,,,,,,,,,,,,
* Purpose: Set text justification for the line.

* Choices::

    1. 'left'
    2. 'center'
    3. 'right'

``x_indent=int``
,,,,,,,,,,,,,,,,
* Purpose: Amount of whitespace (quantified in characters) before the line text starts.

6. ``menu_object.blank()``
--------------------------
* Purpose: Create a blank line.

Optional Arguments
------------------

``filler = " "``
,,,,,,,,,,,,,,
* Purpose: The default filler when you want something to be blank.

7. ``menu_object.selection(text, function)``
--------------------------------------------
* Purpose: Create an option for the user to select from the menu.
- ``text`` is the text that is displayed to the user.
- The function should refer to program code (ie. ``program.my_function``). Do not put in quotations or include the parenthesis.

Optional Arguments
..................

``format=False``
,,,,,,,,,,,,,,,,
* Purpose: Decide the format for option entries.

* Choices::

    1. False: Use default.
    2. "A": Use the format: "[Index] Text"
    3. "B": Use the format: "[T]ext"

``option_option = False``
,,,,,,,,,,,,,,,,,,,,,,,,,
* Purpose: Set the default indexing option, for options.

**See** ``selection_option`` under ``maker.Menu()`` for full details. Use ``False`` for default setting.

``x_indent=int``
,,,,,,,,,,,,,,,,
* Purpose: Amount of whitespace (quantified in characters) before the line text starts.


FINAL NOTES
===========
(besides the version notes, but of the interesting stuff, I mean)

The best way to learn the capabilities is to just mess around with it. Try it on default, then try radically changing it, and start tweaking from there. I tried to make it as straightforward as possible.

I make a lot of menus and so this was mainly to speed up my own work. This is my first library. Thank you for trying it out!
Menu Maker will forever be FOSS, but consider throwing me a literal buck or two here: https://www.buymeacoffee.com/agentnumber47
If you wish to see what else I might be working on: https://github.com/Agentnumber47

Suggestions and feedback are welcome, and you're pretty much free to do what you like with the code, but I'm not seeking any contributors.

BORING AND TECHNICAL
====================

Version Notes
-------------
17 Jun 2021 v0.5.2: UV: Some bugfixes and tweaks. Added ``filler``, ``no_close_gap``.

12 Jun 2021 v0.5: Unveiling: The first workable version of the program, halfway to the first final form. Not entirely optimized, nor combed over for efficiency, but does what it is supposed to. Also, not all features possible, but enough to be feature-rich. More can be done to give user-friendly options for ends that currently require creative customization.

CURRENT LIMITATIONS
-------------------
To be fixed or expanded or whatever.

- No way to pass an argument to a function called by the option.
- The user prompt must come at the ending.

TO COME
-------
(ordered by priority)

- Add more debug features
- Add an offset optional argument to .repeat.
- Integrate time
- Hidden exit key
