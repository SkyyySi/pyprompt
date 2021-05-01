#!/usr/bin/env zsh
setopt PROMPT_SUBST
PYPROMPT_FILE="${0:A:h}/../main.py"
#PYPROMPT_FILE="${0:A:h}/../testcolor.py"
PS1='$(python ${PYPROMPT_FILE} zsh)'
