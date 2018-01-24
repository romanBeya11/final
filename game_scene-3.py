from scene import *
from main_menu_scene import *
import sound
import random
import math
import time
A = Action

class GameScene (Scene):
	def setup(self):
		# Creating 2 arrays which will hold the number of coins, and the number of enemi3s
		self.coin_array = []
		self.enemies_array = []
		
		# Setting up the background
		self.screen_center_x = self.size.x / 2
		self.screen_center_y = self.size.y / 2
		self.bg_pos = Vector2(self.screen_center_x, self.screen_center_y)
		background = SpriteNode(color = 'midnightblue', position = self.bg_pos, parent = self, size = self.size)
		
		# Boundary Detection
		# Setting the ground height
		self.height_of_ground = 35
		# Setting the top of screen boundary
		self.top_of_screen_boundary = self.size.y
		# Left side of screen
		self.left_side_of_screen_boundary = self.screen_center_x - 480
		# Right side of screen
		self.right_side_of_screen_boundary = self.size.x
		
		# Creating player sprite
		self.player_position = Vector2()
		self.player_position.x = self.screen_center_x - 200
		self.player_position.y = self.screen_center_y - 200
		self.player = SpriteNode('plf:HudPlayer_pink', position = self.player_position, parent = self, size = self.size / 10)
		
		# HIT COUNTER FOR COINS
		self.coin_intersect = 0
		self.score_label = Vector2()
		self.score_label.x = self.screen_center_x
		self.score_label.y = self.screen_center_y + 300
		self.score = LabelNode(text = "Coins: 0", position = self.score_label, parent = self, font = ("Copperplate", 40))
		
		# Creating the first enemy
		self.enemy_pos = Vector2()
		self.enemy_pos.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.enemy_pos.y = random.randint(self.height_of_ground, self.score_label.y - 30)
		self.enemies_array.append(SpriteNode('plf:Enemy_Saw_move', position = self.enemy_pos, parent = self, size = self.size / 8))
		
		# Calling this function spawns a coin
		self.create_new_coin()
		
		# While the main game loop is running, everything will function properly, else all game animations stop, when this happens it is game over
		self.begin_main_thread = True
		
	def did_change_size(self):
		pass
			
	def increment_score(self):
		# When this procedure is called, it will increase the score vslue and play a sound!
		self.coin_intersect = self.coin_intersect + 1
		self.score.text = "Coins: " + str(self.coin_intersect)
		sound.play_effect('rpg:HandleCoins')
	
	def decrement_score(self):
		# When this procedure is called, it will decrease the score value and play a sound! 
		self.coin_intersect = self.coin_intersect - 2
		self.score.text = "Coins: " + str(self.coin_intersect)
		sound.play_effect('rpg:HandleCoins2')
		if self.coin_intersect < 0:
			# If the player no longer has any coins left its game over
			self.score.text = "Game Over"
			self.score.color = (.87, .29, .29)
			self.game_over()
			
	def game_over(self):
		# This procedure handles the game over animations
		# Make the score value invisible
		self.score.alpha = 0
		
		# Move the score to the center of the screen
		self.score_label.x = self.screen_center_x
		self.score_label.y = self.screen_center_y
		self.score.run_action(Action.move_to(self.score_label.x, self.score_label.y, 5))
		
		# Show the score label but change the text to say game over
		self.score.run_action(Action.fade_to(1, 3))
		self.score.font = ("Copperplate", 60)
		self.score.color = (1.0, .0, .0)
		
		# Play a sound to indicate its games over
		sound.play_effect('rpg:Chop')
		
		for enemy in self.enemies_array:
			# Make all enemies invisible
			enemy.run_action(Action.fade_to(0, 3))
			
		# make the player invisible
		self.player.run_action(Action.fade_to(0, 3))
		
		for coin in self.coin_array:
			# make all coins invisible
			coin.run_action(Action.fade_to(0, 3))
		
		# return to main menu button
		self.dismiss_scene_button_pos = Vector2()
		self.dismiss_scene_button_pos.x = self.screen_center_x - 400
		self.dismiss_scene_button_pos.y = self.screen_center_y + 300
		self.dismiss_scene_button = SpriteNode('./assets/sprites/left_button.png', position = self.dismiss_scene_button_pos, parent = self, size = self.size / 12)
		
		# now that the game is over the main game loop can stop running
		self.begin_main_thread = False
	
	def create_new_enemy(self):
		# This procedure creates a new enemy each time it is called
		self.enemy_pos = Vector2()
		self.enemy_pos.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.enemy_pos.y = random.randint(self.height_of_ground, self.score_label.y - 30)
		self.enemies_array.append(SpriteNode('plf:Enemy_Saw_move', position = self.enemy_pos, parent = self, size = self.size / 8))
		
	def move_enemy(self):
		# This procedure moves each enemies in a very specific manner
		for e in self.enemies_array:
			# Set a max speed that the enemies can move
			self.enemy_movement_speed = 5
			
			e.run_action(Action.move_to(self.player_position.x, self.player_position.y, self.enemy_movement_speed))
			e.run_action(Action.move_to(self.player_position.x, self.player_position.y, self.enemy_movement_speed))
			
	def enemy_intersect(self):
		# This procedure handles an collision between the player and the enemy
		for enemy in self.enemies_array:
			if self.player.frame.contains_point(enemy.frame):
				self.decrement_score()	
				
	def create_new_coin(self):
		# This procedure creates a new coin each time it is called
		self.new_coin_position = Vector2()
		self.new_coin_position.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.new_coin_position.y = random.randint(self.height_of_ground, self.top_of_screen_boundary)
		self.coin_array.append(SpriteNode('plf:Item_CoinGold', position = self.new_coin_position, parent = self, size = self.size / 13))
	
	def move_coin(self):
		# This procedure moves each coin in a unique way
		random_coin_coordinate_x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		random_coin_coordinate_y = random.randint(self.height_of_ground, self.score_label.y - 30)
		self.coin_speed = 5
		
		for coin in self.coin_array:
			# At the beginning of the game the coin will move in a random direction
			#coin.run_action(Action.move_to(random_coin_coordinate_x, self.player_position.y, self.coin_speed))
			coin.run_action(Action.move_to(-1*self.player_position.x, -1*self.player_position.y, self.coin_speed))
			
			# Handling boundary detection so the coins doesnt fall out of the screen
			# Handling the x coordinates first
			if coin.position.x >= self.right_side_of_screen_boundary:
				# If it hits the side of the screen, pick a random direction in which to travel
				coin.run_action(Action.move_to(self.right_side_of_screen_boundary, random_coin_coordinate_y, self.coin_speed))
			elif coin.position.x <= self.left_side_of_screen_boundary:
				coin.run_action(Action.move_to(random_coin_coordinate_x, random_coin_coordinate_y, self.coin_speed))
				
			# Handling the y coordinate now
			elif coin.position.y >= self.top_of_screen_boundary:
				coin.run_action(Action.move_to(self.left_side_of_screen_boundary, self.top_of_screen_boundary, self.coin_speed))
			elif coin.position.y <= self.height_of_ground:
				coin.run_action(Action.move_to(random_coin_coordinate_x, self.height_of_ground, self.coin_speed))
				
	def coin_to_player_intersection(self):
		# This procedure handles an collision between the coin and the player
		for coin in self.coin_array:
			if self.player.frame.intersects(coin.frame):
				coin.remove_from_parent()
				self.coin_array.remove(coin)
				self.create_new_coin()
				self.increment_score()
				self.create_new_enemy()			
	
	def intiate_gravity(self):
		# GRAVITY STARTS HERE!!
		# The gravity works like this: It is constantly pulling down on the player, however it works by looking at the players y value, and depending on where the player currently is, it is stronger or weaker
		if self.player_position.y == self.height_of_ground:
			self.player_position.y = self.height_of_ground
		else:
			if self.player_position.y >= self.score_label.y - 30:
				self.player_position.y = self.score_label.y - 30
			if self.player_position.x >= self.right_side_of_screen_boundary:
				self.player_position.x = self.right_side_of_screen_boundary
			if self.player_position.x <= self.left_side_of_screen_boundary:
				self.player_position.x = self.left_side_of_screen_boundary
			
			# Find the distance between the ground and the players current position
			# This helps to determine the strength of gravity felt by the player
			distance_to_grnd = self.player_position.y - self.height_of_ground
			if distance_to_grnd <= self.height_of_ground + 20:
				descend = self.player_position.y = self.player_position.y - 2
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					self.player_position.y = self.height_of_ground
			elif distance_to_grnd >= self.height_of_ground + 100:
				descend = self.player_position.y = self.player_position.y - 5
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					self.player_position.y = self.height_of_ground
			else:
				descend = self.player_position.y = self.player_position.y - 8
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					self.player_position.y = self.height_of_ground
		
	def update(self):
		if self.begin_main_thread == True:
			# If the main game is running, ie it is not game over, then proceed
			self.intiate_gravity()
			self.move_coin()
			self.coin_to_player_intersection()
			self.move_enemy()
			self.enemy_intersect()
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
		
	def touch_ended(self, touch):
		if self.begin_main_thread == True:
			# if the main game loop is running, proceed
			# Get the players location when the user touches the screen
			x = self.player_position.x = touch.location.x
			y = self.player_position.y = touch.location.y
			
			# Set a max speed in which the player can move
			self.player_movement_speed = 2
			
			# Move the player to that location
			self.player.run_action(Action.move_by(x, y, self.player_movement_speed))
			
			# Handling boundary detection between the player and the sides of the screen
			if x <= self.left_side_of_screen_boundary:
				x = self.left_side_of_screen_boundary
			elif x >= self.right_side_of_screen_boundary:
				x = self.right_side_of_screen_boundary
			elif y <= self.height_of_ground:
				y = self.height_of_ground
			elif y >= self.score_label:
				y = self.score_label - 30
				
		else:
			# This occurs when it is game over and the main game loop has stopped
			if self.dismiss_scene_button.frame.contains_point(touch.location):
				self.dismiss_modal_scene()
