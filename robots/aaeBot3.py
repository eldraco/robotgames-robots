import rg

class Robot:
    def act(self, game):
        #test = self.robot_id
        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # if there are enemies around, attack them
        #self.test += 1
        #print self.test
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

            # move toward the center
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]


#        ['move', (x, y)]
#        ['attack', (x, y)]
#        ['guard']
#        ['suicide']

# location — the robot's location as a tuple (x, y)
# hp — the robot's health as an int
# player_id — the robot's player_id (what "team" it belongs to)
# robot_id — a unique number identifying each robot (only available for robots on your team)
