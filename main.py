from __future__ import print_function

from nba_py import Scoreboard
from nba_py import game,team,player



def print_score(hometeam,awayteam,game_id):
    homesummary = team.TeamSummary(hometeam)
    awaysummary = team.TeamSummary(awayteam)
    box = game.BoxscoreSummary(game_id=game_id)
    print(homesummary.info()['TEAM_ABBREVIATION'][0], ':', box.line_score()['PTS'][0])
    print(awaysummary.info()['TEAM_ABBREVIATION'][0], ':', box.line_score()['PTS'][1])
def winner(hometeam,awayteam):
    homeroster = team.TeamCommonRoster(hometeam)
    awayroster = team.TeamCommonRoster(awayteam)
    homeprediction = 0
    awayprediction = 0
    homeplayeridlist = []
    awayplayeridlist = []
    for x in homeroster.roster()['PLAYER_ID']:
        homeplayeridlist.append(x)
    for x in awayroster.roster()['PLAYER_ID']:
        awayplayeridlist.append(x)
    for x  in homeplayeridlist:
        try:
            homeplayer = player.PlayerLastNGamesSplits(x).last10()
            homeprediction = homeplayer['PLUS_MINUS'][0] + homeprediction
        except:
            print('error caught')

    for x in awayplayeridlist:
        try:
            awayplayer = player.PlayerLastNGamesSplits(x).last10()
            awayprediction = awayplayer['PLUS_MINUS'][0] + awayprediction
        except:
            print('error caught')
    homeprediction = homeprediction/5+2.33
    awayprediction = awayprediction/5
    homesummary = team.TeamSummary(hometeam)
    awaysummary = team.TeamSummary(awayteam)
    print(homesummary.info()['TEAM_ABBREVIATION'][0],"and",awaysummary.info()['TEAM_ABBREVIATION'][0], ":",(homeprediction-awayprediction))
    #print(awaysummary.info()['TEAM_ABBREVIATION'][0], ":", awayprediction)
# print pbp.info()
today = Scoreboard(month=12, day=25, year=2016)
todayframe = today.game_header()
print(todayframe)
print(todayframe.shape[0])
for x in range(todayframe.shape[0]):
    hometeam = ((todayframe['HOME_TEAM_ID'])[x])
    awayteam = ((todayframe['VISITOR_TEAM_ID'])[x])
    gameid = ((todayframe['GAME_ID'])[x])
    print ("This is game #",x)
    gamestatus = ((todayframe['GAME_STATUS_ID'])[x])
    #print_score(hometeam,awayteam,gameid)
    winner(hometeam,awayteam)
    homesummary = team.TeamSummary(hometeam)
    awaysummary = team.TeamSummary(awayteam)


