#Factor in energy level
#Energy level has to affect player performance/rating

"""def calculate_morale_loss(player_rating, team_rating) :
	rating_difference = team_rating-player_rating
	loss = (20-rating_difference)*0.5
	if loss < 0 :
		return 0
	return loss


team_rating = 75
for player_rating in range(90) :
	print(player_rating, team_rating, calculate_morale_loss(player_rating, team_rating))
#calculate_morale_loss(player_rating, team_rating)
"""
def get_rate_of_morale_loss(team_rating) :
	minimum_rating_for_loss = team_rating-20
	loss = 0
	loss_change = 0.25
	for player_rating in range(minimum_rating_for_loss-1, 100) :
		loss = round(loss, 2)
		print(team_rating, player_rating, loss)
		loss += loss_change
		loss_change += 0.015

get_rate_of_morale_loss(70)
