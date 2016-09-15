#!/usr/bin/python
import numpy as np
from Tkinter import *
from read import *
root = Tk()
root.title('Sudoku')
class Board():
	'''
	This class defines the board where the canvas will be and its methods
	'''
	canvas = Canvas(root, width=450, height=450, bg="white")
	def drawboard(self):
		'''
		Draws the grill
		'''
		def dibuja(w1, h1, w2, h2, lwidth):
			'''
			function to draw any line
			'''
			line = self.canvas.create_line(w1,h1,w2,h2, width = lwidth)
		for ir in range(9):
			dibuja(0, ir*50, 450, ir*50, 1)
		for ic in range(9):
			dibuja(ic*50,0 , ic*50, 450, 1)	
		for i in range(3):
			dibuja(0, i*150, 450, i*150,3)
		for j in range(9):
			dibuja(j*150,0 , j*150, 450, 3)	
	def __init__(self, root):
		'''
		draws the grill and binds the mouse click with the board to be able to introduce a number by clicking
		'''
		self.drawboard()
		self.canvas.bind('<Button-1>', self.click)
	def click(self,event):
		'''
		Gets the mouse x and y coordinates and send them to the casilla class
		'''
		x = event.x
		y = event.y
		casillita = Casilla()
		root.bind_all('<Key>', casillita.key)
		casillita.casilla(x,y)
	canvas.pack()
class Texto():
	'''
	Class to define the message board.
	'''
	text = Canvas(root, width=450, height=40, bg="white")
	def insertotexto(self,pancarta):
		'''
		Insert function to write the message
		'''
		self.text.create_rectangle(0,0,450,45, fill='white')
		self.text.create_text(220, 20, text=pancarta, fill='blue', font=('Helvectica', '16'))
	text.pack()
class Casilla():	
	
	def casilla(self,x,y):
		'''
		Calculates the corresponding box to the given x and y coordinates and if its not an initial number draws the "input box".
		'''
		global rows
		global cols
		rows = int((x/50))+1
		cols = int((y/50))+1		
		if matrizini[cols-1][rows-1] == 0:
			board.canvas.create_rectangle(2 + (50*(rows-1)) ,2 + (50 * (cols-1)),48+(50*(rows-1)),48+(50*(cols-1)),outline = 'grey', fill = 'white')
	def inserto(self,rows,cols,numero):
		'''
		if not an initial value inserts the desired new value
		'''
		if matrizini[cols-1][rows-1] == 0:
			board.canvas.create_text(25+(50*(rows-1)),25+(50*(cols-1)), text=numero, fill='purple', font=('Helvectica', '16'))
	def inser(self,rows,cols,value):
		'''
		if not an initial value reset the previus value of the box and cleans the area
		'''
		if matrizini[cols-1][rows-1] == 0:
			answr[cols-1][rows-1] = 0
			board.canvas.create_rectangle(1.5+(50*(rows-1)) ,1.5+(50 * (cols-1)),49+(50*(rows-1)),49+(50*(cols-1)),fill = 'white', width=0)
			answr[cols-1][rows-1] = value
			self.inserto(rows,cols,value)
	def key(self, event):
		'''
		Defining each number to draw the number desired
		'''
		if event.keysym == '1':
			self.inser(rows,cols,1)
		if event.keysym == '2':
			self.inser(rows,cols,2)
		if event.keysym == '3':
			self.inser(rows,cols,3)
		if event.keysym == '4':
			self.inser(rows,cols,4)
		if event.keysym == '5':
			self.inser(rows,cols,5)
		if event.keysym == '6':
			self.inser(rows,cols,6)
		if event.keysym == '7':
			self.inser(rows,cols,7)
		if event.keysym == '8':
			self.inser(rows,cols,8)
		if event.keysym == '9':
			self.inser(rows,cols,9)
board = Board(root)
texto = Texto()
class Boton:
	'''
	Class button
	'''
	def botton(self,sitio,texto,comando):
		self.boton = Button(sitio, text=texto, command=comando)
		self.boton.pack(side=LEFT)
