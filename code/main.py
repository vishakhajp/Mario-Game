import pygame , sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI
from start import Start
from end import End

class Game:
	def __init__(self):
		# Game attributes
		self.max_level = 7
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0

		self.start = Start(screen)
		self.end = End(screen)

		# Audio
		self.start_music = pygame.mixer.Sound("../audio/start_game.wav")
		self.level_bg_music = pygame.mixer.Sound("../audio/level_music.wav")
		self.overworld_bg_music = pygame.mixer.Sound("../audio/overworld_music.wav")
		self.game_over = pygame.mixer.Sound("../audio/game_over.wav")

		# Overworld creation
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = "start"
		self.start_music.play(loops = -1)

		# User interface
		self.ui = UI(screen)
		


	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health)
		self.status = "level"
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops = -1)
		

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = "overworld"
		self.overworld_bg_music.play(loops = -1)
		self.level_bg_music.stop()

	def change_coins(self,amount):
		self.coins += amount

	def change_health(self,amount):
		self.cur_health += amount

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.max_level,screen,self.create_level)
			self.status = "overworld"
			self.level_bg_music.stop()
			self.overworld_bg_music.play(loops = -1)
			self.status = "end"

	def game_end(self):
		if self.status == "end":
				self.end.draw(screen)
				self.level_bg_music.stop()
				self.overworld_bg_music.stop()
				self.game_over.play(loops = -1)
				self.keys = pygame.key.get_pressed()
				if self.keys[pygame.K_q]:
					self.game_over.stop()
					self.overworld_bg_music.play(loops = -1)
					self.status = "overworld"


	def run(self):
		self.end.draw(screen)
		if self.status == "start":
			self.start.draw(screen)
			self.keys = pygame.key.get_pressed()
			if self.keys[pygame.K_KP_ENTER]:
				self.status = "overworld"
				self.start_music.stop()
				self.overworld_bg_music.play(loops = -1)
			elif self.keys[pygame.K_x]:
				pygame.quit()
				sys.exit()
			

		elif self.status == "overworld":
			self.overworld.run()
			keys = pygame.key.get_pressed()
			if keys[pygame.K_e]:
				self.status = "start"
				self.overworld_bg_music.stop()
				self.start_music.play(loops = -1)
				
				
		else:
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.ui.show_coins(self.coins)
			keys = pygame.key.get_pressed()
			if keys[pygame.K_x]:
				self.status = "overworld"
				self.level_bg_music.stop()
				self.overworld_bg_music.play(loops = -1)
			self.check_game_over()
			self.game_end()
			
				

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Mario")
game = Game()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill('gray')
	game.run()

	pygame.display.update()
	clock.tick(60)
	 