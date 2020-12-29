import pygame
pygame.init()

screenWidth, screenHeight = 1000, 500
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Racing Simulator 2020")
clock = pygame.time.Clock()
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

	global buttonWidth, buttonHeight, button1XCoor, button2XCoor, buttonsYCoor
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

def laneLineDrawers(x, y):
	width = 10
	height = 50
	color = (255, 255, 0)
	pygame.draw.rect(window, (color), (x, y, width, height))

def entireWindow():
	window.fill((128, 128, 128))
	laneLineDrawers((screenWidth/2)/1.5, 0)
	laneLineDrawers((screenWidth/2)/1.5, 150)
	laneLineDrawers((screenWidth/2)/1.5, 300)
	laneLineDrawers((screenWidth/2)/1.5, 450)

	laneLineDrawers((screenWidth/2)*1.35, 0)
	laneLineDrawers((screenWidth/2)*1.35, 150)
	laneLineDrawers((screenWidth/2)*1.35, 300)
	laneLineDrawers((screenWidth/2)*1.35, 450)
	pygame.display.update()

gameRunning1 = True
gameRunning2 = True
while gameRunning1:
	while gameRunning2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		startingMenu()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mousePos = pygame.mouse.get_pos()
				if button1XCoor + buttonWidth > mousePos[0] > button1XCoor and buttonsYCoor + buttonHeight > mousePos[1] > buttonsYCoor:
					pygame.quit()
					quit()
					pygame.display.update()
				if button2XCoor + buttonWidth > mousePos[0] > button2XCoor and buttonsYCoor + buttonHeight > mousePos[1] > buttonsYCoor:
					gameRunning2 = False
					break
				pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	entireWindow()
	pygame.display.update()