boton = Boton()
class Sudoku():
	def __init__(self, root):
		'''
		Defining the UI of the sudoku.
		'''
		self.mainframe = Frame(root)
		self.mainframe.pack()
		self.insert = boton.botton(self.mainframe, 'Insert', self.insert)
		self.reset = boton.botton(self.mainframe, 'Reset', self.reset)
		self.delete = boton.botton(self.mainframe, 'Delete', self.delete)
		self.solve = boton.botton(self.mainframe, 'Solve', self.auto)
		self.validate = boton.botton(self.mainframe, 'Validate', self.comprobar)		
		self.quit = boton.botton(self.mainframe, 'Quit', self.close)
	def close(self):
		self.mainframe.quit()
	def reset(self):
		self.draw()
		i = 0
		j = 0
		while i < len(matrizini):
			while j<len(matrizini[0]):
				answr[i][j] = matrizini[i][j]
				j+=1
			j=0
			i+=1	
#--------------------------------------------------------------------------------------------------------------------#
	def insert(self):
		numero = Tk()
		class Numero:
			def __init__(self,numero):
				self.secframe = Frame(numero)
				self.secframe.pack()
				Label(self.secframe, text='enter the row').pack(side=TOP, padx=10,pady=10)	
				self.ro = Entry(self.secframe, width=10)#row entry
				self.ro.pack()
				Label(self.secframe, text='enter the column').pack(side=TOP, padx=10,pady=10)
				self.col = Entry(self.secframe, width=10)#column entry
				self.col.pack()
				Label(self.secframe, text='enter the number').pack(side=TOP, padx=10,pady=10)
				self.val = Entry(self.secframe, width=10)#number to insert entry
				self.val.pack()
				self.send = boton.botton(self.secframe,'Insert',self.insertnumb)#insert button
				self.cancel = boton.botton(self.secframe,'Cancel',self.closes)#cancel button
			def closes(self):
				numero.destroy()
			def insertnumb(self):
				try:
					rows= int(self.ro.get())	# ------------------------------------- #
					cols = int(self.col.get())	# Gathering the values from the entries #
					value = int(self.val.get())	# ------------------------------------- #
					flag = 0
					if 1<= cols <= 9 and 1<= rows <= 9 and 1<= value <= 9:
						flag = 1
					if  flag == 1 and answr[rows-1][cols-1] == 0:
						answr[rows-1][cols-1] = value
						num = board.canvas.create_rectangle(2 + (50*(cols-1)) ,2 + (50 * (rows-1)),48+(50*(cols-1)),48+(50*(rows-1)), fill = 'white', width=0)
						numb = board.canvas.create_text(25+(50*(cols-1)),25+(50*(rows-1)), text=value, fill='purple', font=('Helvectica', '16'))
						pancarta = 'INSERTED',value,'AT','(',cols,',',rows,')'
					else:
						if flag == 1:
							pancarta = 'NON EMPTY BOX'	
						else:
							pancarta = 'WRONG VALUE'
				except:
					pancarta = 'PLEASE INSERT A VALID NUMBER' 

				texto.insertotexto(pancarta)
				numero.destroy()
		nume = Numero(numero)
