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