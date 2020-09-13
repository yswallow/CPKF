import board
import digitalio
import storage
import os

storage.remount("/", False)

force_writable_button = digitalio.DigitalInOut(board.D2)
force_writable_button.direction = digitalio.Direction.INPUT
force_writable_button.pull = digitalio.Pull.UP


if(not force_writable_button):
	storage.remount("/", True)
else:
	if "log" in os.listdir():
		files = os.listdir("/log");
		if ("error-output-enable.txt" in files) and not ("error-checked.txt" in files):
			with open("/log/error-checked.txt", "w") as fp:
				pass
		
		else:
			storage.remount("/", True)
	else:
		storage.remount("/", True)

