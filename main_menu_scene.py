
# Created by: Roman Beya
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from tutorial_scene import *
from game_scene import *
from credits_scene import *

import ui


class MainMenuScene(Scene):
    def setup(self):
      # this method is called, when user moves to this scene
			# set background image
			self.background = SpriteNode('./assets/sprites/main_menu_bg.PNG',position = self.size / 2, parent = self, size = self.size)
			
			# I created a bunch of sprites whose frame will be what the user clicks on when the 'tap on a button' because the regular hit map was distoted so this is an unorthodox solution. It works by creating 3 of the same sprites, if the user presses any of the 3 created, it will proceed with a given action.
			
			# I created an opacity variable that will make all the sprites invisible so it looks to the user that they are just clicking the button, when in reality they are pressing one of the sprites
			self.opacity = 0
			
			# This is the first sprites which handles the play button
			self.p1_pos = Vector2() 
			self.p1_pos.x = self.size.x / 2
			self.p1_pos.y = self.size.y / 2 + 100     
			self.start_button = SpriteNode('./assets/sprites/play.PNG', position = self.p1_pos, parent = self, size = self.size / 1)
			
			# Second sprite for play button
			self.p1_pos_1 = Vector2() 
			self.p1_pos_1.x = self.size.x / 2 + 50
			self.p1_pos_1.y = self.size.y / 2 + 100
			self.start_button_1 = SpriteNode('plf:Enemy_Bee' , position = self.p1_pos_1, parent = self, size = self.size / 4, alpha = self.opacity)
			
			# Third sprite for play button
			self.p1_pos_2 = Vector2() 
			self.p1_pos_2.x = self.size.x / 2 - 100
			self.p1_pos_2.y = self.size.y / 2 + 100 
			self.start_button_2 = SpriteNode('plf:Enemy_Bee' , position = self.p1_pos_2, parent = self, size = self.size / 4, alpha = self.opacity)
			
			# Positioning the start button
			self.p1_pos_3 = Vector2() 
			self.p1_pos_3.x = self.size.x / 2 + 200
			self.p1_pos_3.y = self.size.y / 2 + 100
			#self.start_button = SpriteNode('./assets/sprites/play.PNG', position = self.p1_pos_1, parent = self, size = self.size / 8)
			self.start_button_3 = SpriteNode('plf:Enemy_Bee' , position = self.p1_pos_3, parent = self, size = self.size / 4, alpha = self.opacity)
			
			# PLAYER 2!!!!!!!!
			# First sprite for tutorial button
			self.p2_pos = Vector2() 
			self.p2_pos.x = self.size.x / 2
			self.p2_pos.y = self.size.y / 2 - 50
			self.tutorial_button = SpriteNode('./assets/sprites/tutorial.PNG', position = self.p2_pos, parent = self, size = self.size / 1)
			self.tutorial_button_1 = SpriteNode('plf:Enemy_FishPink' , position = self.p2_pos, parent = self, size = self.size / 4, alpha = self.opacity) 
		
			# Second sprite for tutorial button
			self.p2_pos_1 = Vector2() 
			self.p2_pos_1.x = self.size.x / 2 - 100
			self.p2_pos_1.y = self.size.y / 2 - 75
			self.tutorial_button_2 = SpriteNode('plf:Enemy_FishPink' , position = self.p2_pos_1, parent = self, size = self.size / 4, alpha = self.opacity)
			
			# Third sprite for tutorial button
			self.p2_pos_2 = Vector2() 
			self.p2_pos_2.x = self.size.x / 2 + 100
			self.p2_pos_2.y = self.size.y / 2 - 75
			self.tutorial_button_3 = SpriteNode('plf:Enemy_FishPink' , position = self.p2_pos_2, parent = self, size = self.size / 4, alpha = self.opacity)
			
			# PLAYER 3!!!!!!!!	
			# First sprite for credits button
			self.p3_pos = Vector2() 
			self.p3_pos.x = self.size.x / 2
			self.p3_pos.y = self.size.y / 2 - 300
			self.credits_button_1 = SpriteNode('plf:Enemy_Frog' , position = self.p3_pos, parent = self, size = self.size / 4, alpha = self.opacity) 
			
			# Second sprite for credits button
			self.p3_pos_x = Vector2() 
			self.p3_pos_x.x = self.size.x / 2
			self.p3_pos_x.y = self.size.y / 2 - 200
			self.credits_button = SpriteNode('./assets/sprites/credits.PNG', position = self.p3_pos_x, parent = self, size = self.size / 1)
		
		#	Third sprite for credits button
			self.p3_pos_1 = Vector2() 
			self.p3_pos_1.x = self.size.x / 2 - 100
			self.p3_pos_1.y = self.size.y / 2 - 300
			self.credits_button_2 = SpriteNode('plf:Enemy_Frog' , position = self.p3_pos_1, parent = self, size = self.size / 4, alpha = self.opacity)
			
			# Positioning of credit button
			self.p3_pos_2 = Vector2() 
			self.p3_pos_2.x = self.size.x / 2 + 100
			self.p3_pos_2.y = self.size.y / 2 - 300
			self.credits_button_3 = SpriteNode('plf:Enemy_Frog' , position = self.p3_pos_2, parent = self, size = self.size / 4, alpha = self.opacity)  
			                    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
    	# this method is called, when user releases a finger from the screen
    	# IF the user presses any one of the sprites, depending on where they press, a different action will occur
      if self.start_button_1.frame.contains_point(touch.location) or self.start_button_2.frame.contains_point(touch.location) or self.start_button_3.frame.contains_point(touch.location):
				self.present_modal_scene(GameScene())
		
      if self.tutorial_button_1.frame.contains_point(touch.location) or self.tutorial_button_2.frame.contains_point(touch.location) or self.tutorial_button_3.frame.contains_point(touch.location):
				self.present_modal_scene(TutorialScene())
				
      if self.credits_button_1.frame.contains_point(touch.location) or self.credits_button_2.frame.contains_point(touch.location) or self.credits_button_3.frame.contains_point(touch.location):
				self.present_modal_scene(CreditScene())
				#print 'extra credit'
				
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
