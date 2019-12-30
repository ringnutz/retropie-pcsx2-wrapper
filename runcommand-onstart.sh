#!/bin/bash
#only if for ps2, launch python wrapper script to catch hotkey assignments (for exiting the emu e.g.)
if [ $1='ps2' ]; then
	/usr/bin/python /opt/retropie/configs/all/gamepad_wrapper.py &
fi