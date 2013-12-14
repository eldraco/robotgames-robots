# Hi arkamar!!!
# This is the future bot7... so far there are no changes with respect to bot6.
# Hi...

# Hi ElDraco, I will begin my TODOs with AR.

# In the new logic i would love not to go to the center, but to wait in the circle...
# to change in the logic?:
# elif game.robots[loc]['player_id'] != my_team and 'spawn' in rg.loc_types(loc):
# elif game.robots[loc]['player_id'] != my_team and rg.wdist(loc, rg.CENTER_POINT) > rg.wdist(self.location, rg.CENTER_POINT)
# TODO AR: instead of rg.dist function we should preffer rg.wdist because it works with manhattan distance which is better for this robots. OK wdist.

import rg

class Robot:
    def act(self, game):
        my_team = self.player_id
        if 'spawn' in rg.loc_types(self.location):
            # Store the position of the spawning point
            self.spawn_loc = self.location
            # Just move one place toward the center
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        else:
            # Get the nearby locations
            near_locations = rg.locs_around(self.location)
            # For each location see if there is a robot there or not...
            for loc in near_locations:
                try:
                    robot_location = game.robots[loc]
                    # There is...

                    # TODO AR: there is problem. When robots from our team are near to each other
                    # they start moving to the center. in late phases of game it will be more often.

                    # If it is our own robot, just move to the center one step. If we are more than 1 distance from the spawning location, stop moving.
                    # this is to avoid moving to the center.
                    #if game.robots[loc]['player_id'] == my_team and self.location != rg.CENTER_POINT: 
                    if game.robots[loc]['player_id'] == my_team and rg.wdist(self.location,self.spawn_loc) == 1:
                        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
                    # Just to take advantage of the situation, if there is an enemy near, attack it.
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
