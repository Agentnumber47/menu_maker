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
