#!/bin/bash
#only if for ps2, kill python wrapper script
if [ $1='ps2' ]; then
	PROCS=$(ps aux | grep gamepad_wrapper.py | awk '{ print $2 }')
	for PROC in ${PROCS[@]}
	do
		kill "$PROC"
	done
fi