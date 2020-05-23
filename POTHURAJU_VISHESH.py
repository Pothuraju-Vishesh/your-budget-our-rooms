from cmd import Cmd

class Hotel(Cmd):
	prompt = '> '
	intro = "----Welcome to Your BUDGET our ROOMS-----"

	def __init__(self):
		super(Hotel, self).__init__()
		self.data = {}
		print("Please add first hotel and room")
		self.addHotel()

	def addHotel(self):
		name = input("Enter Hotel name: ")
		if self.data.get(name, False):
			print("\nHotel with same name already exist!..")
			self.addHotel()
		else:
			self.data[name] = {}
			self.addRoom(name)

	def addRoom(self, name):
		room_no = input("{}-> Enter Room Number: ".format(name))
		self.data[name][room_no]={"items": [], "itemsList": [], "cost": 0}
		i = 0
		while i < 5:
			item = input("{}-> {}-> Enter the item {} name: ".format(name, room_no, i+1))
			price = input("Enter {} prize in $ (should be a number): ".format(item))
			self.data[name][room_no]["items"].append({item: price})
			self.data[name][room_no]["itemsList"].append(item)
			self.data[name][room_no]["cost"] += int(price)
			i += 1
		self.menu()

	def do_add(self,line):
		add_hotel = input("\nDo you want to add New Hotel (Yes/No): ")
		if add_hotel.lower() == "yes":
			self.addHotel()
		elif add_hotel.lower() == "no":
			self.menu()
		else:
			print("Invalid Input")
			self.do_add(line)

	def do_room(self,line):
		add_room = input("\nDo you want to add more Room(Yes/No): ")
		if add_room.lower() == "yes":
			for hotel_name, room_info in self.data.items():
				print(hotel_name)
				print(room_info)
			name=input("select Holel :")
			self.addRoom(name)
		elif add_room.lower() == "no":
			self.menu()
		else:
			print("Invalid Input")
			self.do_room(line)

	def do_show(self,line):
		for hotel_name, room_info in self.data.items():
			rooms = "\nRoom No {0} have the items like {1}, and room rent is ${2}."
			hotels = '\n\n\nHotel -{0}- have following rooms\n'.format(hotel_name)
			for room, amenti_info in room_info.items():
				amenti = ', '.join(amenti_info['itemsList'])
				cost = amenti_info['cost']
				hotels += rooms.format(room, amenti, cost)
			print(hotels)
		self.menu()

	def do_budget(self,line):
		print("\n***********************************************************\n")
		budget = int(input("Please enter your budget: "))
		if budget > 1:
			for hotel_name, room_info in self.data.items():
				rooms = "\nRoom No {0} have the items like {1}, and room rent is ${2}."
				hotels = '\n\n\nHotel -{0}- have following rooms matching your budget\n'.format(hotel_name)
				availability = False
				for room, amenti_info in room_info.items():
					cost = amenti_info['cost']
					if cost <= budget:
						amenti = ', '.join(amenti_info['itemsList'])
						availability = True
						hotels += rooms.format(room, amenti, cost)
				if availability:
					print(hotels)
				else:
					print("\n\n\nNo room available for your budget in hotel {0}".format(hotel_name))
			print("\n***********************************************************\n")
			self.menu()
		else:
			print("Invalid Budget range")
			self.do_budget(line)

	def menu(self):
		print("\n1. add Hotel(type add)")
		print("2. add Room to Hotel(type room)")
		print("3. show all Rooms with Items and their values(type show)")
		print("4 tell your budget to in \$ to get list of rooms in your budget(type budget)")

if __name__ == '__main__':
	Hotel().cmdloop()