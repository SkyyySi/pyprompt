#!/usr/bin/env python3
import libprompt.libprompt as libprompt
from sys       import argv
from os        import environ
from importlib import import_module
#from libprompt.color  import color_zsh as color

# List of supported shells.
supported_shells = ['bash', 'zsh']

# The shell you want to use
global shell
if (str(argv[1])):
	shell = (str(argv[1]))
elif (str(environ('PYPROMPT_SHELL'))):
	shell = (str(environ('PYPROMPT_SHELL')))
else:
	print('No shell defined! Either pass one as an argument or\nset the `PYPROMPT_SHELL`environment variable.')
	exit

# Exit if the given shell .
if (not shell in supported_shells):
	print('The shell "', shell, '" is (currently) not supported! ', sep='')
	exit

# Import the color library.
_color_type  = 'color_'
_color_type += shell
global color
color = getattr(import_module('libprompt.color'), _color_type)

# Use a diffrent color depending on if the user is root or not.
# User comes first, root comes second.
usercolor = libprompt.checkroot(color.fg.green, color.fg.red)

class git_format:
	prefix             = (color.fg.magenta + '[' + color.fg.reset)
	suffix             = (color.fg.magenta + ']' + color.fg.reset)
	tracked_color      = (color.fg.green)
	untracked_color    = (color.fg.yellow)
	tracking_color_end = (color.fg.reset)

git = ('$git:' + git_format.prefix + ':' + git_format.suffix + ':' + git_format.tracked_color + ':' + git_format.untracked_color + ':' + git_format.tracking_color_end)

# List of prompt segments
segments = [usercolor, '$hostname', '@', '$username', color.reset_all, ':', '$path:fish', git, '$usersym', ' ']

def main(segments, shell):
	pass
	#print(color.fg.green, color.bg.red, 'Hello world!', color.reset_all, sep='')
	libprompt.print_prompt(segments, shell)


if __name__ == "__main__":
	main(segments, shell)