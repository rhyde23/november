from starting_team_formations import get_positions_from_formation
from outside_positions_converter import convert_outside_position_to_center
import itertools, time, random

all_formations = [
	'4-2-3-1 (Wide)',
	'5-3-2 (Attacking)',
	'4-4-2 (Flat)',
	'5-2-3 (Flat)',
	'4-3-3 (Defensive)',
	'4-5-1 (Defensive)',
	'4-3-3 (False 9)',
	'5-3-2 (Flat)',
	'4-3-3 (Flat)',
	'4-3-3 (Attacking)',
	'4-2-3-1 (Narrow)',
	'4-1-2-1-2 (Narrow)',
]

same_positions = {
	'Goalkeeper':['GK'],
	'Outside Back':['LB', 'RB'],
	'Wing Back':['LWB', 'RWB'],
	'Center Back':['LCB', 'CB', 'RCB'],
	'Defensive Midfielder':['LDM', 'CDM', 'RDM'],
	'Center Midfielder':['LCM', 'CM', 'RCM'],
	'Outside Midfielder':['LM', 'RM'],
	'Attacking Midfielder':['LAM', 'CAM', 'RAM'],
	'Winger':['LW', 'RW'],
	'Striker':['LS', 'ST', 'RS'],
	'Forward':['CF'],
}

closest_position_dictionary = {
	'GK':['GK', 'CB', 'RB', 'LB', 'RWB', 'LWB', 'CDM', 'CM', 'CAM', 'CF', 'LM', 'LW', 'RM', 'RW', 'ST'],
	'CB':['CB', 'RB', 'LB', 'CDM', 'RWB', 'LWB', 'CM', 'CAM', 'CF', 'LM', 'LW', 'RM', 'RW', 'ST', 'GK'],
	'RCB':['CB', 'RB', 'LB', 'CDM', 'RWB', 'LWB', 'CM', 'CAM', 'CF', 'LM', 'LW', 'RM', 'RW', 'ST', 'GK'],
	'LCB':['CB', 'RB', 'LB', 'CDM', 'RWB', 'LWB', 'CM', 'CAM', 'CF', 'LM', 'LW', 'RM', 'RW', 'ST', 'GK'],
	'RB':['RB', 'LB', 'RWB', 'LWB', 'CB', 'RM', 'LM', 'CDM', 'CM', 'RW', 'LW', 'CAM', 'CF', 'ST', 'GK'],
	'LB':['LB', 'RB', 'LWB', 'RWB', 'CB', 'LM', 'RM', 'CDM', 'CM', 'LW', 'RW', 'CAM', 'CF', 'ST', 'GK'],
	'RWB':['RWB', 'LWB', 'RB', 'LB', 'RM', 'LM', 'CB', 'CDM', 'CM', 'RW', 'LW', 'CAM', 'CF', 'ST', 'GK'],
	'LWB':['LWB', 'RWB', 'LB', 'RB', 'LM', 'RM', 'CB', 'CDM', 'CM', 'LW', 'RW', 'CAM', 'CF', 'ST', 'GK'],
	'CDM':['CDM', 'CM', 'CB', 'RB', 'LB', 'RWB', 'LWB', 'RM', 'LM', 'CAM', 'CF', 'RW', 'LW', 'ST', 'GK'],
	'RDM':['CDM', 'CM', 'CB', 'RB', 'LB', 'RWB', 'LWB', 'RM', 'LM', 'CAM', 'CF', 'RW', 'LW', 'ST', 'GK'],
	'LDM':['CDM', 'CM', 'CB', 'LB', 'RB', 'LWB', 'RWB', 'LM', 'RM', 'CAM', 'CF', 'LW', 'RW', 'ST', 'GK'],
	'CM':['CM', 'CDM', 'CAM', 'RM', 'LM', 'RWB', 'LWB', 'RB', 'LB', 'CB', 'CF', 'ST', 'RW', 'LW', 'GK'],
	'RCM':['CM', 'CDM', 'CAM', 'RM', 'LM', 'RWB', 'LWB', 'RB', 'LB', 'CB', 'CF', 'RW', 'LW', 'ST', 'GK'],
	'LCM':['CM', 'CDM', 'CAM', 'LM', 'RM', 'LWB', 'RWB', 'LB', 'RB', 'CB', 'CF', 'LW', 'RW', 'ST', 'GK'],
	'CAM':['CAM', 'CF', 'CM', 'RM', 'LM', 'ST', 'RW', 'LW', 'CDM', 'RWB', 'LWB', 'CB', 'RB', 'LB', 'GK'],
	'RAM':['CAM', 'CF', 'CM', 'RM', 'LM', 'ST', 'RW', 'LW', 'CDM', 'RWB', 'LWB', 'CB', 'RB', 'LB', 'GK'],
	'LAM':['CAM', 'CF', 'CM', 'LM', 'RM', 'ST', 'LW', 'RW', 'CDM', 'LWB', 'RWB', 'CB', 'LB', 'RB', 'GK'],
	'RM':['RM', 'LM', 'RW', 'LW', 'RWB', 'LWB', 'CAM', 'CM', 'RB', 'LB', 'ST', 'CF', 'CDM', 'CB', 'GK'],
	'LM':['LM', 'RM', 'LW', 'RW', 'LWB', 'RWB', 'CAM', 'CM', 'LB', 'RB', 'ST', 'CF', 'CDM', 'CB', 'GK'],
	'RW':['RW', 'LW', 'RM', 'LM', 'CAM', 'ST', 'CF', 'CM', 'RWB', 'LWB', 'RB', 'LB', 'CDM', 'CB', 'GK'],
	'LW':['LW', 'RW', 'LM', 'RM', 'CAM', 'ST', 'CF', 'CM', 'LWB', 'RWB', 'LB', 'RB', 'CDM', 'CB', 'GK'],
	'ST':['ST', 'CF', 'CAM', 'RW', 'LW', 'RM', 'LM', 'CM', 'CDM', 'RWB', 'LWB', 'RB', 'LB', 'CB', 'GK'],
	'RS':['ST', 'CF', 'CAM', 'RW', 'LW', 'RM', 'LM', 'CM', 'CDM', 'RWB', 'LWB', 'RB', 'LB', 'CB', 'GK'],
	'LS':['ST', 'CF', 'CAM', 'LW', 'RW', 'LM', 'RM', 'CM', 'CDM', 'LWB', 'RWB', 'LB', 'RB', 'CB', 'GK'],
	'CF':['CF', 'CAM', 'ST', 'RW', 'LW', 'RM', 'LM', 'CM', 'CDM', 'RWB', 'LWB', 'RB', 'LB', 'CB', 'GK'],
}

def get_same_position(position) :
	for position_category in same_positions :
		if position in same_positions[position_category] :
			return position_category

def get_best_players_in_each_position(players_position_ratings, all_players, all_positions) :
	return_dictionary = {}
	for ap in all_positions :
		start_answer = sorted(all_players, key=lambda x:players_position_ratings[x][ap], reverse=True)
		last_value = players_position_ratings[start_answer[0]][ap]
		current_run = [start_answer[0]]
		for s_a in start_answer[1:] :
			s_a_value = players_position_ratings[s_a][ap]
			if s_a_value == last_value :
				current_run.append(s_a)
			else :
				if len(current_run) != 1 :
					new_current_run = sorted(current_run, key=lambda x: closest_position_dictionary[ap].index(list(players_position_ratings[x].keys())[0]))
					first_index_replace = start_answer.index(current_run[0])
					for rep in range(first_index_replace, first_index_replace+len(current_run), 1) :
						start_answer[rep] = new_current_run[rep-first_index_replace]
				current_run = [s_a]
			last_value = s_a_value
		return_dictionary[ap] = start_answer
	return return_dictionary

def valid_amounts(p, counts_dictionary) :
	wrong = 0
	for cd in counts_dictionary :
		if p.count(cd) > counts_dictionary[cd] :
			wrong += 1
	return wrong

def calculate_rating(players_position_ratings, combination, combination_names) :
	rating = 0
	for i in range(len(combination)) :
		rating += players_position_ratings[combination_names[i]][convert_outside_position_to_center(same_positions[combination[i]][0])]
	return rating
	
