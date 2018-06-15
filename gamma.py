import numpy as np
import cv2
import argparse

def ajusteGamma(image, gamma=0.5):
	invGamma = 1.0/gamma
	table = np.array([((i/255.0)**invGamma)*255
		for i in np.arange(0,256)]).astype("uint8")

	return cv2.LUT(image,table)

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="")
args = vars(ap.parse_args())

original = cv2.imread(args["image"])

for gamma in np.arange(0.0,3.5,0.5):
	if gamma == 1:
		continue
	gamma = gamma if gamma > 0 else 0.1
	adjusted = ajusteGamma(original, gamma=gamma)
	cv2.imshow("images", np.hstack([original, adjusted]))
cv2.waitKey(0)