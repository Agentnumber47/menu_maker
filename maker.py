#! /usr/bin/env python

# Menu Maker, by AgentNumber47
# Library for generating menus, for use in shell (terminal) programs.
# 12 Jun 2021: v0.5: Unveiling

import logging
from datetime import datetime
from shutil import get_terminal_size as gts
from os import system as osys
from os import name as oname

ALPHA = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"x", 24:"y", 25:"z"}
YND = {1:["yes", "y", "1"], 2:["no","n", "0"]}
BOOL = {1:["true", "t", "1"], 2:["false","f", "0"]}

def check_x_y_manual(x_field, y_field):
    x_manual, y_manual = False, False
    if not x_field:
        x_manual = False
    if not y_field:
        y_manual = False
    return x_manual, y_manual

def main():
    Menu()
    return


class Menu:
    def __init__(self, close_program_command="x", close_program_text="Exit", flanks=("[", "]"), selection_format="A", selection_option ="num", selection_style="enclosed", repeater="*", user_prompt="Select option: ", x_indent=3, x_white=5):
        # Invisible variables
        self.selection_index = 0 # For tracking menu selections
        self.line_count = 3 # Total lines of the menu generated
        self.object = []

        # Customizable Variables
        self.selection_style = selection_style.lower() # selection style (selections: enclosed, open)
        self.selection_format = selection_format
        self.flanks = flanks
        self.repeater = repeater
        self.x_indent = x_indent
        self.x_white = x_white
        self.selection_option = selection_option
        self.user_prompt = user_prompt
        self.close_program_text = close_program_text
        try:
            self.close_program_command = close_program_command.lower()
        except:
            self.close_program_command = close_program_command

    ## Create a heading
    def heading(self, text, repeater=False, x_white=False):
        text.replace("\n", "")
        if not x_white:
            x_white=self.x_white

        whitespace = " "*x_white
        if not repeater:
            repeater = self.repeater

        self.object.append(("H", f"{whitespace}{text}{whitespace}", repeater))
        self.line_count +=1

        return

    ## Create a line of repeating character(s)
    def repeat(self, repeater):
        self.object.append(("R", repeater))
        self.line_count +=1
        return

    ## Create a line of text
    def line_text(self, text, justify="left", x_indent=False):
        if not x_indent:
            pass
        elif x_indent == True:
            text = f'{" "*self.x_indent}{text}'
        else:
            text = f'{" "*x_indent}{text}'


        self.object.append(("L", text, justify.lower()))
        self.line_count += text.count('\n')+1
        return

    ## Create a blank line
    def blank(self):
        self.object.append(("L", " ", "left"))
        self.line_count +=1
        return

    ## Create a menu selection
    def selection(self, text, execution, format=False, selection_option = False, x_indent=False):
        self.selection_index += 1
        ndx = self.selection_index

        if not x_indent:
            x_indent = self.x_indent

        if not selection_option:
            opt = self.selection_option
        else:
            opt = selection_option

        if not format:
            format = self.selection_format

        if format == "A":
            if opt == "num":
                index = ndx
            elif opt == "char":
                index = ALPHA[ndx]
            elif opt == "yn":
                index = YND[ndx]
            elif opt == "bool":
                index = BOOL[ndx]
            else:
                index = selection_option
            self.object.append(("O", index, f" {text}", x_indent, execution))
        elif format == "B":
            self.object.append(("O", text[0], text[1:], x_indent, execution))

        self.line_count += text.count('\n')+1
        return


    # Generate and display the menu
    def deploy(self, auto_clear=False, debug=False, manual_format=False, x_field=False, y_field=False):
        if not debug or debug.lower() == "crash":
            journal = False
        elif debug.lower() == "log" or debug.lower() == "mixed":
            logging.basicConfig(filename='./menuerator.log',level=logging.INFO)
            time = time_thing()
            logging.info(f'{time}: Initializing...\n')
            journal = True
        else:
            print(f"""\nMenuerator FATAL ERROR:\nDebug "{debug}" is invalid. \n\n VALID:\n 1. LOG\n 2. CRASH\n 3. MIXED""")
            return

        x_manual, y_manual = check_x_y_manual(x_field, y_field)

        selection_block = False

        if journal:
            time = time_thing()
            logging.info(f'{time}: Starting menu loop, then formatting')
        while True:
            menu_tree = {}
            selection = 1
            if not x_manual and not y_manual:
                x_field, y_field = gts()
            elif x_manual and not y_manual:
                q, y_field = gts()
            elif not x_manual and y_manual:
                x_field, q = gts()

            if not manual_format:
                total_blank_lines = (y_field - (self.line_count + 2))
                first_white_lines = int(total_blank_lines/3)
                second_white_lines = first_white_lines*2
                first_whitespace = "\n"*first_white_lines
                second_whitespace = "\n"*second_white_lines
            else:
                second_whitespace = "\n"

            if journal:
                time = time_thing()
                logging.info(f'{time}: Clear screen and cycle menu objects/lines')
            osys('cls' if oname == 'nt' else 'clear') # Clear the screen
            for m in self.object:
                time = time_thing()
                if m[0] == "H":
                    if journal: logging.info(f'{time}: Constructor: Adding Heading [{m[1]}]')
                    remaining_space = x_field - len(m[1])

                    left_space = int((remaining_space/2)/len(m[2]))
                    right_space = int((remaining_space - int(left_space*len(m[2])))/len(m[2]))

                    if len(m[2]) == 0:
                        print(" "*x_field)
                    elif len(m[2]) == 1:
                        l = m[2]*left_space
                        r = m[2]*right_space
                    else:
                        line = ""
                        lx = 0
                        for i in range(0, remaining_space):
                            try:
                                line += m[2][lx]
                                lx += 1
                            except:
                                line +=m[2][0]
                                lx=1

                        half_remain = int(remaining_space/2)
                        l = line[half_remain:]
                        r = line[:(remaining_space-half_remain)]

                    print(f"{l}{m[1]}{r}")

                elif m[0] == "R":
                    if journal: logging.info(f'{time}: Constructor: Adding Repeater [{m[1]}]')

                    if len(m[1]) == 0:
                        print(" "*x_field)
                    elif len(m[1]) == 1:
                        multiplier = int(x_field/len(m[1]))
                        print(m[1]*multiplier)
                    else:
                        rx = 0
                        line = ""
                        for i in range(0, x_field):
                            try:
                                line += m[1][rx]
                                rx += 1
                            except:
                                line +=m[1][0]
                                rx=1
                    print(line)

                elif m[0] == "L":
                    if journal: logging.info(f'{time}: Constructor: Adding Line [{m[1]}]')
                    if m[2] == "left":
                        print(m[1])
                    elif m[2] == "center":
                        print(m[1].center(x_field, " "))
                    elif m[2] == "right":
                        print(m[1].rjust(x_field, " "))

                elif m[0] == "O":
                    if journal: logging.info(f'{time}: Constructor: Adding Selection [{m[1]}]')
                    if not selection_block and not manual_format:
                        print(first_whitespace)
                        selection_block = True
                    indent = " "*m[3]

                    if isinstance(m[1], list):
                        for i in m[1]:
                            menu_tree[f"{str(i).lower()}"] = m[4]
                        print(f"{indent}{self.flanks[0]}{m[1][0].title()}{self.flanks[1]}{m[2]}")
                    else:

                        try:
                            menu_tree[f"{m[1].lower()}"] = m[4]
                        except:
                            menu_tree[f"{m[1]}"] = m[4]

                        try:
                            print(f"{indent}{self.flanks[0]}{m[1].upper()}{self.flanks[1]}{m[2]}")
                        except:
                            print(f"{indent}{self.flanks[0]}{m[1]}{self.flanks[1]}{m[2]}")

                    selection +=1

            if journal:
                time = time_thing()
                logging.info(f"{time}: Finishing up display. Selection format set to '{self.selection_format}'")
            selection_block = False

            if self.selection_format == "A":
                if isinstance(self.close_program_text, list):
                    print(f"\n{indent}{self.flanks[0]}{self.close_program_command}{self.flanks[1]} {self.close_program_text}")
                else:
                    print(f"\n{indent}{self.flanks[0]}{self.close_program_command[0].title()}{self.flanks[1]} {self.close_program_text}")
            elif self.selection_format == "B":
                if isinstance(self.close_program_text, list):
                    print(f"\n{indent}{self.flanks[0]}{self.close_program_command}{self.flanks[1]}{self.close_program_text}")
                else:
                    print(f"\n{indent}{self.flanks[0]}{self.close_program_command[0].title()}{self.flanks[1]}{self.close_program_text}")

            if journal:
                time = time_thing()
                logging.info(f'{time}: Prompting user for selection')


            user = input(f"{second_whitespace}{self.user_prompt}").lower()

            if auto_clear:
                osys('cls' if oname == 'nt' else 'clear')
                if journal:
                    time = time_thing()
                    logging.info(f'{time}: auto_clear clears the screen')

            if journal:
                time = time_thing()
                logging.info(f'{time}: Retrieved input: {user}')

            if not user:
                continue

            elif user.lower() == self.close_program_command or user.lower() in self.close_program_command:
                if journal:
                    time = time_thing()
                    logging.info(f'{time}: Input quits program [{self.close_program_command}][END]\n')
                exit()

            if journal:
                time = time_thing()
                logging.info(f'{time}: Attempting execution...\n')

            if not debug:
                try:
                    menu_tree[user]()
                except:
                    continue

            elif debug.upper() == "LOG":
                time = time_thing()
                try:
                    menu_tree[user]()
                    logging.info(f'{time}: Execution sucessful. Returning to menu... \n')
                except:
                    logging.info(f'{time}: input is an invalid entry (check your selection indexes). Returning... \n')
                    continue

            elif debug.upper() == "CRASH" or debug.upper() == "MIXED":
                menu_tree[user]()
                if journal:
                    time = time_thing()
                    logging.info(f'{time}: Execution sucessful. Returning to menu... \n')

        return


def time_thing():
    T = datetime.now()
    return T.strftime("[%d %b %Y] %H:%M:%S")

def say_hi():
    input("Hello World!")
    return

# if __name__ == '__main__':
#     menu = Menu() # Initialize
#     menu.repeat("=[]=X")
#     menu.heading("Hello World") # Create a heading that says "Hello World"
#     menu.blank() # Insert a blank line
#     menu.line_text("For when you want to say, 'Hello, World!'") # Insert a line of text
#     menu.selection("Hello!", say_hi) # Create an selection that says hello, and executes the say_hi() function
#     menu.deploy()
