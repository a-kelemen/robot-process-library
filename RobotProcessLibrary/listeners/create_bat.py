import os, sys
scripts = os.path.join(os.path.dirname(sys.executable), "Scripts")

bat_file = os.path.join(scripts, "rrr.bat")
write_file = open(bat_file, 'w')
write_file.write("@echo off\n")
write_file.write("set batpath=%~dp0\n")
write_file.write("set listenerpath=%batpath%\..\Lib\site-packages\RobotProcessLibrary\listeners\Process.py\n")
write_file.write("set totestpath=%batpath%\..\Lib\site-packages\RobotProcessLibrary\listeners\to_test.py\n")
write_file.write("set toprocesspath=%batpath%\..\Lib\site-packages\RobotProcessLibrary\listeners\to_process.py\n")
write_file.write("python %totestpath% %*\n")
write_file.write("python -m robot.run --listener %listenerpath% %*\n")
write_file.write("python %toprocesspath% %*\n")
write_file.close()