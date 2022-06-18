import numpy as np
import cv2
import os


def merge_channels(input_dir, output_dir):
  images = sorted([i for i in os.walk(input_dir)][0][2])

  for i in range(0, len(images), 3):
    r = cv2.imread(input_dir + images[i + 2])
    g = cv2.imread(input_dir + images[i + 1])
    b = cv2.imread(input_dir + images[i])

    r = cv2.split(r)[0]
    g = cv2.split(g)[0]
    b = cv2.split(b)[0]
    result_image = cv2.merge((b, g, r))
    print("OK")

    cv2.imwrite(output_dir + images[i][:-6] + ".jpg", result_image)


merge_channels("dataset/data/", "dataset/true_data/")