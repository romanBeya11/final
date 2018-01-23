from scene import *
#from main_menu_scene import *
import sound
import random
import math
A = Action

class TutorialScene (Scene):
	def setup(self):
		# Set the center of screen coordinates to placeholders
		self.screen_center_x = self.size.x / 2
		self.screen_center_y = self.size.y / 2
		
		# Setting up background design
		self.background_position = Vector2()
		self.background_position.x = self.screen_center_x
		self.background_position.y = self.screen_center_y
		self.background = SpriteNode(color = 'midnightblue', position = self.background_position, parent = self, size = self.size)
		
		# Creating player sprite
		self.player_position = Vector2()
		self.player_position.x = self.screen_center_x
		self.player_position.y = self.screen_center_y - 200
		self.player = SpriteNode('plf:HudPlayer_pink', position = self.player_position, parent = self, size = self.size / 12)
		
		# Hold the number of tutorials completed as a variable which will change the text on the screen
		self.tutorials_completed = 0
		
		# Implementing tutorial functions
		self.tutorial()
		self.how_to_move_up_tutorial()
		self.how_to_move_down_tutorial()
		self.how_to_move_left_tutorial()
		self.how_to_move_right_tutorial()
		self.collect_coins_tutorial()
		self.avoid_enemies_tutorial()
	
	def tutorial(self):
		# This tutorial handles the instructions that tell the user how to proceed
		self.tutorial_label = Vector2()
		self.tutorial_label.x = self.screen_center_x
		self.tutorial_label.y = self.screen_center_y
		self.tutorial = LabelNode(text = "Tap twice with one finger", position = self.tutorial_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5)
		self.tutorial_fade = True
			
	def how_to_move_up_tutorial(self):
		# This tutorial shows the user how to ascend
		self.tutorial_up_label = Vector2()
		self.tutorial_up_label.x = self.screen_center_x
		self.tutorial_up_label.y = self.screen_center_y 
		self.tutorial_up = LabelNode(text = "Tap Upwards To Ascend", position = self.tutorial_up_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
		
	def how_to_move_down_tutorial(self):
		# This tutorial shows the user how to descend
		self.tutorial_down_label = Vector2()
		self.tutorial_down_label.x = self.screen_center_x
		self.tutorial_down_label.y = self.screen_center_y
		self.tutorial_down = LabelNode(text = "Tap Downwards To Descend", position = self.tutorial_down_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
		
	def how_to_move_left_tutorial(self):
		# This tutorial shows the user to move left
		self.tutorial_left_label = Vector2()
		self.tutorial_left_label.x = self.screen_center_x
		self.tutorial_left_label.y = self.screen_center_y
		self.tutorial_left = LabelNode(text = "Tap Left To Jump To The Left", position = self.tutorial_left_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
	
	def how_to_move_right_tutorial(self):
		# This tutorial shows the user to move right
		self.tutorial_right_label = Vector2()
		self.tutorial_right_label.x = self.screen_center_x
		self.tutorial_right_label.y = self.screen_center_y
		self.tutorial_right = LabelNode(text = "Tap Right To Jump To The Right", position = self.tutorial_right_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
	
	def collect_coins_tutorial(self):
		# This tutorial shows the user to move towards coins for their bounty
		self.collect_coins_label = Vector2()
		self.collect_coins_label.x = self.screen_center_x
		self.collect_coins_label.y = self.screen_center_y
		self.collect_coins = LabelNode(text = "Collect Coins", position = self.collect_coins_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
		
	def avoid_enemies_tutorial(self):
		# This tutorial shows the user to avoid enemies(grey guys)
		self.avoid_enemies_label = Vector2()
		self.avoid_enemies_label.x = self.screen_center_x
		self.avoid_enemies_label.y = self.screen_center_y
		self.avoid_enemies = LabelNode(text = "Avoid Enemies", position = self.avoid_enemies_label, parent = self, font = ("Copperplate", 60), color = "yellow", size = self.size / 5, alpha = 0)
	
	def implement_escape_button(self):
		# This button will be shown at the end of the tutorial to return to the main menu
		self.escape_button_pos = Vector2()
		self.escape_button_pos.x = self.screen_center_x - 400
		self.escape_button_pos.y = self.screen_center_y + 300
		self.escape_button = SpriteNode('./assets/sprites/left_button.png', position = self.escape_button_pos, parent = self, size = self.size / 12)
		
	def did_change_size(self):
		pass
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		# The tutorials work by a number of touches
		# every 2 touch the user will see new info regarding how to play the game
		# if they only tap once, the tutorial will fade away
		# Fade away the tutorial
		self.tutorials_completed = self.tutorials_completed + 1
		if self.tutorials_completed == 1:
			self.tutorial.run_action(Action.fade_to(0, 1))
		elif self.tutorials_completed == 2:
			self.tutorial_up.run_action(Action.fade_to(1, 1))
		elif self.tutorials_completed == 3:
			self.tutorial_up.run_action(Action.fade_to(0, 1))
		elif self.tutorials_completed == 4:
			self.tutorial_down.run_action(Action.fade_to(1, 1)) 
		elif self.tutorials_completed == 5:
			self.tutorial_down.run_action(Action.fade_to(0, 1)) 
		elif self.tutorials_completed == 6:
			self.tutorial_left.run_action(Action.fade_to(1, 1)) 
		elif self.tutorials_completed == 7:
			self.tutorial_left.run_action(Action.fade_to(0, 1)) 
		elif self.tutorials_completed == 8:
			self.tutorial_right.run_action(Action.fade_to(1, 1)) 
		elif self.tutorials_completed == 9:
			self.tutorial_right.run_action(Action.fade_to(0, 1)) 
		elif self.tutorials_completed == 10:
			self.collect_coins.run_action(Action.fade_to(1, 1)) 
		elif self.tutorials_completed == 11:
			self.collect_coins.run_action(Action.fade_to(0, 1)) 
		elif self.tutorials_completed == 12:
			self.avoid_enemies.run_action(Action.fade_to(1, 1)) 
		elif self.tutorials_completed == 13:
			self.avoid_enemies.run_action(Action.fade_to(0, 1)) 
			
			# Implement the escape button now
			self.escape_button_pos = Vector2()
			self.escape_button_pos.x = self.screen_center_x - 400
			self.escape_button_pos.y = self.screen_center_y + 300
			self.escape_button = SpriteNode('./assets/sprites/left_button.png', position = self.escape_button_pos, parent = self, size = self.size / 12)
		
		elif self.escape_button.frame.contains_point(touch.location):
			# when they press here, return to main menu
			self.dismiss_modal_scene()
