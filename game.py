import pygame #When starting a new pygame project import it and then run to see if its workng
	#if it is not working most likely need to install or update pygame in terminal $pip3 install pygame
from sys import exit #look NOTE2 for explanation

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

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

#whenever we want to create text we first need to create an image of the text and then
	#place it on the display surface
	#To work with text there are three different steps 
		#1 Create a font (text size and style) 2. Write text on a surface 3. Blit the text surface (so place the surface on the actual image)
#text_surface = test_font.render(text_info, Anti Aliasing, color) # second step which is writing a text on a surface #render needs three bits of information
	# Anti Aliasing means we smooth the edges of the text, which is not necessary in pixel art, but any other text you want it to be true
text_surface = test_font.render('My Game', False, 'Black')

while True:
	for event in pygame.event.get(): #all the possble events. All the poissble inputs a player can put and the event just loops through it
		if event.type == pygame.QUIT: #looking to see if the player input(event) was quit because if it was then the player can exit the game this will repeat each frame
			pygame.quit()
			exit() #look NOTE2 for explanation
	#draw all our elements
	#update everything
	#screen.blit(surface,position) #bloock mage transfer put one mage on another image
	screen.blit(sky_surface,(0,0))
	screen.blit(ground_surface,(0,300))
	screen.blit(text_surface, (300, 50)) #third step to creating a font
	pygame.display.update() #ths will update the display surface that we had created earlier
		#anything we hae drawn inside of whle loop, we want to display to the player
		#therefore we have to take it and actually put it on the dsplay surface. Like pygame init once you call it you don't have to worry about it anyore

#NOTE1: do not run the code before putting a player input as there is no way to exit the window wthout the code inside the loop for the player to close the window
#NOTE2: pygame.error: video system not initialized ** This is because whenever we have pygame.init which starts pygame and pygame.quit they are polar opposites
	#so we are still closing pygame and having the while loop open so we need to end that whle loop on the spot, most secure is through sys module and close any type of code interily so from sys import exit then call exit under the pygame.quit()
#NOTE3 we dont want our game to run to fast and to run too slow we want t to be constant so we need to wearry of our frame rate and pxels 60 fps - for ceiling and floor
	#computer can run game slower but cant run faster than it's capable of runnng
	clock.tick(60) #tells pygame that while true loop shouldnt run faster than 6-fps


#NOTE4 regular surface - essentiall a sngle mage (somethng mported, rendered text or a plain color) - 
	 #it needs to be placed on the display surface to be visible 
	 #you can have as many regular surfaces as you want, only dsplayed when connect to the display surface whch is unique and s always vsible
#NOTE5 python order matters
