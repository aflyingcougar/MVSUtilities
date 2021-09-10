import paaUtil
import missionUtil
import os

def main():

	MENU = True
	PAAUTIL = False
	MISSIONUTIL = False
	QUIT = False

	# main menu
	print("MVS Utilities by aflyingcougar")
	print("[1] Generate *.paa Files")
	print("[2] Generate Types and TraderConfig")
	print("[3] Quit")

	# get user choice
	choice = input("What would you like to do?")
		
	while choice not in ('3', 'quit', 'exit', 'q'):
		os.system("cls")

		if choice == '1':
			paaUtil.main()

		elif choice == '2':
			missionUtil.main()

		# main menu
		os.system("cls")
		print("MVS Utilities by aflyingcougar")
		print("[1] Generate *.paa Files")
		print("[2] Generate Types and TraderConfig")
		print("[3] Quit")

		choice = input("What would you like to do?")

	os.system("cls")
	print("Thanks for using aflyingcougar's MVS Utilities.")
	os.system("pause")
	

if __name__ == "__main__":
	# calling main function
	main()