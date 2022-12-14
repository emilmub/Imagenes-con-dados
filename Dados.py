import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def grey(Nom):
	'''
	Convierte una imagen RGB a una imagen en escala de grises. La intensidad de los pixeles
	está entre 0 y 255.
	
	Argumentos:
		Nom: Nombre del archivo que contiene la imagen

	Returns:
		Ndata: Matriz con el promedio de los valores RGB en cada pixel

	'''
	img = Image.open(Nom)
	data = np.asarray(img, dtype = 'int32')
	Ndata = np.zeros((data.shape[0],data.shape[1]))

	for i in range(len(data)):
		for j in range(len(data[0])):
			Ndata[i,j] = (data[i,j,0]+data[i,j,1]+data[i,j,2])/3

	return Ndata

def avgPixel(Imagen,region = 3):
	'''
	Promedia la intensidad de los pixeles en una region cuadrada

	Argumentos:
		Imagen: Arreglo con los valores de los pixeles de la imagen
		region: tamano de la region a promediar

	Returns:
		Im_avg: Arreglo con los valores promediados de la Imagen
	'''

	Im_avg = np.zeros((len(Imagen)//region,len(Imagen[0])//region)) # Crea la matriz que contendrá los promedios

	for px_ver in range(len(Im_avg)):
		for px_hor in range(len(Im_avg[0])):

			Im_avg[px_ver,px_hor] = np.average(Imagen[px_ver*region:region*(px_ver + 1), px_hor*region:region*(px_hor + 1)]) # Promedia la region de pixeles

	return Im_avg

def dice(Im_avg):
	'''
	Decide la cara del dado que le corresponde a cada pixel

	Argumentos:
		Im_avg: Arreglo con los valores promediados por regiones de la imagen

	Returns:
		Im_dice: Arreglo de dados que recrea la imagen original en escala de grises
		faces: Diccionario con la cantidad de cada cara en la imagen
	'''

	Im_dice = np.zeros((Im_avg.shape[0]*7,Im_avg.shape[1]*7)) # Crea la matriz que contendrá los dados
	maxval = Im_avg.max()
	faces = {}

	for px_ver in range(Im_avg.shape[0]):
		for px_hor in range(Im_avg.shape[1]):

			if Im_avg[px_ver,px_hor] <= maxval/6: # Cara 1
				faces[1] = faces.get(1,0) + 1 # Cuenta el numero de caras 1
				Im_dice[px_ver*7 + 3,px_hor*7 + 3] = 255	
			elif Im_avg[px_ver,px_hor] <= 2*maxval/6: # Cara 2
				faces[2] = faces.get(2,0) + 1 # Cuenta el numero de caras 2
				Im_dice[px_ver*7 + 5,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 1,px_hor*7 + 5] = 255
			elif Im_avg[px_ver,px_hor] <= 3*maxval/6: # Cara 3
				faces[3] = faces.get(3,0) + 1 # Cuenta el numero de caras 3
				Im_dice[px_ver*7 + 5,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 3,px_hor*7 + 3] = 255
				Im_dice[px_ver*7 + 1,px_hor*7 + 5] = 255
			elif Im_avg[px_ver,px_hor] <= 4*maxval/6: # Cara 4
				faces[4] = faces.get(4,0) + 1 # Cuenta el numero de caras 4
				Im_dice[px_ver*7 + 1,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 5,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 1,px_hor*7 + 5] = 255
				Im_dice[px_ver*7 + 5,px_hor*7 + 5] = 255
			elif Im_avg[px_ver,px_hor] <= 5*maxval/6: # Cara 5
				faces[5] = faces.get(5,0) + 1 # Cuenta el numero de caras 5
				Im_dice[px_ver*7 + 1,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 5,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 3,px_hor*7 + 3] = 255
				Im_dice[px_ver*7 + 1,px_hor*7 + 5] = 255
				Im_dice[px_ver*7 + 5,px_hor*7 + 5] = 255
			else: 									 # Cara 6
				faces[6] = faces.get(6,0) + 1 # Cuenta el numero de caras 6
				Im_dice[px_ver*7 + 1,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 3,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 5,px_hor*7 + 1] = 255
				Im_dice[px_ver*7 + 1,px_hor*7 + 5] = 255
				Im_dice[px_ver*7 + 3,px_hor*7 + 5] = 255
				Im_dice[px_ver*7 + 5,px_hor*7 + 5] = 255	

	return Im_dice, faces


if __name__ == '__main__':
	Nom = "patos.jpg" # Nombre del archivo

	Im_gris = grey(Nom)
	Im_avg = avgPixel(Im_gris, region = 30)
	print('Las dimensiones de la imagen en numero de dados son',Im_avg.shape,'alto x ancho')
	print('Para dados de 12mm, las dimensiones de la imagen son',Im_avg.shape[0]*12,'mm de alto por',Im_avg.shape[1]*12,'mm de ancho')
	print('Se necesitan',Im_avg.shape[0]*Im_avg.shape[1],'dados para recrear la imagen')
	print('Si en una hoja A4 caben 408 caras de 12 mm, entonces se necesitan imprimir',np.ceil(Im_avg.shape[0]*Im_avg.shape[1]/408),'hojas')
	Im_dice, faces = dice(Im_avg)
	print('El numero asociado a cada cara es',faces)
	
	Im = Image.fromarray(Im_dice) # Transforma la matriz a una imagen en escala de grises
	Im.show()