import setuptools
from setuptools.command.install import install

class PostInstallCommand(install):
	"""Post-installation for installation mode."""
	def run(self):
		import os, sys
		scripts = os.path.join(os.path.dirname(sys.executable), "Scripts")

		bat_file = os.path.join(scripts, "roboproc.bat")
		write_file = open(bat_file, 'w')
		write_file.write("@echo off\n")
		write_file.write("set batpath=%~dp0\n")
		write_file.write("set listenerpath=%batpath%\..\Lib\site-packages\RobotProcessLibrary\listeners\Process.py\n")
		write_file.write("set totestpath=%batpath%\..\Lib\site-packages\RobotProcessLibrary\listeners\\to_test.py\n")
		write_file.write("set toprocesspath=%batpath%\..\Lib\site-packages\RobotProcessLibrary\listeners\\to_process.py\n")
		write_file.write("python %totestpath% %*\n")
		write_file.write("python -m robot.run -r None --listener %listenerpath% %*\n")
		write_file.write("python %toprocesspath% %*\n")
		write_file.close()
		install.run(self)


setuptools.setup(name='robotprocesslibrary',
      version='0.1',
      description='Library for robotic process automation.',
      url='',
      author='Andras Kelemen',
      author_email='kelemenandras11@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(exclude=['RobotProcessLibrary.tests']),

      install_requires=[
      # todo a 3 lib
        'robotframework',
      ],
      cmdclass={
        'install': PostInstallCommand,
      },
      test_suite="tests",
      tests_require=['nose'],
      zip_safe=False
      )