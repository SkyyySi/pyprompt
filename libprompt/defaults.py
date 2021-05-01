#!/usr/bin/env python3
# This file stores all the default settings used by
# libprompt in order to keep it clean and (hopefully)
# readable. Note: This file also contains settings classes
# for functions that don't have any parameters, both for
# consistancy and to futureproove.
class setting:
	class hostname:
		pass

	class username:
		pass

	class path:
		form = 'fish'

	class exitcode:
		pass

	class checkroot:
		user = '$$'
		root = '#'
	
	class usersym:
		user = '$$'
		root = '#'

	class git:
		prefix             = ['$color.fg.magenta', '[', '$color.fg.reset']
		suffix             = ['$color.fg.magenta', ']', '$color.fg.reset']
		tracked_color      = '$color.fg.green'
		untracked_color    = '$color.fg.yellow'
		tracking_color_end = '$color.fg.reset'

# The reason for this function is that no additional libraries need
# to be imported. For example, the color library would be needed if
# it weren't for this function.
def parsesetting(s):
	def parser(p):
		if (p.startswith('$') and not p.startswith('$$')):
			return(eval(p[1:]))
		elif (p.startswith('$$')):
			return(p[1:])
		else:
			return(p)
	
	if (type(s) == "<class 'list'>"):
		out = ''
		for i in s:
			out += (parser(i))
		return(out)
	else:
		return(parser(s))