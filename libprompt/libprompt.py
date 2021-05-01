#!/usr/bin/env python3
import os
from .defaults  import setting, parsesetting
from socket     import gethostname
from pwd        import getpwuid
from subprocess import Popen, PIPE, call, STDOUT, check_output, DEVNULL
from shutil     import which
from packaging  import version

# The list of modules currently supported. This (hopefull) impoves performance,
# since no "super hacky" way of getting all functions has to be used, but
# instead, it just gets checked if the function is in this list.
_modules = ['$hostname', '$username', '$path', '$usersym', '$git']

####################################################################
#                             HOSTNAME                             #
####################################################################
def hostname():
	host = gethostname()
	return(host)

####################################################################
#                             USERNAME                             #
####################################################################
def username():
	name = getpwuid(os.getuid()).pw_name
	return(name)

####################################################################
#                               PATH                               #
####################################################################

def _short_path(cwd, cwd_full, mode='out'):
	home_full = os.path.expanduser('~')
	home      = home_full.split(sep='/')
	home.pop(0)
	
	path = ''
	out  = ''
	if (cwd_full.startswith(home_full)):
		for i in cwd:
			if (i not in home):
				path += '/'
				path += i
		out += path
		if (mode == 'out'):
			out_tmp  = '~'
			out_tmp += out
			return(out_tmp)
	else:
		if (mode == 'out'):
			return(cwd_full)
	
	if (mode == 'redir'):
		return(out)

def _fish_path(path):
	cwd = str(path).split('/')
	cwd.pop(0)
	out = '~'
	for i in cwd[:-1]:
		out += ('/')
		out += (i[0][0])
	out += '/'
	out += (cwd[-1])
	return(out)

def path(format=parsesetting(setting.path.form)):
	cwd_full = os.getcwd()
	cwd      = cwd_full.split('/')
	cwd.pop(0)
	
	if (format == 'full'):
		return(cwd_full)
	
	if (format == 'fish'):
		path_tmp = str(_short_path(cwd, cwd_full, 'redir'))
		return(_fish_path(path_tmp))
	


####################################################################
#                             EXITCODE                             #
####################################################################
def exitcode():
	return(os.getenv('?'))

####################################################################
#                              USERSYM                             #
####################################################################
def checkroot(user=parsesetting(setting.checkroot.user), root=parsesetting(setting.checkroot.root)):
	if (int(os.geteuid()) == 0):
		return(root)
	else:
		return(user)

def usersym(user=parsesetting(setting.usersym.user), root=parsesetting(setting.usersym.root)):
	return(checkroot(user, root))

####################################################################
#                               GIT                                #
####################################################################
_git_is_in_repo    = call(['env', 'GIT_OPTIONAL_LOCKS=0', 'git', 'rev-parse', '--git-dir'],   stderr=DEVNULL, stdout=DEVNULL)
_git_repo_is_dirty = call(['env', 'GIT_OPTIONAL_LOCKS=0', 'git', 'status',    '--porcelain'], stderr=DEVNULL)

def _git_get():
	if (not command_exists('git')):
		return
	
	git_version = str(check_output(['git', '--version']).decode("utf-8")).split(' ')[-1].rstrip('\n')
	
	if (version.parse(git_version) >= version.parse('2.22')):
		get_current_branch_command = ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
	else:
		get_current_branch_command = ['git', 'branch', '--show-current']
	
	if (_git_is_in_repo == 0):
		current_branch = check_output(get_current_branch_command)
		return(current_branch)

def git(prefix='(', suffix=')', tracked_color='|A|', untracked_color='|B|', tracking_color_end='|C|'):
	if (_git_is_in_repo != 0):
		return
	
	if (_git_repo_is_dirty):
		tracking_color = tracked_color
	else:
		tracking_color = untracked_color
	
	git = _git_get().decode('utf-8').rstrip('\n')
	out = [parsesetting(setting.git.prefix), tracking_color, git, tracking_color_end, suffix]
	return(''.join(out))

#############
# Check if the given command exists.
def command_exists(name):
	return which(name) is not None

# Print a segment without seperating it with a new line.
def printseg(s):
	print(s, sep='', end='')

# Parse the segement list
def _parsesegs(s):
	no_dollar_prefix = (s[1:])
#	function_name    = ('_' + no_dollar_prefix)
	return(no_dollar_prefix)

# Print all segments. The array of segments must be provided
# as an argument.
def print_prompt(seg, shell):
	for i in seg:
		if (i == ':'):
			printseg(i)
		else:
			seg = i.split(':')
			i   = ''.join(seg[0])
			if (seg[0] in _modules):
				segment = _parsesegs(seg[0])
				#args = ''.join(seg[1:])
				
				args = ''
				if (seg):
					for i in seg[1:]:
						#arg   = ''.join(i)
						args += ("'" + i + '' + "'")
				
				if (segment):
					function = eval(segment + '(' + args + ')')
				else:
					function = eval(segment + '()')
				printseg(function)
			else:
				printseg(i)