def get_going_to_try(players_position_ratings, best_players, positions_from_formation) :
	going_to_try = {}
	for pff in positions_from_formation :
		converted_pff = convert_outside_position_to_center(pff)
		best = best_players[converted_pff][0]
		if not best in going_to_try :
			going_to_try[best] = [pff]
		else :
			going_to_try[best].append(pff)
	counts = {}
	for key in going_to_try :
		positions = going_to_try[key]
		for position in positions :
			if position in counts :
				counts[position] += 1
			else :
				counts[position] = 1
	for count_key in counts :
		if count_key != 'GK' :
			for i in range(counts[count_key]) :
				try :
					converted = convert_outside_position_to_center(count_key)
					start_player_in_question = best_players[converted][i+1]
					start_rating = players_position_ratings[start_player_in_question][converted]
					piq_index = i+1
					while True :
						if players_position_ratings[best_players[converted][piq_index]][converted] == start_rating :
							player_in_question = best_players[converted][piq_index]
							if player_in_question in going_to_try :
								going_to_try[player_in_question].append(count_key)
							else :
								going_to_try[player_in_question] = [count_key]
						else :
							break
						piq_index += 1
				except :
					pass
	new_gtt = {}
	for key in going_to_try :
		array = going_to_try[key]
		array = [get_same_position(pos) for pos in array]
		new_gtt[key] = list(set(array))
	total_array = [get_same_position(pff) for pff in positions_from_formation]
	counts_dictionary = {same_positions_key:total_array.count(same_positions_key) for same_positions_key in list(same_positions.keys())} 
	new_gtt_keys = list(new_gtt.keys())
	iter_array = [new_gtt[k] for k in new_gtt]
	best_p, best_p_amount, followed_amounts = [], 0, 0
	for p in itertools.product(*iter_array) :
		if len(p) > len(positions_from_formation) :
			p = p[:len(positions_from_formation)]
		rating = calculate_rating(players_position_ratings, p, new_gtt_keys)
		if rating > best_p_amount :
			best_p = p
			best_p_amount = rating
			followed_amounts = valid_amounts(p, counts_dictionary)
		else :
			if rating == best_p_amount :
				if valid_amounts(p, counts_dictionary) < followed_amounts :
					best_p = p
					best_p_amount = rating
					followed_amounts = valid_amounts(p, counts_dictionary)
	best_p_real_positions = []
	for category in best_p :
		for posit in same_positions[category] :
			if not posit in best_p_real_positions and posit in positions_from_formation :
				best_p_real_positions.append(posit)
				break
	if len(new_gtt_keys) > len(best_p_real_positions) :
		new_gtt_keys = new_gtt_keys[:len(best_p_real_positions)]
	return new_gtt_keys, best_p_real_positions
	
def best_lineup_individual(players_position_ratings, formation_name, required_players) :
	players_taken = []
	positions_taken = []
	positions_from_formation = get_positions_from_formation(formation_name)
	divisors = {}
	for required_player in required_players :
		best_position_in_formation = sorted(positions_from_formation, key=lambda x: players_position_ratings[required_player][convert_outside_position_to_center(x)], reverse=True)[0]
		player_rating_at_pos = players_position_ratings[required_player][convert_outside_position_to_center(best_position_in_formation)]
		best_player_in_club_at_position = sorted(list(players_position_ratings.keys()), key=lambda x: players_position_ratings[x][convert_outside_position_to_center(best_position_in_formation)], reverse=True)[0]
		bpicap_rating = players_position_ratings[best_player_in_club_at_position][convert_outside_position_to_center(best_position_in_formation)]
		divisor = 500-player_rating_at_pos
		divisors[required_player] = divisor
		for position_changing in players_position_ratings[required_player] :
			players_position_ratings[required_player][position_changing] += divisor 
	while True :
		if len(players_taken) == 11 :
			break
		new_positions_from_formation = [new_position for new_position in positions_from_formation if not new_position in positions_taken]
		new_players_position_ratings = {key:players_position_ratings[key] for key in players_position_ratings if not key in players_taken}
		all_players = list(new_players_position_ratings.keys())
		all_positions = [convert_outside_position_to_center(p) for p in positions_from_formation]
		best_players = get_best_players_in_each_position(new_players_position_ratings, all_players, all_positions)
		t_players, t_positions = get_going_to_try(new_players_position_ratings, best_players, new_positions_from_formation)
		players_taken = players_taken+t_players
		positions_taken = positions_taken+t_positions
	positions_from_formation = get_positions_from_formation(formation_name)
	final_result = ['' for x in range(11)]
	for pti, pt in enumerate(positions_taken) :
		final_result[positions_from_formation.index(pt)] = players_taken[pti]
	for required_player in required_players :
		for position_changing in players_position_ratings[required_player] : 
			players_position_ratings[required_player][position_changing] -= divisors[required_player]
	while True :
		final_result_playing = {final_result[index]:convert_outside_position_to_center(positions_from_formation[index]) for index in range(11)}
		change = False
		for i1 in range(11) :
			name1 = final_result[i1]
			b = False
			for i2 in range(i1+1, 11, 1) :
				name2 = final_result[i2]
				current_sum = players_position_ratings[name1][final_result_playing[name1]]+players_position_ratings[name2][final_result_playing[name2]]
				could_be_sum = players_position_ratings[name1][final_result_playing[name2]]+players_position_ratings[name2][final_result_playing[name1]]
				if could_be_sum > current_sum :
					final_result[i1] = name2
					final_result[i2] = name1
					b = True
					break
			if b :
				change = True
				break
		if not change :
			break
	return final_result 

def calculate_final_rating(players_position_ratings, fin, positions_ff) :
	t = 0
	for i, name in enumerate(fin) :
		name_pos = positions_ff[i]
		t += players_position_ratings[name][convert_outside_position_to_center(name_pos)]
	return t

def best_lineup(players_position_ratings, required_players=[], forbidden_players=[]) :
	for forbidden_player in forbidden_players :
		del players_position_ratings[forbidden_player]
	best_final, best_final_rating, best_final_formation = [], 0, ''
	for formation_name in all_formations :
		fin = best_lineup_individual(players_position_ratings, formation_name, required_players)
		fin_rating = calculate_final_rating(players_position_ratings, fin, get_positions_from_formation(formation_name))
		if fin_rating > best_final_rating :
			best_final = fin
			best_final_rating = fin_rating
			best_final_formation = formation_name
	return best_final_formation, best_final, best_final_rating
























































