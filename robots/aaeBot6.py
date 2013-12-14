import rg

class Robot:
    def act(self, game):
        my_team = self.player_id
        if 'spawn' in rg.loc_types(self.location):
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        else:
            # Get the nearby locations
            near_locations = rg.locs_around(self.location)
            # For each location see if there is a robot there or not...
            for loc in near_locations:
                try:
                    robot_location = game.robots[loc]
                    # There is...
                    # If it is our own robot, just move to the center one step. Stop moving when we reach the center.
                    if game.robots[loc]['player_id'] == my_team and self.location != rg.CENTER_POINT:
                        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
                    elif game.robots[loc]['player_id'] != my_team:
                        return ['attack', loc ]
                except KeyError:
                    # There are no robots there...
                    pass 

        return ['guard']



#for loc_robot in game.robots:
    #print loc_robot
    #print game.robots[loc_robot]
    #print game.robots[loc_robot]['player_id']

#FUNCTIONS
#    after_settings()
#    
#    dist(p1, p2)
#    
#    loc_types = __getitem__(...)
#        x.__getitem__(y) <==> x[y]
#    
#    locs_around(loc, filter_out=None)
#    
#    memodict(f)
#        Memoization decorator for a function taking a single argument
#    
#    set_settings(s)
#    
#    sqrt(...)
#        sqrt(x)
#        
#        Return the square root of x.
#    
#    toward(curr, dest)
#    
#    wdist(p1, p2)
#
#DATA
#    CENTER_POINT = (9, 9)
#    settings = {'obstacle_color': (0.2, 0.2, 0.2), 'suicide_dam..._color':...


#        ['move', (x, y)]
#        ['attack', (x, y)]
#        ['guard']
#        ['suicide']

# location — the robot's location as a tuple (x, y)
# hp — the robot's health as an int
# player_id — the robot's player_id (what "team" it belongs to)
# robot_id — a unique number identifying each robot (only available for robots on your team)
