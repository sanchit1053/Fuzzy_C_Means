from matplotlib import pyplot as plt
import numpy as np
import scipy.signal as sig
import cv2


img = np.array([range(0,4), range(4, 8), range(8, 12), range(12, 16)])
print(np.sum(img,axis=0))