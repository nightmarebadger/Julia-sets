from tkinter import Tk, Canvas, PhotoImage, NW
from random import randint
import time
#import cmath

wid = 1000
hei = 1000
maxiter = 256
blowup = 2



global_colors = []
for i in range(256):
	global_colors.append(( randint(0,255), randint(0,255), randint(0,255) ))



def color(k):
	"""
	if(k == 0):
		return(0,0,0)
	elif(k == 1):
		return(255,0,0)
	elif(k == 2):
		return(0,255,0)
	elif(k == 3):
		return(0,0,255)

	return(global_colors[k%256])
	k = (k*2)**2
	return(k, k, k)
	"""
	#return(global_colors[k%256])
	#return((10*k)%255, (10*k)%255, (100-10*k)%255)
	#return(0,0,0)
	#return((125+k)%255, 0, 0)
	#return((2*k)%255, 0, (50+5*k)%255)
	#return((k*10)%255, (k*10)%255, (k*10)%255)
	return(k%255, (2*k)%255, (3*k)%255)

		
class Mandel:
	def __init__(self, root, x1, y1, x2, y2):

		t = time.time()
		self.img = PhotoImage(width=wid, height=hei)

		canv = Canvas(root, width = wid, height = hei)
		canv.pack()
		canv.create_image(0, 0, image = self.img, anchor=NW)

		dx = abs(x2-x1)/wid
		dy = abs(y2-y1)/hei

		y = y1
		for j in range(hei):
			line = '{'
			x = x1
			
			for i in range(wid):

				x = x + dx
				c = complex(x, y)
				a = 0

				for k in range(maxiter):
					a = a**2 + c
					if(abs(a) > blowup):
						break

				if(k == maxiter-1):
				
					line += '#%02x%02x%02x ' % (255,255,255)
				else:
					
					line += '#%02x%02x%02x ' % color(k)

			line += '}'
			self.img.put(line, (0, j))
			canv.update()
			y = y - dy
			
		print(time.time() - t)




class Jul:
	def __init__(self, root, x1, y1, x2, y2):

		t = time.time()
		self.img = PhotoImage(width=wid, height=hei)

		canv = Canvas(root, width = wid, height = hei)
		canv.pack()
		canv.create_image(0, 0, image = self.img, anchor=NW)

		dx = abs(x2-x1)/wid
		dy = abs(y2-y1)/hei

		#c = complex(-0.8, 0.156)
		#c = complex(-0.74543,+0.11301)
		#c = complex(-0.1,0.651)
		#c = complex(-0.70176,-0.3842)
		c = complex(-0.835,-0.2321)
		#c = complex(-1,0)
		#c = complex(-0.74434, -0.10772)
		#c = complex(-0.62772, 0.42193)

		y = y1
		for j in range(hei):
			line = '{'
			x = x1
			
			for i in range(wid):

				x = x + dx
				a = complex(x, y)

				for k in range(maxiter):
					a = a**2 + c
					#a = a**3 + c
					#a = cmath.sin(a**2) + cmath.cos(c)
					if(abs(a) > blowup):
						break
				#print(k)
				if(k == maxiter-1):
					#print("Hello")
					#line += '#%02x%02x%02x ' % (255,255,255)
					line += '#%02x%02x%02x ' % (0,0,0)
				else:
					
					line += '#%02x%02x%02x ' % color(k)

			line += '}'
			self.img.put(line, (0, j))
			canv.update()
			y = y - dy
			
		print(time.time() - t)

root = Tk()

a = Jul(root, -blowup, blowup, blowup, -blowup)


root.mainloop()
