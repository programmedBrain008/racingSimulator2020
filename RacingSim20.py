
import pygame
import time
import random 

pygame.init()

screenWidth, screenHeight = 800, 900
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Racing Simulator 2020")
clock = pygame.time.Clock()

CarImg = pygame.image.load("CarForRacingSim2020.png")

def startingMenu():
	window.fill((0, 0, 0))
	lineWidth = 10
	lineHeight = 50
	pygame.draw.rect(window, (255, 255, 0), (screenWidth/2 - lineWidth/2, 0, lineWidth, lineHeight))
	pygame.draw.rect(window, (255, 255, 0), (screenWidth/2 - lineWidth/2, 150, lineWidth, lineHeight))
	pygame.draw.rect(window, (255, 255, 0), (screenWidth/2 - lineWidth/2, 300, lineWidth, lineHeight))
	pygame.draw.rect(window, (255, 255, 0), (screenWidth/2 - lineWidth/2, 450, lineWidth, lineHeight))
	pygame.draw.rect(window, (255, 255, 0), (screenWidth/2 - lineWidth/2, 500, lineWidth, lineHeight))

	font = pygame.font.SysFont("comicsans", 90, True, True)
	title = font.render("Racing Simulator 2020", 1, (0, 255, 255))
	window.blit(title, (screenWidth/2 - title.get_width()/2, screenHeight/2 - title.get_height()/2))
	pygame.draw.rect(window, (0, 0, 255), (80, screenHeight/2 + 30, title.get_width(), 10))
	pygame.display.update()
	clock.tick(20)

	buttonWidth = 150
	button1XCoor = (screenWidth/2)/2 - buttonWidth/2
	button2XCoor = (screenWidth/2)*1.5 - buttonWidth/2
	buttonsYCoor = 350
	buttonHeight = 75

	pygame.draw.rect(window, (190, 0, 0), (button1XCoor, 350, buttonWidth, buttonHeight))
	pygame.draw.rect(window, (0, 190, 0), (button2XCoor, 350, buttonWidth, buttonHeight))
	font = pygame.font.SysFont("comicsans", 35)
	quit = font.render("QUIT", 1, (0, 0, 0))
	window.blit(quit, (button1XCoor + 40, buttonsYCoor + 25))
	start = font.render("GO", 1, (0, 0, 0))
	window.blit(start, (button1XCoor + 555, buttonsYCoor + 25))
	mousePos = pygame.mouse.get_pos()
	
	if button1XCoor + buttonWidth > mousePos[0] > button1XCoor and buttonsYCoor + buttonHeight > mousePos[1] > buttonsYCoor:
		pygame.draw.rect(window, (255, 0, 0), (button1XCoor, buttonsYCoor, buttonWidth, buttonHeight))
		font = pygame.font.SysFont("comicsans", 35)
		quit = font.render("QUIT", 1, (0, 0, 0))
		window.blit(quit, (button1XCoor + 40, buttonsYCoor + 25))
		pygame.display.update()

	if button2XCoor + buttonWidth > mousePos[0] > button2XCoor and buttonsYCoor + buttonHeight > mousePos[1] > buttonsYCoor:
		pygame.draw.rect(window, (0, 255, 0), (button2XCoor, buttonsYCoor, buttonWidth, buttonHeight))
		font = pygame.font.SysFont("comicsans", 35)
		start = font.render("GO", 1, (0, 0, 0))
		window.blit(start, (button1XCoor + 555, buttonsYCoor + 25))
		pygame.display.update()

	pygame.display.update()

def obstaclesDodged(count):
	font = pygame.font.SysFont("comicsans", 30)
	text = font.render("Obstacles Dodged: " + str(count), 1, (0, 255, 255))
	window.blit(text, (10, 10))

def racecar(x, y):
	window.blit(CarImg, (x, y))
	pygame.display.update()
def message_display(text, fontSize, yPoos):
	font = pygame.font.SysFont("comicsans", fontSize)
	actualText = font.render(text, 1, (0, 0, 0))
	window.blit(actualText, (screenWidth/2 - actualText.get_width()/2, yPoos))
	pygame.display.update()

	time.sleep(2)

	gameLoop()

def crashedFromBoundry():
	message_display("You Crashed!", 120, (screenHeight/2)/2)
def crashedFromObstacle():
	message_display("You Crashed!", 120, (screenHeight/2)/2)

def obstacles(obstacleX, obstacleY, obstacleWidth, obstacleHeight, obstacleColor):
	pygame.draw.rect(window, (obstacleColor), (obstacleX, obstacleY, obstacleWidth, obstacleHeight))
	pygame.display.update()


def gameLoop():
	x = (screenWidth * 0.45)
	y = (screenHeight * 0.65)
	carWidth = 100
	carHeight = 200
	x_change = 0

	obstacle_startx = int(random.randrange(0, screenWidth))
	obstacle_starty = -600
	obstacle_velocity = 3
	obstacle_width = 100
	obstacle_height = 100

	dodged = 0

	gameExited = False

	while not gameExited:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				 if event.key == pygame.K_LEFT:
				 	x_change = -5
				 if event.key == pygame.K_RIGHT:
				 	x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change

		window.fill((128, 128, 128))

		# obstacles(obstacleX, obstacleY, obstacleWidth, obstacleHeight, obstacleColor)
		obstacles(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height, (0, 255, 255))
		obstacle_starty += obstacle_velocity

		racecar(x, y)
		obstaclesDodged(dodged)

		if x > screenWidth - carWidth or x < 0:
			crashedFromBoundry()

		if obstacle_starty > screenHeight:
			obstacle_starty = 0 - obstacle_height
			obstacle_startx = random.randrange(0, screenWidth)
			dodged += 1
			obstacle_velocity += 1
			obstacle_width += (dodged * 1.2)

		if y < obstacle_starty + obstacle_height:
			if x > obstacle_startx and x < obstacle_startx + obstacle_width or x + carWidth > obstacle_startx and x + carWidth < obstacle_startx + obstacle_width:
				crashedFromObstacle()

		pygame.display.update()
		clock.tick(60)

gameLoop()
pygame.quit()  
quit()