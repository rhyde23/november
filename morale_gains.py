def new_approach(same_rating_games, distribution, expo_value) :
	team_rating = 99
	og = round((same_rating_games-2)/distribution, 2)
	slope = round((same_rating_games-2)/distribution, 2)
	add = 0
	for i in range(1, 69) :
		add += (i*expo_value)
	current_days = round(same_rating_games+((team_rating-30)*slope)+add, 3)
	values = []
	for x in range(140) :
		values.append(current_days)
		if current_days > 2 :
			current_days -= slope
			slope += expo_value
			current_days = round(current_days, 2)
			if current_days < 2 :
				current_days = 2.0
		else :
			current_days = 2.0
	return values

"""
same_rating_games, distribution, expo_value = 15, 15, 0.01
array1 = new_approach(same_rating_games, distribution, expo_value)
print(array1, array1[69-17])
same_rating_games, distribution, expo_value = 15, 10, 0
array2 = new_approach(same_rating_games, distribution, expo_value)
print(array2, array2[69-17])
"""

def get_reversed(x) :
	return 99-(x-30)

def fill_values(same_rating_games, distribution, expo_value) :
	values = new_approach(same_rating_games, distribution, expo_value)
	file1 = open("morale_gains.txt","w")
	L = []
	start, end = 0, 69
	for team_rating in range(30, 100) :
		new_L = []
		slope = round((same_rating_games-2)/distribution, 2)
		current_days = round(same_rating_games+((team_rating-30)*slope), 2)
		for player_rating in range(start, end+1) :
			new_L.append(str((player_rating-start)+30)+", "+str(get_reversed(team_rating))+": "+str(values[player_rating])+"\n")
			if current_days > 2 :
				current_days -= slope
				current_days = round(current_days, 2)
				if current_days < 2 :
					current_days = 2.0
			else :
				current_days = 2.0
		start += 1
		end += 1
		L = L + list(reversed(new_L))
	file1.writelines(list(reversed(L)))
	file1.close() 

def get_values_gains() :
	file1 = open("morale_gains.txt","r").read()
	days_values = []
	current_array = []
	current_tr = 30
	for line in file1.split('\n') :
		try :
			value1, value2, value3 = line.split(' ')
		except :
			pass
		player_rating = int(value1[:-1])
		team_rating = int(value2[:-1])
		days = float(value3)
		if team_rating != current_tr :
			days_values.append(current_array)
			current_tr = team_rating
			current_array = [days]
		else :
			current_array.append(days)
	days_values.append(current_array)
	return days_values
		

#same_rating_games, distribution, expo_value = 7.5, 20, 0.005
#fill_values(same_rating_games, distribution, expo_value)

#days_values = get_values()
#for days_array in days_values :
	#print(days_array)
