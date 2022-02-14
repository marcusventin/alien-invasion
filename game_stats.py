class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self.load_high_score()

        # Start game in an inactive state.
        self.game_active = False
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def save_high_score(self):
        filename = 'high_score.txt'
        try:
            with open(filename) as f:
                saved_high_score = int(f.read())
        except Exception:
            with open(filename, 'w') as f:
                f.write(str(self.high_score))
        else:
            if self.high_score > int(saved_high_score):
                f.write(str(self.high_score))
    
    def load_high_score(self):
        filename = 'high_score.txt'
        try:
            with open(filename) as f:
                contents = f.read()
        except FileNotFoundError:
            return(0)
        else:
            try:
                saved_high_score = int(contents)
            except ValueError:
                return(0)
            else:
                return(saved_high_score)
            
