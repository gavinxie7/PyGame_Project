class GameStats():
    #track statistics for alien invasion

    def __init__(self,ai_settings):
        #initizlize statistics
        self.ai_settings=ai_settings
        self.reset_stats()

        #start alien invasion in an acticve state
        self.game_active=True

    def reset_stats(self):
        #initialize statistics that can change during the game
        self.ships_left=self.ai_settings.ship_limit
