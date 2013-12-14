import rg

class Robot:
    def act(self, game):
        for loc, robot in game.robots.items():
            if robot.player_id == self.player_id:
                print loc
                return ['guard']
