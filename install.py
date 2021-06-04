#
# Follow on GitHub : https://github.com/AnythingSuitable
#

from os import system, path, geteuid
from sys import exit

print('\n[+] Installing : TorghostNG GUI\n\n')

if geteuid() != 0:
	print("Program requires Super-User Access.\nRun with 'sudo' privileges...\nExiting :/")
	exit()

if path.exists('/usr/bin/torghostng') == True and path.exists('/usr/bin/torngSRC') == True:
	print('[$] TorghostNG GUI seems already available on your Device...')
	choice = input('Wanna uninstall :/ [y/n]\n')

	if choice.upper()[0] == 'Y':
		print("[!] Uninstalling TorghostNg-GUI...")
		system('sudo rm -rf /usr/bin/torghostng')
		system('sudo rm -rf /usr/bin/torngSRC')
		print("[!] Done uninstalling...\n\nHope we see you again...")
		exit()
	else:
		print("[!] Good decision...")
		exit()


print('[#] Checking for desired Files ...')

if path.exists('torghostng') == True and path.exists('torngSRC') == True:
	print('[$] Hmmm.... Seems everything Fine...')

	choice = input('Wanna Install :) [y/n]\n')

	if choice.upper()[0] == 'Y':
		print('[$] Continuing Installation\n')
	else:
		print('[!] Seems you changed your mood :<')
		exit()

	

else:
	print("[!] TorghostNg/GUI Lacking some Files... Kindly Download again from GitHub.\nExitting...")
	exit()

try:
	system('sudo cp torghostng /usr/bin/')
	system('sudo cp -r torngSRC/ /usr/bin/')
	system('chmod +x /usr/bin/torghostng')
	print('[#] Installed : TorghostNG GUI successfully :D')
	print("[#] Run 'sudo torghostng' to see what u just installed...")
	print('\nWe hope you like what you see :v')

except KeyboardInterrupt:
	print()
	exit()

except Exception as e:
	print("\n[!] Something's getting wrong while installing TorghostNg-GUI...\nExitting...")
	exit()