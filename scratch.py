import pygame
import json
projectjson=open("./project/project.json","r")
projectjson=projectjson.read()
projectjson=json.loads(projectjson)
sprite=["0"]
spritecostume=["0"]
bg=(((projectjson.get("targets")[0]).get("costumes")[(projectjson.get("targets")[0]).get("currentCostume")]).get("md5ext"))
for x in range(len(projectjson.get("targets"))):
	if x == 0:
		continue
	spritecostume.insert(x, str(((projectjson.get("targets")[x]).get("costumes")[(projectjson.get("targets")[x]).get("currentCostume")]).get("md5ext")))
	print(spritecostume)
	print(x)
	sprite.insert(x, ([spritecostume[x], [(projectjson.get("targets")[x]).get("x"),(projectjson.get("targets")[x]).get("y")], (projectjson.get("targets")[x]).get("size"), (projectjson.get("targets")[x]).get("direction")])) # costume, coords, rotation, size
pygame.init()


screen = pygame.display.set_mode([960, 720]) #480, 360


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((255, 255, 255))
	screen.blit(pygame.image.load("./project/" + bg), (0,0))
	for x in range(len(projectjson.get("targets"))):
		if x == 0:
			continue
		costume = pygame.image.load(("./project/" + spritecostume[x]))
		costume = pygame.transform.scale(costume, (costume.get_width()*(sprite[x][3]/50),costume.get_height()*(sprite[x][3]/50)))
		costume = pygame.transform.rotate(costume, sprite[x][3]-90)
		screen.blit(costume, ((sprite[x][1][0]*2+360)-costume.get_width()/2,(360-(sprite[x][1][1]*2)-costume.get_height()/2)))
	pygame.display.flip()
pygame.quit()