"""
#players_position_ratings = {'Willian': {'RM': 80, 'CAM': 80, 'CB': 59, 'CDM': 68, 'CF': 79, 'CM': 77, 'GK': 33, 'LB': 67, 'LM': 80, 'LW': 79, 'LWB': 71, 'RB': 67, 'RW': 79, 'RWB': 71, 'ST': 74}, 'Gabriel Martinelli': {'LM': 76, 'CAM': 74, 'CB': 59, 'CDM': 61, 'CF': 75, 'CM': 68, 'GK': 28, 'LB': 64, 'LW': 75, 'LWB': 66, 'RB': 64, 'RM': 76, 'RW': 75, 'RWB': 66, 'ST': 74}, 'Karl Hein': {'GK': 57, 'CAM': 22, 'CB': 23, 'CDM': 23, 'CF': 22, 'CM': 23, 'LB': 23, 'LM': 21, 'LW': 21, 'LWB': 23, 'RB': 23, 'RM': 21, 'RW': 21, 'RWB': 23, 'ST': 23}, 'Miguel Azeez': {'CM': 64, 'CAM': 64, 'CB': 52, 'CDM': 57, 'CF': 64, 'GK': 29, 'LB': 55, 'LM': 64, 'LW': 63, 'LWB': 57, 'RB': 55, 'RM': 64, 'RW': 63, 'RWB': 57, 'ST': 62}, 'Nicolas Pépé': {'RM': 82, 'CAM': 79, 'CB': 55, 'CDM': 62, 'CF': 80, 'CM': 74, 'GK': 32, 'LB': 63, 'LM': 82, 'LW': 80, 'LWB': 66, 'RB': 63, 'RW': 80, 'RWB': 66, 'ST': 78}, 'Reiss Nelson': {'RM': 74, 'CAM': 71, 'CB': 49, 'CDM': 57, 'CF': 71, 'CM': 66, 'GK': 30, 'LB': 58, 'LM': 74, 'LW': 72, 'LWB': 61, 'RB': 58, 'RW': 72, 'RWB': 61, 'ST': 68}, 'Ben Cottrell': {'CM': 59, 'CAM': 60, 'CB': 48, 'CDM': 52, 'CF': 59, 'GK': 24, 'LB': 51, 'LM': 60, 'LW': 59, 'LWB': 52, 'RB': 51, 'RM': 60, 'RW': 59, 'RWB': 52, 'ST': 58}, 'Rúnar Alex Rúnarsson': {'GK': 72, 'CAM': 31, 'CB': 28, 'CDM': 29, 'CF': 31, 'CM': 31, 'LB': 29, 'LM': 30, 'LW': 30, 'LWB': 29, 'RB': 29, 'RM': 30, 'RW': 30, 'RWB': 29, 'ST': 31}, 'Eddie Nketiah': {'ST': 74, 'CAM': 71, 'CB': 47, 'CDM': 51, 'CF': 73, 'CM': 63, 'GK': 29, 'LB': 51, 'LM': 70, 'LW': 71, 'LWB': 53, 'RB': 51, 'RM': 70, 'RW': 71, 'RWB': 53}, 'Kieran Tierney': {'LB': 81, 'CAM': 77, 'CB': 78, 'CDM': 79, 'CF': 76, 'CM': 77, 'GK': 35, 'LM': 79, 'LW': 77, 'LWB': 81, 'RB': 81, 'RM': 79, 'RW': 77, 'RWB': 81, 'ST': 73}, 'Folarin Balogun': {'ST': 63, 'CAM': 58, 'CB': 41, 'CDM': 43, 'CF': 61, 'CM': 52, 'GK': 27, 'LB': 45, 'LM': 59, 'LW': 59, 'LWB': 46, 'RB': 45, 'RM': 59, 'RW': 59, 'RWB': 46}, 'Cédric': {'RB': 77, 'CAM': 74, 'CB': 74, 'CDM': 75, 'CF': 74, 'CM': 75, 'GK': 33, 'LB': 77, 'LM': 75, 'LW': 74, 'LWB': 76, 'RM': 75, 'RW': 74, 'RWB': 76, 'ST': 72}, 'Calum Chambers': {'RB': 76, 'CAM': 70, 'CB': 76, 'CDM': 76, 'CF': 69, 'CM': 72, 'GK': 31, 'LB': 76, 'LM': 70, 'LW': 69, 'LWB': 74, 'RM': 70, 'RW': 69, 'RWB': 74, 'ST': 68}, 'Bukayo Saka': {'RM': 81, 'CAM': 79, 'CB': 69, 'CDM': 74, 'CF': 78, 'CM': 77, 'GK': 31, 'LB': 75, 'LM': 81, 'LW': 79, 'LWB': 77, 'RB': 75, 'RW': 79, 'RWB': 77, 'ST': 73}, 'Tolaji Bola': {'LB': 58, 'CAM': 49, 'CB': 58, 'CDM': 54, 'CF': 50, 'CM': 49, 'GK': 24, 'LM': 52, 'LW': 51, 'LWB': 57, 'RB': 58, 'RM': 52, 'RW': 51, 'RWB': 57, 'ST': 50}, 'Mathew Ryan': {'GK': 80, 'CAM': 37, 'CB': 33, 'CDM': 36, 'CF': 35, 'CM': 38, 'LB': 33, 'LM': 35, 'LW': 34, 'LWB': 33, 'RB': 33, 'RM': 35, 'RW': 34, 'RWB': 33, 'ST': 33}, 'Rob Holding': {'CB': 77, 'CAM': 62, 'CDM': 74, 'CF': 60, 'CM': 66, 'GK': 32, 'LB': 72, 'LM': 61, 'LW': 60, 'LWB': 71, 'RB': 72, 'RM': 61, 'RW': 60, 'RWB': 71, 'ST': 58}, 'Gabriel': {'CB': 79, 'CAM': 62, 'CDM': 75, 'CF': 60, 'CM': 67, 'GK': 29, 'LB': 72, 'LM': 60, 'LW': 58, 'LWB': 69, 'RB': 72, 'RM': 60, 'RW': 58, 'RWB': 69, 'ST': 60}, 'Héctor Bellerín': {'RB': 78, 'CAM': 73, 'CB': 73, 'CDM': 74, 'CF': 72, 'CM': 72, 'GK': 33, 'LB': 78, 'LM': 75, 'LW': 73, 'LWB': 77, 'RM': 75, 'RW': 73, 'RWB': 77, 'ST': 68}, 'Martin Ødegaard': {'CAM': 84, 'CB': 66, 'CDM': 74, 'CF': 81, 'CM': 81, 'GK': 34, 'LB': 72, 'LM': 83, 'LW': 82, 'LWB': 75, 'RB': 72, 'RM': 83, 'RW': 82, 'RWB': 75, 'ST': 77}, 'Cătălin Cîrjan': {'CM': 64, 'CAM': 65, 'CB': 51, 'CDM': 57, 'CF': 63, 'GK': 29, 'LB': 56, 'LM': 64, 'LW': 63, 'LWB': 57, 'RB': 56, 'RM': 64, 'RW': 63, 'RWB': 57, 'ST': 59}, 'Pierre-Emerick Aubameyang': {'ST': 85, 'CAM': 82, 'CB': 59, 'CDM': 64, 'CF': 84, 'CM': 77, 'GK': 32, 'LB': 66, 'LM': 82, 'LW': 83, 'LWB': 69, 'RB': 66, 'RM': 82, 'RW': 83, 'RWB': 69}, 'Thomas Partey': {'CM': 86, 'CAM': 82, 'CB': 83, 'CDM': 85, 'CF': 81, 'GK': 34, 'LB': 82, 'LM': 81, 'LW': 80, 'LWB': 83, 'RB': 82, 'RM': 81, 'RW': 80, 'RWB': 83, 'ST': 79}, 'Emile Smith Rowe': {'CAM': 76, 'CB': 50, 'CDM': 59, 'CF': 74, 'CM': 71, 'GK': 29, 'LB': 58, 'LM': 75, 'LW': 74, 'LWB': 61, 'RB': 58, 'RM': 75, 'RW': 74, 'RWB': 61, 'ST': 69}, 'Pablo Marí': {'CB': 76, 'CAM': 55, 'CDM': 71, 'CF': 55, 'CM': 61, 'GK': 29, 'LB': 68, 'LM': 54, 'LW': 53, 'LWB': 65, 'RB': 68, 'RM': 54, 'RW': 53, 'RWB': 65, 'ST': 57}, 'Granit Xhaka': {'CDM': 79, 'CAM': 73, 'CB': 73, 'CF': 72, 'CM': 78, 'GK': 30, 'LB': 73, 'LM': 71, 'LW': 70, 'LWB': 74, 'RB': 73, 'RM': 71, 'RW': 70, 'RWB': 74, 'ST': 70}, 'Alexandre Lacazette': {'ST': 83, 'CAM': 81, 'CB': 63, 'CDM': 67, 'CF': 82, 'CM': 77, 'GK': 30, 'LB': 64, 'LM': 79, 'LW': 80, 'LWB': 67, 'RB': 64, 'RM': 79, 'RW': 80, 'RWB': 67}, 'Dani Ceballos': {'CM': 79, 'CAM': 78, 'CB': 70, 'CDM': 76, 'CF': 76, 'GK': 33, 'LB': 73, 'LM': 77, 'LW': 76, 'LWB': 75, 'RB': 73, 'RM': 77, 'RW': 76, 'RWB': 75, 'ST': 72}, 'Bernd Leno': {'GK': 85, 'CAM': 39, 'CB': 35, 'CDM': 39, 'CF': 36, 'CM': 41, 'LB': 35, 'LM': 36, 'LW': 35, 'LWB': 36, 'RB': 35, 'RM': 36, 'RW': 35, 'RWB': 36, 'ST': 34}, 'Mohamed Elneny': {'CDM': 78, 'CAM': 72, 'CB': 74, 'CF': 71, 'CM': 76, 'GK': 31, 'LB': 74, 'LM': 71, 'LW': 70, 'LWB': 75, 'RB': 74, 'RM': 71, 'RW': 70, 'RWB': 75, 'ST': 69}, 'Dejan Iliev': {'GK': 63, 'CAM': 27, 'CB': 26, 'CDM': 27, 'CF': 27, 'CM': 27, 'LB': 26, 'LM': 27, 'LW': 27, 'LWB': 27, 'RB': 26, 'RM': 27, 'RW': 27, 'RWB': 27, 'ST': 28}, 'Joel López': {'LB': 60, 'CAM': 52, 'CB': 56, 'CDM': 54, 'CF': 52, 'CM': 51, 'GK': 26, 'LM': 56, 'LW': 54, 'LWB': 58, 'RB': 60, 'RM': 56, 'RW': 54, 'RWB': 58, 'ST': 51}, 'David Luiz': {'CB': 80, 'CAM': 72, 'CDM': 79, 'CF': 71, 'CM': 76, 'GK': 33, 'LB': 76, 'LM': 71, 'LW': 70, 'LWB': 75, 'RB': 76, 'RM': 71, 'RW': 70, 'RWB': 75, 'ST': 71}}
#players_position_ratings = {'Ferran Torres': {'RW': 81, 'CAM': 81, 'CB': 55, 'CDM': 62, 'CF': 81, 'CM': 76, 'GK': 33, 'LB': 61, 'LM': 81, 'LW': 81, 'LWB': 65, 'RB': 61, 'RM': 81, 'RWB': 65, 'ST': 79}, 'Rodri': {'CDM': 85, 'CAM': 80, 'CB': 82, 'CF': 79, 'CM': 83, 'GK': 33, 'LB': 80, 'LM': 77, 'LW': 76, 'LWB': 80, 'RB': 80, 'RM': 77, 'RW': 76, 'RWB': 80, 'ST': 78}, 'Scott Carson': {'GK': 68, 'CAM': 29, 'CB': 29, 'CDM': 27, 'CF': 29, 'CM': 28, 'LB': 26, 'LM': 26, 'LW': 27, 'LWB': 26, 'RB': 26, 'RM': 26, 'RW': 27, 'RWB': 26, 'ST': 30}, 'Philippe Sandler': {'CB': 71, 'CAM': 64, 'CDM': 70, 'CF': 61, 'CM': 67, 'GK': 30, 'LB': 66, 'LM': 62, 'LW': 60, 'LWB': 65, 'RB': 66, 'RM': 62, 'RW': 60, 'RWB': 65, 'ST': 58}, 'Riyad Mahrez': {'RW': 85, 'CAM': 84, 'CB': 55, 'CDM': 65, 'CF': 84, 'CM': 79, 'GK': 33, 'LB': 64, 'LM': 84, 'LW': 85, 'LWB': 68, 'RB': 64, 'RM': 84, 'RWB': 68, 'ST': 79}, 'Fernandinho': {'CDM': 85, 'CAM': 78, 'CB': 83, 'CF': 78, 'CM': 81, 'GK': 34, 'LB': 80, 'LM': 76, 'LW': 76, 'LWB': 80, 'RB': 80, 'RM': 76, 'RW': 76, 'RWB': 80, 'ST': 77}, 'Rúben Dias': {'CB': 85, 'CAM': 63, 'CDM': 80, 'CF': 62, 'CM': 69, 'GK': 30, 'LB': 77, 'LM': 63, 'LW': 60, 'LWB': 76, 'RB': 77, 'RM': 63, 'RW': 60, 'RWB': 76, 'ST': 63}, 'Ederson': {'GK': 90, 'CAM': 47, 'CB': 38, 'CDM': 44, 'CF': 44, 'CM': 48, 'LB': 38, 'LM': 43, 'LW': 42, 'LWB': 40, 'RB': 38, 'RM': 43, 'RW': 42, 'RWB': 40, 'ST': 41}, 'Liam Delap': {'ST': 65, 'CAM': 60, 'CB': 44, 'CDM': 45, 'CF': 62, 'CM': 54, 'GK': 26, 'LB': 46, 'LM': 61, 'LW': 61, 'LWB': 47, 'RB': 46, 'RM': 61, 'RW': 61, 'RWB': 47}, 'Kevin De Bruyne': {'CM': 91, 'CAM': 91, 'CB': 74, 'CDM': 83, 'CF': 89, 'GK': 37, 'LB': 79, 'LM': 90, 'LW': 89, 'LWB': 83, 'RB': 79, 'RM': 90, 'RW': 89, 'RWB': 83, 'ST': 86}, 'João Cancelo': {'RB': 86, 'CAM': 84, 'CB': 81, 'CDM': 83, 'CF': 84, 'CM': 85, 'GK': 35, 'LB': 86, 'LM': 85, 'LW': 84, 'LWB': 86, 'RM': 85, 'RW': 84, 'RWB': 86, 'ST': 81}, 'Bernardo Silva': {'CAM': 87, 'CB': 66, 'CDM': 75, 'CF': 85, 'CM': 84, 'GK': 34, 'LB': 74, 'LM': 87, 'LW': 86, 'LWB': 77, 'RB': 74, 'RM': 87, 'RW': 86, 'RWB': 77, 'ST': 80}, 'Kyle Walker': {'RB': 85, 'CAM': 78, 'CB': 83, 'CDM': 83, 'CF': 79, 'CM': 80, 'GK': 34, 'LB': 85, 'LM': 80, 'LW': 78, 'LWB': 84, 'RM': 80, 'RW': 78, 'RWB': 84, 'ST': 77}, 'Eric García': {'CB': 75, 'CAM': 61, 'CDM': 72, 'CF': 59, 'CM': 65, 'GK': 29, 'LB': 70, 'LM': 60, 'LW': 58, 'LWB': 69, 'RB': 70, 'RM': 60, 'RW': 58, 'RWB': 69, 'ST': 57}, 'İlkay Gündoğan': {'CM': 87, 'CAM': 86, 'CB': 77, 'CDM': 83, 'CF': 84, 'GK': 35, 'LB': 79, 'LM': 83, 'LW': 83, 'LWB': 81, 'RB': 79, 'RM': 83, 'RW': 83, 'RWB': 81, 'ST': 81}, 'Claudio Gomes': {'CDM': 67, 'CAM': 63, 'CB': 66, 'CF': 62, 'CM': 63, 'GK': 27, 'LB': 64, 'LM': 62, 'LW': 61, 'LWB': 64, 'RB': 64, 'RM': 62, 'RW': 61, 'RWB': 64, 'ST': 61}, 'Adrián Bernabé': {'CAM': 63, 'CB': 51, 'CDM': 54, 'CF': 62, 'CM': 59, 'GK': 26, 'LB': 55, 'LM': 64, 'LW': 63, 'LWB': 57, 'RB': 55, 'RM': 64, 'RW': 63, 'RWB': 57, 'ST': 59}, 'Gabriel Jesus': {'ST': 85, 'CAM': 83, 'CB': 61, 'CDM': 66, 'CF': 84, 'CM': 77, 'GK': 33, 'LB': 65, 'LM': 82, 'LW': 83, 'LWB': 67, 'RB': 65, 'RM': 82, 'RW': 83, 'RWB': 67}, 'Nathan Aké': {'CB': 81, 'CAM': 71, 'CDM': 79, 'CF': 70, 'CM': 74, 'GK': 32, 'LB': 78, 'LM': 72, 'LW': 70, 'LWB': 78, 'RB': 78, 'RM': 72, 'RW': 70, 'RWB': 78, 'ST': 69}, 'Benjamin Mendy': {'LB': 79, 'CAM': 75, 'CB': 77, 'CDM': 77, 'CF': 74, 'CM': 76, 'GK': 31, 'LM': 76, 'LW': 74, 'LWB': 79, 'RB': 79, 'RM': 76, 'RW': 74, 'RWB': 79, 'ST': 71}, 'Sergio Agüero': {'ST': 87, 'CAM': 84, 'CB': 57, 'CDM': 63, 'CF': 86, 'CM': 77, 'GK': 36, 'LB': 60, 'LM': 82, 'LW': 84, 'LWB': 63, 'RB': 60, 'RM': 82, 'RW': 84, 'RWB': 63}, 'Felix Nmecha': {'CAM': 64, 'CB': 54, 'CDM': 57, 'CF': 62, 'CM': 61, 'GK': 27, 'LB': 57, 'LM': 64, 'LW': 63, 'LWB': 58, 'RB': 57, 'RM': 64, 'RW': 63, 'RWB': 58, 'ST': 61}, 'Aymeric Laporte': {'CB': 85, 'CAM': 71, 'CDM': 83, 'CF': 69, 'CM': 76, 'GK': 32, 'LB': 80, 'LM': 69, 'LW': 68, 'LWB': 78, 'RB': 80, 'RM': 69, 'RW': 68, 'RWB': 78, 'ST': 69}, 'John Stones': {'CB': 83, 'CAM': 73, 'CDM': 81, 'CF': 71, 'CM': 76, 'GK': 32, 'LB': 79, 'LM': 72, 'LW': 71, 'LWB': 79, 'RB': 79, 'RM': 72, 'RW': 71, 'RWB': 79, 'ST': 69}, 'Tommy Doyle': {'CM': 65, 'CAM': 63, 'CB': 60, 'CDM': 63, 'CF': 61, 'GK': 29, 'LB': 62, 'LM': 64, 'LW': 62, 'LWB': 63, 'RB': 62, 'RM': 64, 'RW': 62, 'RWB': 63, 'ST': 60}, 'Yeboah Amankwah': {'CB': 57, 'CAM': 42, 'CDM': 52, 'CF': 42, 'CM': 45, 'GK': 24, 'LB': 52, 'LM': 43, 'LW': 42, 'LWB': 51, 'RB': 52, 'RM': 43, 'RW': 42, 'RWB': 51, 'ST': 43}, 'Cole Palmer': {'CAM': 62, 'CB': 52, 'CDM': 55, 'CF': 61, 'CM': 59, 'GK': 27, 'LB': 56, 'LM': 62, 'LW': 61, 'LWB': 57, 'RB': 56, 'RM': 62, 'RW': 61, 'RWB': 57, 'ST': 59}, 'Phil Foden': {'CAM': 84, 'CB': 64, 'CDM': 73, 'CF': 82, 'CM': 80, 'GK': 33, 'LB': 71, 'LM': 83, 'LW': 82, 'LWB': 74, 'RB': 71, 'RM': 83, 'RW': 82, 'RWB': 74, 'ST': 78}, 'Zack Steffen': {'GK': 79, 'CAM': 39, 'CB': 31, 'CDM': 37, 'CF': 35, 'CM': 40, 'LB': 32, 'LM': 36, 'LW': 34, 'LWB': 33, 'RB': 32, 'RM': 36, 'RW': 34, 'RWB': 33, 'ST': 33}, 'Oleksandr Zinchenko': {'LB': 81, 'CAM': 80, 'CB': 78, 'CDM': 80, 'CF': 78, 'CM': 81, 'GK': 35, 'LM': 80, 'LW': 78, 'LWB': 80, 'RB': 81, 'RM': 80, 'RW': 78, 'RWB': 80, 'ST': 76}, 'Raheem Sterling': {'LW': 87, 'CAM': 86, 'CB': 62, 'CDM': 69, 'CF': 86, 'CM': 80, 'GK': 36, 'LB': 69, 'LM': 86, 'LWB': 72, 'RB': 69, 'RM': 86, 'RW': 87, 'RWB': 72, 'ST': 82}}
#players_position_ratings = {'Diogo Jota': {'LW': 83, 'CAM': 82, 'CB': 70, 'CDM': 73, 'CF': 84, 'CM': 79, 'GK': 34, 'LB': 72, 'LM': 83, 'LWB': 73, 'RB': 72, 'RM': 83, 'RW': 83, 'RWB': 73, 'ST': 83}, 'Naby Keïta': {'CM': 81, 'CAM': 81, 'CB': 70, 'CDM': 77, 'CF': 80, 'GK': 34, 'LB': 73, 'LM': 80, 'LW': 79, 'LWB': 76, 'RB': 73, 'RM': 80, 'RW': 79, 'RWB': 76, 'ST': 76}, 'Rhys Williams': {'CB': 64, 'CAM': 52, 'CDM': 61, 'CF': 50, 'CM': 55, 'GK': 27, 'LB': 58, 'LM': 51, 'LW': 50, 'LWB': 57, 'RB': 58, 'RM': 51, 'RW': 50, 'RWB': 57, 'ST': 50}, 'Caoimhin Kelleher': {'GK': 66, 'CAM': 25, 'CB': 25, 'CDM': 25, 'CF': 24, 'CM': 25, 'LB': 24, 'LM': 23, 'LW': 23, 'LWB': 24, 'RB': 24, 'RM': 23, 'RW': 23, 'RWB': 24, 'ST': 25}, 'Xherdan Shaqiri': {'RW': 80, 'CAM': 80, 'CB': 61, 'CDM': 69, 'CF': 79, 'CM': 78, 'GK': 34, 'LB': 67, 'LM': 80, 'LW': 80, 'LWB': 70, 'RB': 67, 'RM': 80, 'RWB': 70, 'ST': 76}, 'Jordan Henderson': {'CDM': 87, 'CAM': 83, 'CB': 83, 'CF': 82, 'CM': 86, 'GK': 35, 'LB': 83, 'LM': 82, 'LW': 81, 'LWB': 84, 'RB': 83, 'RM': 82, 'RW': 81, 'RWB': 84, 'ST': 79}, 'Paul Glatzel': {'ST': 61, 'CAM': 59, 'CB': 44, 'CDM': 46, 'CF': 59, 'CM': 54, 'GK': 26, 'LB': 47, 'LM': 59, 'LW': 59, 'LWB': 48, 'RB': 47, 'RM': 59, 'RW': 59, 'RWB': 48}, 'Yasser Larouci': {'LB': 62, 'CAM': 59, 'CB': 59, 'CDM': 58, 'CF': 59, 'CM': 58, 'GK': 25, 'LM': 61, 'LW': 60, 'LWB': 61, 'RB': 62, 'RM': 61, 'RW': 60, 'RWB': 61, 'ST': 57}, 'Joe Hardy': {'ST': 56, 'CAM': 52, 'CB': 35, 'CDM': 37, 'CF': 55, 'CM': 45, 'GK': 23, 'LB': 37, 'LM': 53, 'LW': 53, 'LWB': 39, 'RB': 37, 'RM': 53, 'RW': 53, 'RWB': 39}, 'Joe Gomez': {'CB': 82, 'CAM': 67, 'CDM': 78, 'CF': 65, 'CM': 70, 'GK': 30, 'LB': 79, 'LM': 69, 'LW': 66, 'LWB': 78, 'RB': 79, 'RM': 69, 'RW': 66, 'RWB': 78, 'ST': 62}, 'Ben Davies': {'CB': 74, 'CAM': 60, 'CDM': 71, 'CF': 59, 'CM': 64, 'GK': 30, 'LB': 72, 'LM': 63, 'LW': 61, 'LWB': 71, 'RB': 72, 'RM': 63, 'RW': 61, 'RWB': 71, 'ST': 59}, 'Joel Matip': {'CB': 83, 'CAM': 68, 'CDM': 80, 'CF': 67, 'CM': 73, 'GK': 32, 'LB': 77, 'LM': 66, 'LW': 65, 'LWB': 75, 'RB': 77, 'RM': 66, 'RW': 65, 'RWB': 75, 'ST': 66}, 'Divock Origi': {'ST': 78, 'CAM': 74, 'CB': 52, 'CDM': 57, 'CF': 76, 'CM': 69, 'GK': 33, 'LB': 56, 'LM': 74, 'LW': 75, 'LWB': 59, 'RB': 56, 'RM': 74, 'RW': 75, 'RWB': 59}, 'Neco Williams': {'RB': 68, 'CAM': 61, 'CB': 64, 'CDM': 65, 'CF': 59, 'CM': 62, 'GK': 30, 'LB': 68, 'LM': 64, 'LW': 62, 'LWB': 67, 'RM': 64, 'RW': 62, 'RWB': 67, 'ST': 56}, 'Nathaniel Phillips': {'CB': 70, 'CAM': 50, 'CDM': 65, 'CF': 48, 'CM': 55, 'GK': 26, 'LB': 63, 'LM': 49, 'LW': 47, 'LWB': 61, 'RB': 63, 'RM': 49, 'RW': 47, 'RWB': 61, 'ST': 50}, 'Billy Koumetio': {'CB': 57, 'CAM': 42, 'CDM': 52, 'CF': 42, 'CM': 45, 'GK': 25, 'LB': 53, 'LM': 43, 'LW': 42, 'LWB': 51, 'RB': 53, 'RM': 43, 'RW': 42, 'RWB': 51, 'ST': 44}, 'Mohamed Salah': {'RW': 89, 'CAM': 89, 'CB': 65, 'CDM': 72, 'CF': 89, 'CM': 84, 'GK': 37, 'LB': 72, 'LM': 88, 'LW': 89, 'LWB': 75, 'RB': 72, 'RM': 88, 'RWB': 75, 'ST': 87}, 'Sadio Mané': {'LW': 89, 'CAM': 88, 'CB': 65, 'CDM': 70, 'CF': 89, 'CM': 82, 'GK': 35, 'LB': 70, 'LM': 88, 'LWB': 73, 'RB': 70, 'RM': 88, 'RW': 89, 'RWB': 73, 'ST': 88}, 'Alisson': {'GK': 89, 'CAM': 41, 'CB': 33, 'CDM': 36, 'CF': 39, 'CM': 41, 'LB': 33, 'LM': 36, 'LW': 37, 'LWB': 33, 'RB': 33, 'RM': 36, 'RW': 37, 'RWB': 33, 'ST': 37}, 'Virgil van Dijk': {'CB': 89, 'CAM': 74, 'CDM': 85, 'CF': 73, 'CM': 78, 'GK': 35, 'LB': 83, 'LM': 72, 'LW': 71, 'LWB': 81, 'RB': 83, 'RM': 72, 'RW': 71, 'RWB': 81, 'ST': 73}, 'Fabinho': {'CDM': 88, 'CAM': 80, 'CB': 86, 'CF': 79, 'CM': 84, 'GK': 34, 'LB': 85, 'LM': 79, 'LW': 78, 'LWB': 85, 'RB': 85, 'RM': 79, 'RW': 78, 'RWB': 85, 'ST': 77}, 'Alex Oxlade-Chamberlain': {'CM': 81, 'CAM': 81, 'CB': 73, 'CDM': 78, 'CF': 80, 'GK': 33, 'LB': 76, 'LM': 81, 'LW': 80, 'LWB': 78, 'RB': 76, 'RM': 81, 'RW': 80, 'RWB': 78, 'ST': 76}, 'Georginio Wijnaldum': {'CM': 87, 'CAM': 85, 'CB': 82, 'CDM': 85, 'CF': 84, 'GK': 35, 'LB': 83, 'LM': 85, 'LW': 83, 'LWB': 84, 'RB': 83, 'RM': 85, 'RW': 83, 'RWB': 84, 'ST': 83}, 'Adrián': {'GK': 76, 'CAM': 30, 'CB': 31, 'CDM': 32, 'CF': 30, 'CM': 31, 'LB': 30, 'LM': 29, 'LW': 29, 'LWB': 30, 'RB': 30, 'RM': 29, 'RW': 29, 'RWB': 30, 'ST': 31}, 'Ozan Kabak': {'CB': 76, 'CAM': 63, 'CDM': 72, 'CF': 61, 'CM': 66, 'GK': 28, 'LB': 69, 'LM': 62, 'LW': 59, 'LWB': 67, 'RB': 69, 'RM': 62, 'RW': 59, 'RWB': 67, 'ST': 59}, 'Konstantinos Tsimikas': {'LB': 77, 'CAM': 73, 'CB': 73, 'CDM': 74, 'CF': 72, 'CM': 72, 'GK': 32, 'LM': 75, 'LW': 73, 'LWB': 76, 'RB': 77, 'RM': 75, 'RW': 73, 'RWB': 76, 'ST': 70}, 'James Milner': {'CM': 82, 'CAM': 78, 'CB': 79, 'CDM': 82, 'CF': 77, 'GK': 33, 'LB': 80, 'LM': 78, 'LW': 77, 'LWB': 81, 'RB': 80, 'RM': 78, 'RW': 77, 'RWB': 81, 'ST': 75}, 'Andrew Robertson': {'LB': 86, 'CAM': 81, 'CB': 81, 'CDM': 84, 'CF': 80, 'CM': 82, 'GK': 34, 'LM': 82, 'LW': 80, 'LWB': 86, 'RB': 86, 'RM': 82, 'RW': 80, 'RWB': 86, 'ST': 76}, 'Curtis Jones': {'CM': 75, 'CAM': 74, 'CB': 65, 'CDM': 70, 'CF': 73, 'GK': 30, 'LB': 68, 'LM': 73, 'LW': 72, 'LWB': 69, 'RB': 68, 'RM': 73, 'RW': 72, 'RWB': 69, 'ST': 70}, 'Ben Woodburn': {'CAM': 66, 'CB': 42, 'CDM': 49, 'CF': 65, 'CM': 61, 'GK': 27, 'LB': 49, 'LM': 66, 'LW': 65, 'LWB': 52, 'RB': 49, 'RM': 66, 'RW': 65, 'RWB': 52, 'ST': 63}, 'Trent Alexander-Arnold': {'RB': 85, 'CAM': 82, 'CB': 80, 'CDM': 84, 'CF': 81, 'CM': 85, 'GK': 34, 'LB': 85, 'LM': 83, 'LW': 81, 'LWB': 85, 'RM': 83, 'RW': 81, 'RWB': 85, 'ST': 78}, 'Thiago': {'CM': 87, 'CAM': 85, 'CB': 74, 'CDM': 81, 'CF': 82, 'GK': 34, 'LB': 78, 'LM': 84, 'LW': 82, 'LWB': 80, 'RB': 78, 'RM': 84, 'RW': 82, 'RWB': 80, 'ST': 77}, 'Roberto Firmino': {'CF': 86, 'CAM': 85, 'CB': 72, 'CDM': 77, 'CM': 84, 'GK': 33, 'LB': 74, 'LM': 85, 'LW': 84, 'LWB': 76, 'RB': 74, 'RM': 85, 'RW': 84, 'RWB': 76, 'ST': 83}}
#players_position_ratings = {'Dominic Calvert-Lewin': {'ST': 82, 'CAM': 76, 'CB': 61, 'CDM': 61, 'CF': 79, 'CM': 70, 'GK': 32, 'LB': 62, 'LM': 76, 'LW': 77, 'LWB': 64, 'RB': 62, 'RM': 76, 'RW': 77, 'RWB': 64}, 'João Virgínia': {'GK': 65, 'CAM': 27, 'CB': 24, 'CDM': 25, 'CF': 27, 'CM': 27, 'LB': 24, 'LM': 25, 'LW': 26, 'LWB': 24, 'RB': 24, 'RM': 25, 'RW': 26, 'RWB': 24, 'ST': 26}, 'Ryan Astley': {'CB': 61, 'CAM': 49, 'CDM': 56, 'CF': 48, 'CM': 51, 'GK': 26, 'LB': 57, 'LM': 50, 'LW': 49, 'LWB': 55, 'RB': 57, 'RM': 50, 'RW': 49, 'RWB': 55, 'ST': 48}, 'Tom Davies': {'CM': 77, 'CAM': 75, 'CB': 72, 'CDM': 75, 'CF': 74, 'GK': 32, 'LB': 73, 'LM': 74, 'LW': 73, 'LWB': 73, 'RB': 73, 'RM': 74, 'RW': 73, 'RWB': 73, 'ST': 71}, 'Jordan Pickford': {'GK': 83, 'CAM': 44, 'CB': 37, 'CDM': 43, 'CF': 41, 'CM': 46, 'LB': 36, 'LM': 40, 'LW': 38, 'LWB': 37, 'RB': 36, 'RM': 40, 'RW': 38, 'RWB': 37, 'ST': 39}, 'Richarlison': {'ST': 84, 'CAM': 81, 'CB': 69, 'CDM': 70, 'CF': 82, 'CM': 77, 'GK': 33, 'LB': 70, 'LM': 81, 'LW': 81, 'LWB': 72, 'RB': 70, 'RM': 81, 'RW': 81, 'RWB': 72}, 'Bobby Carroll': {'CM': 60, 'CAM': 59, 'CB': 55, 'CDM': 57, 'CF': 59, 'GK': 26, 'LB': 57, 'LM': 60, 'LW': 59, 'LWB': 57, 'RB': 57, 'RM': 60, 'RW': 59, 'RWB': 57, 'ST': 57}, 'Kyle John': {'RB': 63, 'CAM': 58, 'CB': 60, 'CDM': 59, 'CF': 58, 'CM': 57, 'GK': 26, 'LB': 63, 'LM': 61, 'LW': 59, 'LWB': 62, 'RM': 61, 'RW': 59, 'RWB': 62, 'ST': 55}, 'André Gomes': {'CM': 80, 'CAM': 77, 'CB': 74, 'CDM': 78, 'CF': 76, 'GK': 32, 'LB': 73, 'LM': 74, 'LW': 74, 'LWB': 74, 'RB': 73, 'RM': 74, 'RW': 74, 'RWB': 74, 'ST': 74}, 'Nathan Broadhead': {'LW': 64, 'CAM': 63, 'CB': 45, 'CDM': 49, 'CF': 63, 'CM': 57, 'GK': 25, 'LB': 50, 'LM': 63, 'LWB': 52, 'RB': 50, 'RM': 63, 'RW': 64, 'RWB': 52, 'ST': 63}, 'Bernard': {'LM': 77, 'CAM': 76, 'CB': 52, 'CDM': 59, 'CF': 75, 'CM': 71, 'GK': 30, 'LB': 60, 'LW': 75, 'LWB': 63, 'RB': 60, 'RM': 77, 'RW': 75, 'RWB': 63, 'ST': 71}, 'Josh Bowler': {'RM': 65, 'CAM': 63, 'CB': 45, 'CDM': 51, 'CF': 62, 'CM': 59, 'GK': 28, 'LB': 52, 'LM': 65, 'LW': 63, 'LWB': 55, 'RB': 52, 'RW': 63, 'RWB': 55, 'ST': 60}, 'Abdoulaye Doucouré': {'CM': 81, 'CAM': 79, 'CB': 79, 'CDM': 80, 'CF': 79, 'GK': 36, 'LB': 79, 'LM': 78, 'LW': 77, 'LWB': 79, 'RB': 79, 'RM': 78, 'RW': 77, 'RWB': 79, 'ST': 78}, 'Einar Iversen': {'CM': 59, 'CAM': 58, 'CB': 58, 'CDM': 59, 'CF': 57, 'GK': 27, 'LB': 59, 'LM': 58, 'LW': 57, 'LWB': 59, 'RB': 59, 'RM': 58, 'RW': 57, 'RWB': 59, 'ST': 55}, 'Yerry Mina': {'CB': 79, 'CAM': 63, 'CDM': 74, 'CF': 63, 'CM': 67, 'GK': 29, 'LB': 71, 'LM': 61, 'LW': 60, 'LWB': 69, 'RB': 71, 'RM': 61, 'RW': 60, 'RWB': 69, 'ST': 65}, 'Niels Nkounkou': {'LB': 62, 'CAM': 56, 'CB': 58, 'CDM': 57, 'CF': 57, 'CM': 55, 'GK': 27, 'LM': 61, 'LW': 59, 'LWB': 61, 'RB': 62, 'RM': 61, 'RW': 59, 'RWB': 61, 'ST': 55}, 'Con Ouzounidis': {'CB': 60, 'CAM': 48, 'CDM': 56, 'CF': 46, 'CM': 50, 'GK': 25, 'LB': 57, 'LM': 50, 'LW': 48, 'LWB': 56, 'RB': 57, 'RM': 50, 'RW': 48, 'RWB': 56, 'ST': 46}, 'Ben Godfrey': {'CB': 77, 'CAM': 65, 'CDM': 74, 'CF': 64, 'CM': 68, 'GK': 30, 'LB': 74, 'LM': 66, 'LW': 64, 'LWB': 73, 'RB': 74, 'RM': 66, 'RW': 64, 'RWB': 73, 'ST': 63}, 'James Rodríguez': {'RW': 83, 'CAM': 84, 'CB': 63, 'CDM': 71, 'CF': 83, 'CM': 82, 'GK': 35, 'LB': 67, 'LM': 82, 'LW': 83, 'LWB': 71, 'RB': 67, 'RM': 82, 'RWB': 71, 'ST': 81}, 'Fabian Delph': {'CDM': 77, 'CAM': 75, 'CB': 74, 'CF': 73, 'CM': 76, 'GK': 31, 'LB': 75, 'LM': 74, 'LW': 73, 'LWB': 75, 'RB': 75, 'RM': 74, 'RW': 73, 'RWB': 75, 'ST': 71}, 'Alex Iwobi': {'RM': 77, 'CAM': 76, 'CB': 52, 'CDM': 60, 'CF': 75, 'CM': 72, 'GK': 31, 'LB': 58, 'LM': 77, 'LW': 75, 'LWB': 62, 'RB': 58, 'RW': 75, 'RWB': 62, 'ST': 71}, 'Mason Holgate': {'CB': 79, 'CAM': 68, 'CDM': 77, 'CF': 66, 'CM': 71, 'GK': 32, 'LB': 76, 'LM': 69, 'LW': 67, 'LWB': 76, 'RB': 76, 'RM': 69, 'RW': 67, 'RWB': 76, 'ST': 64}, 'Séamus Coleman': {'RB': 79, 'CAM': 75, 'CB': 78, 'CDM': 78, 'CF': 75, 'CM': 76, 'GK': 32, 'LB': 79, 'LM': 75, 'LW': 75, 'LWB': 78, 'RM': 75, 'RW': 75, 'RWB': 78, 'ST': 73}, 'Muhamed Bešić': {'CM': 72, 'CAM': 70, 'CB': 73, 'CDM': 73, 'CF': 68, 'GK': 30, 'LB': 69, 'LM': 67, 'LW': 66, 'LWB': 68, 'RB': 69, 'RM': 67, 'RW': 66, 'RWB': 68, 'ST': 66}, 'Robin Olsen': {'GK': 78, 'CAM': 31, 'CB': 30, 'CDM': 32, 'CF': 30, 'CM': 33, 'LB': 29, 'LM': 28, 'LW': 28, 'LWB': 29, 'RB': 29, 'RM': 28, 'RW': 28, 'RWB': 29, 'ST': 30}, 'Gylfi Sigurðsson': {'CAM': 80, 'CB': 67, 'CDM': 73, 'CF': 78, 'CM': 79, 'GK': 34, 'LB': 71, 'LM': 77, 'LW': 77, 'LWB': 73, 'RB': 71, 'RM': 77, 'RW': 77, 'RWB': 73, 'ST': 76}, 'Joshua King': {'ST': 78, 'CAM': 76, 'CB': 58, 'CDM': 61, 'CF': 77, 'CM': 71, 'GK': 31, 'LB': 60, 'LM': 75, 'LW': 76, 'LWB': 62, 'RB': 60, 'RM': 75, 'RW': 76, 'RWB': 62}, 'Lucas Digne': {'LB': 85, 'CAM': 80, 'CB': 82, 'CDM': 83, 'CF': 80, 'CM': 82, 'GK': 33, 'LM': 81, 'LW': 80, 'LWB': 85, 'RB': 85, 'RM': 81, 'RW': 80, 'RWB': 85, 'ST': 78}, 'Imam Jagne': {'CDM': 56, 'CAM': 53, 'CB': 56, 'CF': 52, 'CM': 53, 'GK': 26, 'LB': 55, 'LM': 55, 'LW': 53, 'LWB': 55, 'RB': 55, 'RM': 55, 'RW': 53, 'RWB': 55, 'ST': 52}, 'Michael Keane': {'CB': 81, 'CAM': 65, 'CDM': 76, 'CF': 63, 'CM': 69, 'GK': 32, 'LB': 75, 'LM': 64, 'LW': 63, 'LWB': 73, 'RB': 75, 'RM': 64, 'RW': 63, 'RWB': 73, 'ST': 63}, 'Jean-Philippe Gbamin': {'CDM': 79, 'CAM': 74, 'CB': 78, 'CF': 73, 'CM': 75, 'GK': 33, 'LB': 76, 'LM': 73, 'LW': 72, 'LWB': 76, 'RB': 76, 'RM': 73, 'RW': 72, 'RWB': 76, 'ST': 71}, 'Sean McAllister': {'CM': 57, 'CAM': 58, 'CB': 53, 'CDM': 53, 'CF': 58, 'GK': 25, 'LB': 54, 'LM': 58, 'LW': 57, 'LWB': 54, 'RB': 54, 'RM': 58, 'RW': 57, 'RWB': 54, 'ST': 57}, 'Allan': {'CM': 85, 'CAM': 82, 'CB': 82, 'CDM': 85, 'CF': 81, 'GK': 34, 'LB': 83, 'LM': 81, 'LW': 80, 'LWB': 84, 'RB': 83, 'RM': 81, 'RW': 80, 'RWB': 84, 'ST': 78}}
#players_position_ratings = {'Eric Bailly': {'CB': 79, 'CAM': 64, 'CDM': 73, 'CF': 63, 'CM': 66, 'GK': 31, 'LB': 73, 'LM': 64, 'LW': 63, 'LWB': 72, 'RB': 73, 'RM': 64, 'RW': 63, 'RWB': 72, 'ST': 63}, 'Luke Shaw': {'LB': 83, 'CAM': 78, 'CB': 82, 'CDM': 81, 'CF': 77, 'CM': 79, 'GK': 32, 'LM': 79, 'LW': 77, 'LWB': 82, 'RB': 83, 'RM': 79, 'RW': 77, 'RWB': 82, 'ST': 74}, 'Dean Henderson': {'GK': 81, 'CAM': 33, 'CB': 29, 'CDM': 32, 'CF': 32, 'CM': 34, 'LB': 30, 'LM': 31, 'LW': 31, 'LWB': 30, 'RB': 30, 'RM': 31, 'RW': 31, 'RWB': 30, 'ST': 31}, 'Phil Jones': {'CB': 75, 'CAM': 59, 'CDM': 69, 'CF': 58, 'CM': 62, 'GK': 29, 'LB': 67, 'LM': 58, 'LW': 58, 'LWB': 65, 'RB': 67, 'RM': 58, 'RW': 58, 'RWB': 65, 'ST': 60}, 'Brandon Williams': {'LB': 75, 'CAM': 70, 'CB': 72, 'CDM': 72, 'CF': 70, 'CM': 70, 'GK': 30, 'LM': 72, 'LW': 71, 'LWB': 74, 'RB': 75, 'RM': 72, 'RW': 71, 'RWB': 74, 'ST': 68}, 'Reece Devine': {'LB': 62, 'CAM': 57, 'CB': 61, 'CDM': 59, 'CF': 57, 'CM': 57, 'GK': 26, 'LM': 60, 'LW': 58, 'LWB': 61, 'RB': 62, 'RM': 60, 'RW': 58, 'RWB': 61, 'ST': 56}, 'Alex Telles': {'LB': 84, 'CAM': 82, 'CB': 80, 'CDM': 83, 'CF': 81, 'CM': 83, 'GK': 35, 'LM': 83, 'LW': 81, 'LWB': 84, 'RB': 84, 'RM': 83, 'RW': 81, 'RWB': 84, 'ST': 80}, 'Hannibal Mejbri': {'CAM': 64, 'CB': 57, 'CDM': 60, 'CF': 62, 'CM': 62, 'GK': 26, 'LB': 60, 'LM': 64, 'LW': 62, 'LWB': 61, 'RB': 60, 'RM': 64, 'RW': 62, 'RWB': 61, 'ST': 59}, 'Harry Maguire': {'CB': 83, 'CAM': 71, 'CDM': 81, 'CF': 70, 'CM': 76, 'GK': 34, 'LB': 76, 'LM': 68, 'LW': 67, 'LWB': 75, 'RB': 76, 'RM': 68, 'RW': 67, 'RWB': 75, 'ST': 69}, 'Aaron Wan-Bissaka': {'RB': 83, 'CAM': 74, 'CB': 80, 'CDM': 79, 'CF': 74, 'CM': 75, 'GK': 31, 'LB': 83, 'LM': 77, 'LW': 75, 'LWB': 82, 'RM': 77, 'RW': 75, 'RWB': 82, 'ST': 71}, 'Daniel James': {'RM': 78, 'CAM': 75, 'CB': 58, 'CDM': 64, 'CF': 76, 'CM': 71, 'GK': 30, 'LB': 65, 'LM': 78, 'LW': 76, 'LWB': 68, 'RB': 65, 'RW': 76, 'RWB': 68, 'ST': 73}, 'Shola Shoretire': {'RM': 62, 'CAM': 61, 'CB': 44, 'CDM': 49, 'CF': 60, 'CM': 56, 'GK': 24, 'LB': 49, 'LM': 62, 'LW': 61, 'LWB': 51, 'RB': 49, 'RW': 61, 'RWB': 51, 'ST': 58}, 'Juan Mata': {'CAM': 80, 'CB': 51, 'CDM': 62, 'CF': 77, 'CM': 76, 'GK': 30, 'LB': 58, 'LM': 76, 'LW': 76, 'LWB': 62, 'RB': 58, 'RM': 76, 'RW': 76, 'RWB': 62, 'ST': 72}, 'Anthony Martial': {'ST': 82, 'CAM': 82, 'CB': 57, 'CDM': 62, 'CF': 83, 'CM': 75, 'GK': 32, 'LB': 63, 'LM': 82, 'LW': 82, 'LWB': 66, 'RB': 63, 'RM': 82, 'RW': 82, 'RWB': 66}, 'Anthony Elanga': {'LM': 65, 'CAM': 62, 'CB': 42, 'CDM': 48, 'CF': 62, 'CM': 56, 'GK': 26, 'LB': 49, 'LW': 63, 'LWB': 52, 'RB': 49, 'RM': 65, 'RW': 63, 'RWB': 52, 'ST': 59}, 'Ethan Galbraith': {'CDM': 67, 'CAM': 66, 'CB': 62, 'CF': 64, 'CM': 66, 'GK': 29, 'LB': 65, 'LM': 66, 'LW': 64, 'LWB': 65, 'RB': 65, 'RM': 66, 'RW': 64, 'RWB': 65, 'ST': 62}, 'Mason Greenwood': {'RM': 79, 'CAM': 78, 'CB': 57, 'CDM': 62, 'CF': 78, 'CM': 73, 'GK': 29, 'LB': 62, 'LM': 79, 'LW': 78, 'LWB': 65, 'RB': 62, 'RW': 78, 'RWB': 65, 'ST': 77}, 'Edinson Cavani': {'ST': 85, 'CAM': 80, 'CB': 70, 'CDM': 70, 'CF': 83, 'CM': 77, 'GK': 34, 'LB': 69, 'LM': 78, 'LW': 79, 'LWB': 71, 'RB': 69, 'RM': 78, 'RW': 79, 'RWB': 71}, 'Amad Diallo': {'RM': 68, 'CAM': 66, 'CB': 42, 'CDM': 47, 'CF': 67, 'CM': 59, 'GK': 28, 'LB': 49, 'LM': 68, 'LW': 67, 'LWB': 51, 'RB': 49, 'RW': 67, 'RWB': 51, 'ST': 64}, 'Fred': {'CDM': 83, 'CAM': 81, 'CB': 78, 'CF': 79, 'CM': 82, 'GK': 36, 'LB': 81, 'LM': 81, 'LW': 79, 'LWB': 82, 'RB': 81, 'RM': 81, 'RW': 79, 'RWB': 82, 'ST': 75}, 'Lee Grant': {'GK': 69, 'CAM': 35, 'CB': 33, 'CDM': 35, 'CF': 33, 'CM': 36, 'LB': 31, 'LM': 32, 'LW': 32, 'LWB': 31, 'RB': 31, 'RM': 32, 'RW': 32, 'RWB': 31, 'ST': 33}, 'Scott McTominay': {'CDM': 82, 'CAM': 78, 'CB': 80, 'CF': 78, 'CM': 80, 'GK': 32, 'LB': 78, 'LM': 77, 'LW': 76, 'LWB': 79, 'RB': 78, 'RM': 77, 'RW': 76, 'RWB': 79, 'ST': 78}, 'Victor Lindelöf': {'CB': 81, 'CAM': 72, 'CDM': 80, 'CF': 70, 'CM': 76, 'GK': 33, 'LB': 78, 'LM': 71, 'LW': 69, 'LWB': 77, 'RB': 78, 'RM': 71, 'RW': 69, 'RWB': 77, 'ST': 68}, 'Paul Pogba': {'CM': 87, 'CAM': 86, 'CB': 77, 'CDM': 80, 'CF': 86, 'GK': 30, 'LB': 77, 'LM': 85, 'LW': 84, 'LWB': 78, 'RB': 77, 'RM': 85, 'RW': 84, 'RWB': 78, 'ST': 84}, 'Marcus Rashford': {'LM': 87, 'CAM': 85, 'CB': 64, 'CDM': 70, 'CF': 86, 'CM': 80, 'GK': 34, 'LB': 69, 'LW': 85, 'LWB': 72, 'RB': 69, 'RM': 87, 'RW': 85, 'RWB': 72, 'ST': 85}, 'Sergio Romero': {'GK': 81, 'CAM': 38, 'CB': 32, 'CDM': 36, 'CF': 36, 'CM': 39, 'LB': 31, 'LM': 34, 'LW': 33, 'LWB': 32, 'RB': 31, 'RM': 34, 'RW': 33, 'RWB': 32, 'ST': 34}, 'Donny van de Beek': {'CM': 83, 'CAM': 81, 'CB': 77, 'CDM': 80, 'CF': 81, 'GK': 34, 'LB': 77, 'LM': 80, 'LW': 79, 'LWB': 78, 'RB': 77, 'RM': 80, 'RW': 79, 'RWB': 78, 'ST': 80}, 'Bruno Fernandes': {'CAM': 90, 'CB': 78, 'CDM': 84, 'CF': 88, 'CM': 89, 'GK': 38, 'LB': 82, 'LM': 88, 'LW': 87, 'LWB': 84, 'RB': 82, 'RM': 88, 'RW': 87, 'RWB': 84, 'ST': 86}, 'Nemanja Matić': {'CDM': 80, 'CAM': 74, 'CB': 79, 'CF': 73, 'CM': 77, 'GK': 33, 'LB': 74, 'LM': 71, 'LW': 71, 'LWB': 75, 'RB': 74, 'RM': 71, 'RW': 71, 'RWB': 75, 'ST': 73}, "D'Mani Bughail-Mellor": {'ST': 64, 'CAM': 62, 'CB': 52, 'CDM': 53, 'CF': 63, 'CM': 58, 'GK': 27, 'LB': 54, 'LM': 62, 'LW': 62, 'LWB': 55, 'RB': 54, 'RM': 62, 'RW': 62, 'RWB': 55}, 'Arnau Puigmal': {'CM': 66, 'CAM': 66, 'CB': 61, 'CDM': 64, 'CF': 66, 'GK': 28, 'LB': 64, 'LM': 68, 'LW': 66, 'LWB': 65, 'RB': 64, 'RM': 68, 'RW': 66, 'RWB': 65, 'ST': 63}, 'De Gea': {'GK': 87, 'CAM': 41, 'CB': 36, 'CDM': 41, 'CF': 39, 'CM': 42, 'LB': 37, 'LM': 39, 'LW': 38, 'LWB': 38, 'RB': 37, 'RM': 39, 'RW': 38, 'RWB': 38, 'ST': 37}, 'Axel Tuanzebe': {'CB': 75, 'CAM': 67, 'CDM': 73, 'CF': 64, 'CM': 69, 'GK': 29, 'LB': 72, 'LM': 67, 'LW': 65, 'LWB': 71, 'RB': 72, 'RM': 67, 'RW': 65, 'RWB': 71, 'ST': 62}}
#r = ['Roberto Firmino', 'Curtis Jones', 'Mohamed Salah', 'Naby Keïta', 'Billy Koumetio', 'Ben Woodburn']
#r=['Roberto Firmino']
r=[]
#f = ['Roberto Firmino', 'Alisson']
f=[]
start = time.time()
print(best_lineup(players_position_ratings, required_players=r, forbidden_players=f))
print(time.time()-start)
quit()
ppr_keys = list(players_position_ratings.keys())
for amount in range(1, 12) :
	start = time.time()
	r = []
	for i in range(amount) :
		choice = random.choice(ppr_keys)
		if not choice in r :
			r.append(choice)
	print(r)
	best_line = best_lineup(players_position_ratings, required_players=r)
	print(best_line)
	all_in = True
	for rand in r :
		if not rand in best_line[1] :
			all_in = False
			break
	if not all_in :
		print('ERROR')
		quit()
	print(time.time()-start)
	print()
	print()
"""