#--------------------------------------------------------------------------------------------------------------------#
	def delete(self):
		'''
		Function to delete the desired number from the board and from the answer matrix
		'''
		numerodel = Tk()
		class Del:
			def __init__(self,numerodel):
				self.terframe = Frame(numerodel)
				self.terframe.pack()
				Label(self.terframe, text='enter the row').pack(side=TOP, padx=10,pady=10)	
				self.ro = Entry(self.terframe, width=10)#row entry
				self.ro.pack()
				Label(self.terframe, text='enter the column').pack(side=TOP, padx=10,pady=10)
				self.col = Entry(self.terframe, width=10)#column entry
				self.col.pack()
				self.send = boton.botton(self.terframe, 'Delete', self.delet)
				self.cancel = boton.botton(self.terframe, 'Cancel', self.closes)
			def closes(self):
				numerodel.destroy()
			def delet(self):
		    		'''
		    		Actually this function its the one which does the work
		    		'''
				try:    						#same as in insert function
					rows= int(self.ro.get())
					cols = int(self.col.get())
					value = 3
					if answr[rows-1][cols-1] == 0:	#checks if the box is empty...if so it shows an error message
						pancarta = 'EMPTY BOX'
					if matrizini[rows-1][cols-1] != 0:	#checks if the box is filled with an initial matrix value, if so it doesn't delete it and alerts of the error
						pancarta = 'UNABLE TO DELETE'    
					else:
						answr[rows-1][cols-1] = 0	#cleans the spot in the answer matrix
						num = board.canvas.create_rectangle(2 + (50*(cols-1)) ,2 + (50 * (rows-1)),48+(50*(cols-1)),48+(50*(rows-1)), fill = 'white', width=0)	#cleans the area where the number were
						pancarta = 'DELETED'
				except:	#to check if the entries have invalid characters
					pancarta = 'PLEASE INSERT A VALID NUMBER'        
				texto.insertotexto(pancarta)
				numerodel.destroy()
		dele=Del(numerodel)
#--------------------------------------------------------------------------------------------------------------------#	
	def draw(self):
		board.canvas.create_rectangle(0,0,450,450,fill='white', width=0)
		board.drawboard()
		basic(matrizini)
		pancarta = 'RESETED'
		texto.insertotexto(pancarta)
#--------------------------------------------------------------------------------------------------------------------#
	def auto(self):
		'''
		shows the solution of the current sudoku
		'''
		resultado = readresult(sol)		#reads the solution matrix from read module
		self.draw()	#redraw the grill
		i = 0
		j = 0
		while i < len(resultado):
			while j<len(resultado[0]):
				numero = resultado[i][j]
				if numero != matrizini[i][j]:	#if the value isn't in the initial matrix it draws it in purple
					answr[i][j] = numero
					board.canvas.create_text(25+(50*(j)),25+(50*(i)), text=numero, fill='purple', font=('Helvectica', '16'))
				else:				#else draws it in blue
					board.canvas.create_text(25+(50*(j)),25+(50*(i)), text=numero, fill='blue', font=('Helvectica', '16'))                     
				j += 1
			i+=1
			j=0 
		pancarta = 'SOLVED'
		texto.insertotexto(pancarta)	
