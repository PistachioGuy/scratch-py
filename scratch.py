import pygame
import json
projectjson=open("./project/project.json","r")
projectjson=projectjson.read()
projectjson=json.loads(projectjson)
sprite=["0"]
spritecostume=["0"]
bg=(((projectjson.get("targets")[0]).get("costumes")[(projectjson.get("targets")[0]).get("currentCostume")]).get("assetId"))
for x in range(len(projectjson.get("targets"))):
	if x == 0:
		continue
	spritecostume.insert(x, str(((projectjson.get("targets")[x]).get("costumes")[(projectjson.get("targets")[x]).get("currentCostume")]).get("assetId")))
	print(spritecostume)
	print(x)
	sprite.insert(x, ([spritecostume[x], [(projectjson.get("targets")[x]).get("x"),(projectjson.get("targets")[x]).get("y")]])) # costume, coords, rotation
pygame.init()


screen = pygame.display.set_mode([960, 720]) #480, 360


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((255, 255, 255))
	screen.blit(pygame.image.load(("./project/" + bg + ".png")), (0,0))
	for x in range(len(projectjson.get("targets"))):
		if x == 0:
			continue
		try:
			screen.blit(pygame.image.load(("./project/" + spritecostume[x] + ".png")), ((sprite[x][1][0]*2+360),(360-(sprite[x][1][1]*2))))
		except:
			screen.blit(pygame.image.load(("./project/" + spritecostume[x] + ".svg")), ((sprite[x][1][0]*2+360),(360-(sprite[x][1][1]*2))))
	pygame.display.flip()
pygame.quit()
