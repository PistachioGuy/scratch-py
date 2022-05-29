import tkinter
from tkinter import *
import json
window = Tk()
window.title("")
canvas = Canvas(window, width=960, height=720, bg="white")
canvas.pack()
projectjson=open("./project/project.json","r")
projectjson=projectjson.read()
projectjson=json.loads(projectjson)
default_bg=(((projectjson.get("targets")[0]).get("costumes")[(projectjson.get("targets")[0]).get("currentCostume")]).get("assetId"))
try:
	scratch_bg=tkinter.PhotoImage(file=("./project/" + default_bg + ".png"))
except:
	scratch_bg=tkinter.PhotoImage(file=("./project/" + default_bg + ".svg"))
canvas.create_image(480, 360, image=scratch_bg, anchor=CENTER)
#print(projectjson)
window.mainloop()