# ----------------------------------------------------------------------- #
	def mirobien(self):
		'''
		checks if there's any number repeated in any 3x3 area.
		'''
		pancarta = 'CORRECT'
		i = 0
		j = 0
		fila = 0
		cuadrado = 0
		granfila = 0
		while i < (len(answr)*3) and flag == 1:
			while j < len(answr[0]) and flag == 1:
				Fila = i%3
				Columna = j%3
				if fila < 3 and cuadrado < 9 and granfila < 27:
					fila += 1
					cuadrado += 1
					granfila += 1
					tres[Fila][Columna] = answr[Fila+l][Columna+p]
					a = 0
					b = 0
					while a < len(tres) and flag == 1:
						while b < len(tres[0]) and flag == 1:
							c = 0
							d = 0
							while c < len(tres) and flag == 1:
								while d < len(tres[0]) and flag == 1:
									if tres[a][b] == tres[d][c] and c!=b and tres[a][b] != 0:
										pancarta = 'WRONG'
										flag = 0
									d += 1
								d = 0
								c += 1	
							b += 1
						b=0
						a += 1
	       			if fila==3 and cuadrado<9 and granfila<27:	#if it has ended a row it resets and skips to the next one
	       				fila=0
	       				i+=1
	       			if cuadrado==9 and granfila<27:	#if it has ended a 3x3 matrix it resets and skips to the next one
	       				cuadrado=0
	       				fila=0
	       				tres = np.zeros((3,3),dtype = int8)	#reset the 3x3 matrix to refill it again
	       				p += 3
	       			if granfila == 27:	# if it has ended a row of 3x3 matrixes it resets and skips to the next one
					granfila=0
	       				p=0
	       				cuadrado=0
	       				fila=0
	       				tres = np.zeros((3,3),dtype = int8)	#again it resets the matrix
	       				l+= 3
	       			j += 1
	       		j=0
	       		i+=1				
		return pancarta
	def comprobante(self):
		i = 0
		j = 0
		a = 1
		pancarta = 'vale'
		while i < len(answr) and a == 1:
			while j<len(answr[0]) and a == 1:
				if answr[i][j] == 0:
					pancarta = 'no'
					a = 0
				j += 1
			j=0
			i+=1
		if pancarta == 'vale':
			pancarta = self.mirobien(self)
		else:
			pancarta = 'WRONG'
		return pancarta	#-------------------------------------------------------------------------------------------------------------------#
	def comprobar(self):
		'''
		checks if the sudoku is succesfully completed
		'''
		resultado = readresult(sol)	#reads the solution matrix
		i = 0
		j = 0
		flag = 0
		while i < len(answr):
			while j<len(answr[0]):
				num = answr[i][j]
				if num != resultado[i][j]:	#checks if any value from the answer matrix doesn't match the correspondent one from the solution matrix 
					board.canvas.create_rectangle(2 + (50*(j)) ,2 + (50 * (i)),48+(50*(j)),48+(50*(i)), fill = 'white', width=0)
					board.canvas.create_text(25+(50*(j)),25+(50*(i)), text=num, fill='red', font=('Helvectica', '16'))	#if so it draws it in red and raise a flag to clasificate the message
					flag = 1
				else:
					if num != matrizini[i][j]:	#draws in green all the numbers that matches with the solution and arent initial values
						board.canvas.create_rectangle(2 + (50*(j)) ,2 + (50 * (i)),48+(50*(j)),48+(50*(i)), fill = 'white', width=0)
						board.canvas.create_text(25+(50*(j)),25+(50*(i)), text=num, fill='green', font=('Helvectica', '16'))
				j += 1
			i+=1
			j=0	
		if flag == 0:
			pancarta = 'GRATS! ITS CORRECT'
		else:
			pancarta = 'SORRY ITS WRONG'
		if pancarta == 'SORRY ITS WRONG':	#checks if the sudoku its correct but its a diferent solution,to do so it runs the check function 
			i = 0
			j = 0
			while i < len(answr):
				while j < len(answr[0]):
					if answr[i][j] != 0:
						textillo = 'valido'
						j +=1
					else:
						textillo = 'hay 0'
						break
				i+=1
				j=0
			if textillo == 'valido':
				pancarta = self.comprobante()
				if pancarta == 'CHECKED':
					pancarta = 'CORRECT'
				else:
					pancarta = 'SORRY ITS WRONG'			
		texto.insertotexto(pancarta)     
	#----------------------------------------------------------------------------------------------------------------------#
def load():
    direcs = str(raw_input('Introduce the sudokus starting file (default: sudoku1.txt): '))
    def tablero(direcs):
	#loads sudoku's default file
        if direcs == '':
            matrx = read('sudoku1.txt')	#default file
        else:
            matrx = read(direcs)
        return matrx   	
    matriz = tablero(direcs)  #matriz from read module.
    return matriz 
     
matrizini = load()

def solucion():    
    sol = str(raw_input('Introduce sudokus solution file (default: solsdk1.txt): '))    
    if sol == '':
        solu = 'solsdk1.txt'	#default solution file
    else:
        solu = sol   
    return solu   
    
sol = solucion()    #solution matrix

def basic(matriz):
    '''
    This function takes the initial matrix and draws it
    '''
    for i in range(10):
        for j in range(10):
            num = matriz[i-1][j-1]
            if num != 0:
                board.canvas.create_text(25+(50*(j-1)),25+(50*(i-1)), text=num, fill='blue', font=('Helvectica', '16'))	#draws the initial numbers in blue
            else:
                pass
                
basic(matrizini)	#calling basic function to draw the initial matrix
answr = []
for i in matrizini:			# A copy from the initial matrix to add the user's answers
	answr.append(i[:])


basic(matrizini)
frame = Sudoku(root)
root.mainloop()
