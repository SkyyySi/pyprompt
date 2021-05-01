#!/usr/bin/env python3
# This script was just for testing some stuff without modifying libprompt.py directly.
# I'll probably remove it at some point.
from os  import getcwd, environ
from sys import argv

supported_shells = ['bash', 'zsh']

def defcolor(mode):
	global color
	# Bash is picky about the color format
	if (mode == 'bash'):
		class color:
			reset_all         = '\001\033[00m\002'
			class fg:
				grey          = '\001\033[30m\002'
				red           = '\001\033[31m\002'
				green         = '\001\033[32m\002'
				yellow        = '\001\033[33m\002'
				blue          = '\001\033[34m\002'
				magenta       = '\001\033[35m\002'
				cyan          = '\001\033[36m\002'
				light_gray    = '\001\033[37m\002'
				dark_gray     = '\001\033[90m\002'
				ligth_red     = '\001\033[91m\002'
				ligth_green   = '\001\033[92m\002'
				ligth_yellow  = '\001\033[93m\002'
				ligth_blue    = '\001\033[94m\002'
				ligth_magenta = '\001\033[95m\002'
				ligth_cyan    = '\001\033[96m\002'
				ligth_white   = '\001\033[97m\002'
				reset         = '\001\033[39m\002'
			class bg:
				grey          = '\001\033[40m\002'
				red           = '\001\033[41m\002'
				green         = '\001\033[42m\002'
				yellow        = '\001\033[43m\002'
				blue          = '\001\033[44m\002'
				magenta       = '\001\033[45m\002'
				cyan          = '\001\033[46m\002'
				light_gray    = '\001\033[47m\002'
				dark_gray     = '\001\033[100m\002'
				ligth_red     = '\001\033[101m\002'
				ligth_green   = '\001\033[102m\002'
				ligth_yellow  = '\001\033[103m\002'
				ligth_blue    = '\001\033[104m\002'
				ligth_magenta = '\001\033[105m\002'
				ligth_cyan    = '\001\033[106m\002'
				ligth_white   = '\001\033[107m\002'
				reset         = '\001\033[49m\002'
			class style:
				# Note: Most terminals and shells don't support some of these, so
				# you're better of only using bold, itallic and underlined text if
				# you want to share your theme with others.
				bold          = '\001\033[1m\002'
				dim           = '\001\033[2m\002'
				underlined    = '\001\033[4m\002'
				blink         = '\001\033[5m\002'
				reverse       = '\001\033[7m\002'
				hidden        = '\001\033[8m\002'
				no_bold       = '\001\033[21m\002'
				no_dim        = '\001\033[22m\002'
				no_underlined = '\001\033[24m\002'
				no_blink      = '\001\033[25m\002'
				no_reverse    = '\001\033[27m\002'
				no_hidden     = '\001\033[28m\002'
	# Zsh has a much nicer format for printing colors
	elif (mode == 'zsh'):
		class color:
			reset_all         = '%{\033[00m%}'
			class fg:
				grey          = '%F{0}'
				red           = '%F{1}'
				green         = '%F{2}'
				yellow        = '%F{3}'
				blue          = '%F{4}'
				magenta       = '%F{5}'
				cyan          = '%F{6}'
				light_gray    = '%F{7}'
				dark_gray     = '%F{8}'
				ligth_red     = '%F{9}'
				ligth_green   = '%F{10}'
				ligth_yellow  = '%F{11}'
				ligth_blue    = '%F{12}'
				ligth_magenta = '%F{13}'
				ligth_cyan    = '%F{14}'
				ligth_white   = '%F{15}'
				reset         = '%f'
			class bg:
				grey          = '%K{0}'
				red           = '%K{1}'
				green         = '%K{2}'
				yellow        = '%K{3}'
				blue          = '%K{4}'
				magenta       = '%K{5}'
				cyan          = '%K{6}'
				light_gray    = '%K{7}'
				dark_gray     = '%K{8}'
				ligth_red     = '%K{9}'
				ligth_green   = '%K{10}'
				ligth_yellow  = '%K{11}'
				ligth_blue    = '%K{12}'
				ligth_magenta = '%K{13}'
				ligth_cyan    = '%K{14}'
				ligth_white   = '%K{15}'
				reset         = '%k'
			class style:
				# Note: Most terminals and shells don't support some of these, so
				# you're better of only using bold and underlined text if you want
				# to share your theme with others.
				bold         = '%B'
				dim          = '%{\033[2m%}'
				underline    = '%U'
				blink        = '%{\033[5m%}'
				reverse      = '%S'
				hidden       = '%{\033[8m%}'
				no_bold      = '%b'
				no_dim       = '%{\033[22m%}'
				no_underline = '%u'
				no_reverse   = '%s'
				no_reverse   = '%{\033[28m%}'

def main():
	global shell
	if (str(argv[1])):
		shell = (str(argv[1]))
	elif (str(environ('PYPROMPT_SHELL'))):
		shell = (str(environ('PYPROMPT_SHELL')))
	else:
		print('No shell defined! Either pass one as an argument or\nset the `PYPROMPT_SHELL`environment variable. ')
		return

	if (not shell in supported_shells):
		print('The shell "', shell, '" is (currently) not supported! ', sep='')
		return

	#print(shell)
	defcolor(shell)

	#print(color.reset_all)
#	print(color.fg.blue, getcwd(), color.reset_all, '$ ', sep='')   # Commented out so vscode doesn't complain ;)

if __name__ == "__main__":
	main()