import os
import json

class GameStats():
    """Track all game statistics"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        
        self.game_active = False
        self.high_score = 0
        self.max_level = 1
        
        self.load_progress()
        
        
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_progress(self):
        try:
            with open('data/saved_progress.json', 'r') as fp:
                progress = json.load(fp)
                self.high_score = progress['high_score']
                self.max_level = progress['max_level']
        except FileNotFoundError:
            print('No saved progress')
            pass

    def save_progress(self):
        progress = {
            'high_score': self.high_score
            , 'max_level': self.max_level
        }
        
        if not os.path.exists('data/'):
            os.mkdir('data/')
        
        with open('data/saved_progress.json', 'w') as fp:
            json.dump(progress, fp)
            print('Progress saved')