def get_new_change(player_morale, morale_at_default, importance_percentage, change) :
	new_change = change*(player_morale/morale_at_default)
	if change < 0 :
		
	c = abs(abs(change)-(abs(change)*(player_morale/morale_at_default)))*(importance_percentage/100)
	if change < 0 :
		return change+change_to_change
	new = (change*(player_morale/morale_at_default))
	diff = new-change
	if diff == 0 :
		pass
	elif diff > 0 :
		diff = diff*(importance_percentage/100)
	else :
		pass
	if neg :
		return (change*(100-importance_percentage))+diff
	else :
		return -(change+diff)
	
