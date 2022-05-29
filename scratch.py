import tkinter
from cairosvg import svg2png
from tkinter import *
import json
from PIL import Image, ImageTk
import time
window = Tk()
window.title("")
canvas = Canvas(window, width=960, height=720, bg="white")
canvas.pack()
projectjson=open("./project/project.json","r")
projectjson=projectjson.read()
projectjson=json.loads(projectjson)
default_bg=(((projectjson.get("targets")[0]).get("costumes")[(projectjson.get("targets")[0]).get("currentCostume")]).get("assetId"))
try:
	scratch_bg=ImageTk.PhotoImage(Image.open("./project/" + default_bg + ".png"))
except:
	scratch_bg=ImageTk.PhotoImage(Image.open("./project/" + default_bg + ".svg"))
canvas.create_image(480, 360, image=scratch_bg, anchor=CENTER)
for x in range(len(projectjson.get("targets"))):
	if x == 0:
		continue
	print(x)
	exec('spritecostume'+str(x)+'=(((projectjson.get("targets")[x]).get("costumes")[(projectjson.get("targets")[x]).get("currentCostume")]).get("assetId"))')
	try:
		exec('spritecostume'+str(x)+'=ImageTk.PhotoImage(Image.open("./project/" + spritecostume'+str(x)+' + ".png").resize([int(Image.open("./project/" + spritecostume'+str(x)+' + ".png").size[0]*2*(float(projectjson.get("targets")[x].get("size"))/100)), int(Image.open("./project/" + spritecostume'+str(x)+' + ".png").size[1]*2*(float(projectjson.get("targets")[x].get("size"))/100))]).rotate(90-float(projectjson.get("targets")[x].get("direction")), expand=1))')
	except:
		exec('svg_code=open(("./project/" + spritecostume'+str(x)+' + ".svg"), "r")')
		svg_code=svg_code.read()
		svg2png(bytestring=svg_code,write_to='temp.png')
		exec('spritecostume'+str(x)+'=ImageTk.PhotoImage(Image.open("./temp.png").resize([int(Image.open("./temp.png").size[0]*2*(float(projectjson.get("targets")[x].get("size"))/100)), int(Image.open("./temp.png").size[1]*2*(float(projectjson.get("targets")[x].get("size"))/100))]).rotate(90-float(projectjson.get("targets")[x].get("direction")), expand=1))')
	exec('spritecoords'+str(x)+'=[((((projectjson.get("targets")[x]).get("x")*2)+480)), (720-(((projectjson.get("targets")[x]).get("y")*2)+360))]')
	exec('canvas.create_image(spritecoords'+str(x)+'[0], spritecoords'+str(x)+'[1], image=spritecostume'+str(x)+')')

#print(projectjson)
window.mainloop()
