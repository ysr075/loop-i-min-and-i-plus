from time import sleep

def i_plus_plus():
	i = 0
	while True:
		i += 1
		print("case " + str(i))
		sleep(0.5)

def i_min_min():
	i = 0
	while True:
		i -= 1
		print("case " + str(i))
		sleep(0.5)

def main():
	choice = input("plus / min: ")
	if choice == "plus":
		i_plus_plus()
	elif choice	== "min":
		i_min_min()
	else:
		return main()

if __name__ == '__main__':
	main()
