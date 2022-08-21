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

	'''

	Im_avg = np.zeros((len(Imagen)//region,len(Imagen[0])//region)) # Crea la matriz que contiene los promedios

	for px_ver in range(len(Im_avg)):
		for px_hor in range(len(Im_avg[0])):

			Im_avg[px_ver,px_hor] = np.average(Imagen[px_ver*region:region*(px_ver + 1), px_hor*region:region*(px_hor + 1)])

	return Im_avg


if __name__ == '__main__':
	Nom = "patos.jpg"

	Im_gris = grey(Nom)
	Im_avg = avgPixel(Im_gris, region = 20)

	print(Im_avg.shape)
	Im = Image.fromarray(Im_avg)
	Im.show()