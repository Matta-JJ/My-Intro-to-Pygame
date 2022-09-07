import pygame #When starting a new pygame project import it and then run to see if its workng
	#if it is not working most likely need to install or update pygame in terminal $pip3 install pygame
from sys import exit #look NOTE2 for explanations

pygame.init() #this is to initialize pygame, it's like starting the engine of a car
#The next thing to do is create a display surface, this window the player is going
	#to see at the end - screen = pygame.display.set_mode((width,height)) 
screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption('Runner') #setting title
#So far we have imported pygame we have initialzed pygame and we have created the display surface
#Since the code ends the display surface disappers so we need a way to keep code running forever .. so
	#we need a while true loop, so the conditon inside the while loop will run forever and the only way to break it
	#is from the inside
clock = pygame.time.Clock() #frame rate

# this s temporary to play wth test_surface = pygame.Surface((w,h))
#test_surface = pygame.Surface((100,200))
#test_surface.fill('Red')

#test_font = pygame.font.Font(font type, font size)
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) #creating a font (make sure to captialize second font)

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha() #.convert helps convert the image into something that pygame can work with much easier
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

#whenever we want to create text we first need to create an image of the text and then
	#place it on the display surface
	#To work with text there are three different steps 
		#1 Create a font (text size and style) 2. Write text on a surface 3. Blit the text surface (so place the surface on the actual image)
#text_surface = test_font.render(text_info, Anti Aliasing, color) # second step which is writing a text on a surface #render needs three bits of information
	# Anti Aliasing means we smooth the edges of the text, which is not necessary in pixel art, but any other text you want it to be true
score_surf = test_font.render('My Game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50)


#Next we are wanting to move the snail from the left side of the image to the right
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
#snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha() #just this is static and we need it to move
#snail_x_pos = 600 # we moved the 600 that was in the snail position into a variable
snail_rect = snail_surf.get_rect(bottomright = (600,300))


player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))


while True:
	for event in pygame.event.get(): #all the possble events. All the poissble inputs a player can put and the event just loops through it
		if event.type == pygame.QUIT: #looking to see if the player input(event) was quit because if it was then the player can exit the game this will repeat each frame
			pygame.quit()
			exit() #look NOTE2 for explanation
		#if event.type == pygame.MOUSEMOTION:
			#if player_rect.collidepoint(event.pos): print('collision')

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print('jump')


	#draw all our elements
	#update everything
	#screen.blit(surface,position) #bloock mage transfer put one mage on another image
	screen.blit(sky_surface,(0,0))
	screen.blit(ground_surface,(0,300))
	pygame.draw.rect(screen, '#c0e8ec', score_rect)
	pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
	screen.blit(score_surf, score_rect) #third step to creating a font
	#snail_x_pos -= 4 #this is so that every time the loop runs we move the snails position by 1 so the snail will be moving about 60 frames every second
		#left is -= 1 and right is += 1
	#Our next problem is that we need something to help when the snail moves out of the display window so we use an if statement
	#if snail_surface 
	#if snail_x_pos < -100: snail_x_pos = 800
	snail_rect.x -= 4
	if snail_rect.right <= 0: snail_rect.left = 800
	screen.blit(snail_surf,snail_rect)
	#player_rect.left += 1
	screen.blit(player_surf,player_rect)

	#keys = pygame.key.get_pressed()
	#if keys[pygame.K_SPACE]:
	#	print('jump')

	#if player.rect.colliderect(snail_rect): #this returns either a 0 or 1 if there is no collision we get a one if there is a collision we get a 1
	#rect1.collidepoint(x,y) is important for when you are using clickers

	#mouse_pos = pygame.mouse.get_pos()
	#if player_rect.collidepoint((mouse_pos)):
		#pygame.mouse.get_pressed

	pygame.display.update() #ths will update the display surface that we had created earlier
	clock.tick(60) #tells pygame that while true loop shouldnt run faster than 6-fps
		#anything we hae drawn inside of whle loop, we want to display to the player
		#therefore we have to take it and actually put it on the dsplay surface. Like pygame init once you call it you don't have to worry about it anyore

#NOTE1: do not run the code before putting a player input as there is no way to exit the window wthout the code inside the loop for the player to close the window
#NOTE2: pygame.error: video system not initialized ** This is because whenever we have pygame.init which starts pygame and pygame.quit they are polar opposites
	#so we are still closing pygame and having the while loop open so we need to end that whle loop on the spot, most secure is through sys module and close any type of code interily so from sys import exit then call exit under the pygame.quit()
#NOTE3: we dont want our game to run to fast and to run too slow we want t to be constant so we need to wearry of our frame rate and pxels 60 fps - for ceiling and floor
	#computer can run game slower but cant run faster than it's capable of runnng

#NOTE4: regular surface - essentiall a sngle mage (somethng mported, rendered text or a plain color) - 
	 #it needs to be placed on the display surface to be visible 
	 #you can have as many regular surfaces as you want, only dsplayed when connect to the display surface whch is unique and s always vsible
#NOTE5: python order matters
#NOTE6: How to animate in pygame. We are not drawing static image, but we are updating the image over and over again 60 times a second and placing it in the same place
	# animating each just means changing the position slight on each frame
#NOTE7: Rectangles, Precise positioning of surfaces, helps avoid basic collisions 
#NOTE8: the player character. Keyboard input, jump + gravity, creating a floor
	#two ways to get keyboard input is with method or through event loop
		#Keyboard input in the event loop 1. check if any button was pressed 2 work with a specific key
			#there's two methods because when using classes you want the controls isnide of the relevant class. Pygame.mouse and pygame.keys are great for that
	