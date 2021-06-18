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

class Menu:
    def __init__(self, close_program_command="x", close_program_text="Exit", filler = " ", flanks=("[", "]"), selection_format="A", selection_option ="num", selection_style="enclosed", repeater="*", user_prompt="Select option: ", x_indent=3, x_white=5):
        # Invisible variables
        self.selection_index = 0 # For tracking menu selections
        self.line_count = 3 # Total lines of the menu generated
        self.object = []

        # Customizable Variables
        try:
            self.close_program_command = close_program_command.lower()
        except:
            self.close_program_command = close_program_command
        self.close_program_text = close_program_text
        self.filler = filler
        self.flanks = flanks
        self.repeater = repeater
        self.selection_format = selection_format
        self.selection_option = selection_option
        self.selection_style = selection_style.lower() # selection style (selections: enclosed, open)
        self.user_prompt = user_prompt
        self.x_indent = x_indent
        self.x_white = x_white

    ## Create a heading
    def heading(self, text, repeater=False, x_white=False):
        text.replace("\n", "")
        if not x_white:
            x_white=self.x_white

        whitespace = " "*x_white
        if not repeater:
            repeater = self.repeater

        self.object.append(("H", 1, f"{whitespace}{text}{whitespace}", repeater))

        return

    ## Create a line of repeating character(s)
    def repeat(self, repeater):
        self.object.append(("R", 1, repeater))
        return

    ## Create a line of text
    def line_text(self, text, filler = False, justify="left", x_indent=False,):
        if not x_indent:
            pass
        elif x_indent == True:
            text = f'{" "*self.x_indent}{text}'
        else:
            text = f'{" "*x_indent}{text}'

        if not filler:
            filler=self.filler

        self.object.append(("L", text.count('\n')+1, text, justify.lower(), filler))
        return

    ## Create a blank line
    def blank(self, filler=False):
        if not filler:
            filler = self.filler
        self.object.append(("L", 1, "", "left", filler))
        return

    ## Create a menu selection
    def selection(self, text, execution, filler=False, format=False, selection_option = False, x_indent=False):
        self.selection_index += 1
        ndx = self.selection_index

        if not x_indent:
            x_indent = self.x_indent
        if not filler:
            filler = self.filler

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
            self.object.append(("O", text.count('\n')+1, index, f" {text}", x_indent, execution, filler))
        elif format == "B":
            self.object.append(("O", text.count('\n')+1, text[0], text[1:], x_indent, execution, filler))

        return


    # Generate and display the menu
    def deploy(self, auto_clear=False, no_close_gap=False, debug=False, manual_format=False, x_field=False, y_field=False):

        if not debug or debug.lower() == "crash":
            journal = False
        elif debug.lower() == "log" or debug.lower() == "mixed":
            logging.basicConfig(filename='./menu-maker.log',level=logging.INFO)
            logging.info(f'{compile_time()}: Initializing...\n')
            journal = True
        else:
            print(f"""\nMenu Maker FATAL ERROR:\nDebug "{debug}" is invalid. \n\n VALID:\n 1. LOG\n 2. CRASH\n 3. MIXED""")
            return

        if not no_close_gap: self.object.append(("L", 1, "", "left", self.filler))

        if isinstance(self.close_program_command, list):
            self.object.append(("O", 1, self.close_program_command[0].title(), f" {self.close_program_text}", self.x_indent, exit, self.filler))
        else:
            self.object.append(("O", 1, self.close_program_command, f" {self.close_program_text}", self.x_indent, exit, self.filler))

        for i in self.object:
            self.line_count += i[1]

        first_option_index = 0
        for i in self.object:
            if i[0] == "O":
                break
            else:
                first_option_index += 1
                continue

        if journal: logging.info(f'{compile_time()}: Starting menu loop, then formatting')
        while True:
            menu_tree, selection = {}, 1

            # Determine the display field
            x, y = gts()
            x_field = x if not x_field else x_field
            y_field = y if not y_field else y_field


            # Auto-format if manual_format not specified
            if not manual_format:
                total_blank_lines = (y_field - (self.line_count + 2))
                first_white_lines = int(total_blank_lines/3)
                second_white_lines = first_white_lines*2
                for i in range(0, first_white_lines):
                    self.object.insert(first_option_index, ("L", 1, "", "left", self.filler))
                for i in range(0, second_white_lines):
                    self.object.append(("L", 1, "", "left", self.filler))
            else:
                second_whitespace = "\n"

            if journal:
                logging.info(f'{compile_time()}: Clear screen and cycle menu objects/lines')

            osys('cls' if oname == 'nt' else 'clear') # Clear the screen
            for m in self.object:
                if m[0] == "H":
                    if journal: logging.info(f'{compile_time()}: Constructor: Adding Heading [{m[2]}]')

                    remaining_space = x_field - len(m[2])
                    left_space = int((remaining_space/2)/len(m[3]))
                    right_space = int((remaining_space - int(left_space*len(m[3])))/len(m[3]))

                    if len(m[3]) == 0: l, r = " "*left_space, " "*right_space
                    elif len(m[3]) == 1: l, r = m[3]*left_space, m[3]*right_space
                    else:
                        l, r, repeat_string = repeat_fill(m[3], remaining_space)

                    print(f"{l}{m[2]}{r}")

                elif m[0] == "R":
                    if journal: logging.info(f'{compile_time()}: Constructor: Adding Repeater [{m[2]}]')

                    if len(m[2]) == 0: line = " "*x_field
                    elif len(m[2]) == 1: line = m[2]*x_field
                    else:
                        x, y, line = repeat_fill(m[2], x_field)
                    print(line)

                elif m[0] == "L":
                    if journal: logging.info(f'{compile_time()}: Constructor: Adding Line [{m[1]}]')
                    remaining_space = x_field - len(m[2])
                    l, r, fill_space = repeat_fill(m[4], remaining_space)


                    if m[3].lower() == "left": print(f"{m[2]}{fill_space}")
                    elif m[3].lower() == "center":
                        print(f"{l}{m[2]}{r}")
                    elif m[3].lower() == "right": print(f"{fill_space}{m[2]}")

                elif m[0] == "O":
                    if journal: logging.info(f'{compile_time()}: Constructor: Adding Selection [{m[1]}]')

                    if isinstance(m[2], list):
                        for i in m[2]:
                            menu_tree[f"{str(i).lower()}"] = m[5]
                        line = f"{self.flanks[0]}{m[2][0].title()}{self.flanks[1]}{m[3]}"
                    else:

                        try:
                            menu_tree[f"{m[2].lower()}"] = m[5]
                        except:
                            menu_tree[f"{m[2]}"] = m[5]

                        try:
                            line = f"{self.flanks[0]}{m[2].upper()}{self.flanks[1]}{m[3]} "
                        except:
                            line = f"{self.flanks[0]}{m[2]}{self.flanks[1]}{m[3]} "

                    remaining_space = x_field - len(line)

                    x, y, remainder = repeat_fill(m[6], remaining_space)
                    # l, r = remainder[m[4]:], remainder[:-m[4]]
                    l, r = remainder[:m[4]], remainder[m[4]:]

                    print(f"{l}{line}{r}")

                    selection +=1

            if journal:
                logging.info(f"{compile_time()}: Finishing up display. Selection format set to '{self.selection_format}'")

            for i in range(0, second_white_lines):
                self.object.pop()
            for i in range(0, first_white_lines):
                del self.object[first_option_index]


            if journal: logging.info(f'{compile_time()}: Prompting user for selection')
            user = input(f"{self.user_prompt}").lower()

            if journal: logging.info(f'{compile_time()}: Retrieved input: {user}')

            if auto_clear:
                if journal: logging.info(f'{compile_time()}: auto_clear clears the screen')
                osys('cls' if oname == 'nt' else 'clear')

            if not user:
                continue
            elif user.lower() == self.close_program_command or user.lower() in self.close_program_command:
                if journal: logging.info(f'{compile_time()}: Input quits program [{self.close_program_command}][END]\n')
                exit()

            if journal: logging.info(f'{compile_time()}: Attempting execution...\n')

            if not debug:
                try:
                    menu_tree[user]()
                except:
                    continue

            elif debug.upper() == "LOG":
                try:
                    menu_tree[user]()
                    logging.info(f'{compile_time()}: Execution sucessful. Returning to menu... \n')
                except:
                    logging.info(f'{compile_time()}: input is an invalid entry (check your selection indexes). Returning... \n')
                    continue

            elif debug.upper() == "CRASH" or debug.upper() == "MIXED":
                menu_tree[user]()
                if journal: logging.info(f'{compile_time()}: Execution sucessful. Returning to menu... \n')

        return


def repeat_fill(R, x_span):
    repeat_string = ""
    lx = 0
    for i in range(0, x_span):
        try:
            repeat_string += R[lx]
            lx += 1
        except:
            repeat_string += R[0]
            lx = 1

    l, r = repeat_string[:int(x_span/2)], repeat_string[(x_span-int(x_span/2) - 1):]

    return l, r, repeat_string

def compile_time():
    T = datetime.now()
    return T.strftime("[%d %b %Y] %H:%M:%S")

def say_hi():
    input("Hello World!")
    return

if __name__ == '__main__':
    menu = Menu() # Initialize
    menu.repeat("=[]=X")
    menu.heading("Hello World") # Create a heading that says "Hello World"
    menu.blank()
    menu.line_text("For when you want to say, 'Hello, World!'", justify='center') # Insert a line of text
    menu.selection("Hello!", say_hi) # Create an selection that says hello, and executes the say_hi() function
    menu.deploy()
