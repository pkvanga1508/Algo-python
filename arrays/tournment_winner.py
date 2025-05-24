# This is a sample solution to the tournament winner problem.
# Problem: Given a list of competitions and their results, return the name of the team that won the tournament.
# The competitions are represented as a list of lists, where each inner list contains the names of the two teams that competed.
# The results are represented as a list of integers, where each integer is either 0 or 1.
# A 0 indicates that the first team in the competition lost, and a 1 indicates that the first team won.
# The function should return the name of the team that won the tournament.
# The function should have a time complexity of O(n) and a space complexity of O(n).
def tournamentWinner(competitions, results):

    winner = None
    max_points = 0
    team_points = {}

    for index in range(len(competitions)) :
        curr_winner = competitions[index][0] if results[index] == 1 else competitions[index][1]
        curr_points = team_points.get(curr_winner, 0) + 3
        team_points[curr_winner] = curr_points
        if curr_points > max_points:
            winner = curr_winner
            max_points = curr_points

    # Write your code here.
    return winner
