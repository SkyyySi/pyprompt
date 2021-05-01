#!/usr/bin/env bash
PYPROMPT_FILE="$(cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)/../main.py"
#PYPROMPT_FILE="$(cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)/../testcolor.py"
PROMPT_COMMAND='PS1="$(python ${PYPROMPT_FILE} bash)"'