"""
	print(players_position_ratings['Roberto Firmino']['CM'], 'CM Rating', formation_name)
	fake_players_position_ratings = {players_position_ratings_key:players_position_ratings[players_position_ratings_key] for players_position_ratings_key in players_position_ratings}
	positions_from_formation = get_positions_from_formation(formation_name)
	new_positions_from_formation = [new_position for new_position in positions_from_formation if not new_position in positions_taken]
	new_players_position_ratings = {key:players_position_ratings[key] for key in players_position_ratings if not key in players_taken}
	all_players = list(new_players_position_ratings.keys())
	all_positions = [convert_outside_position_to_center(p) for p in positions_from_formation]
	best_players = get_best_players_in_each_position(new_players_position_ratings, all_players, all_positions)
	t_a = [get_same_position(pff) for pff in positions_from_formation]
	c_d = {same_positions_key:t_a.count(same_positions_key) for same_positions_key in list(same_positions.keys())}
	corrections = {}
	for required_player in required_players :
		corrections[required_player] = {}
		differences_dictionary = {best_player_pos:players_position_ratings[best_players[best_player_pos][c_d[get_same_position(best_player_pos)]-1]][best_player_pos]-players_position_ratings[required_player][best_player_pos] for best_player_pos in best_players}
		#try :
			#print(differences_dictionary, required_player, formation_name, c_d[get_same_position('CM')]-1, best_players['CM'][c_d[get_same_position('CM')]-1], players_position_ratings[best_players['CM'][c_d[get_same_position('CM')]-1]]['CM'])
		#except :
			#pass
		best_alternatives = sorted(list(differences_dictionary.keys()), key=lambda x: differences_dictionary[x])
		best_alternative_standard = differences_dictionary[best_alternatives[0]]
		print(best_alternatives, 'BEST ALTERNATIVES')
		try :
			print(differences_dictionary, 'DIFFERENCES DICTIONARY', c_d[get_same_position('CM')]-1, best_players['CM'][c_d[get_same_position('CM')]-1], players_position_ratings[best_players['CM'][c_d[get_same_position('CM')]-1]]['CM'])
			print(differences_dictionary, 'DIFFERENCES DICTIONARY', c_d[get_same_position('ST')]-1, best_players['ST'][c_d[get_same_position('ST')]-1], players_position_ratings[best_players['ST'][c_d[get_same_position('ST')]-1]]['ST'])
		except :
			pass
		print()
		for best_alternatives_key in best_alternatives :
			if differences_dictionary[best_alternatives_key] == best_alternative_standard :
				corrections[required_player][best_alternatives_key] = 99
	print()
	print(corrections)
	print()
	"""
