import base64
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
from scipy import ndimage

def b64_str_to_np(base64_str):
    base64_str = str(base64_str)
    if "base64" in base64_str:
        _, base64_str = base64_str.split(',')

    buf = BytesIO()
    buf.write(base64.b64decode(base64_str))
    buf.seek(0)
    pimg = Image.open(buf)
    img = np.array(pimg)

    # Keep only 4th value in 3rd dimension (first 3 are all zeros)
    return img[:, :, 3]


def crop_img(img_ndarray,v2):
    first_row = np.nonzero(img_ndarray)[0].min()
    last_row = np.nonzero(img_ndarray)[0].max()
    middle_row = np.mean([last_row, first_row])
    first_col = np.nonzero(img_ndarray)[1].min()
    last_col = np.nonzero(img_ndarray)[1].max()
    middle_col = np.mean([last_col, first_col])

    row_length = last_row - first_row
    col_length = last_col - first_col
    length = max(row_length, col_length)
    if v2 == 1:
        length = max(length, 28)
    else:
        length = max(length, 32)
        

    # Get half length to add to middle point (add some padding: 1px)
    half_length = (length / 2) + 1

    # Make sure even the shorter dimension is centered
    first_row = int(middle_row - half_length)
    last_row = int(middle_row + half_length)
    first_col = int(middle_col - half_length)
    last_col = int(middle_col + half_length)

    # Crop image
    return img_ndarray[first_row:last_row, first_col:last_col]


def center_img(img_ndarray):
    com = ndimage.measurements.center_of_mass(img_ndarray)
    center = len(img_ndarray) / 2

    row_diff = int(com[0] - center)
    col_diff = int(com[1] - center)

    rows = np.zeros((abs(row_diff), img_ndarray.shape[1]))
    if row_diff > 0:
        img_ndarray = np.vstack((img_ndarray, rows))
    elif row_diff < 0:
        img_ndarray = np.vstack((rows, img_ndarray))

    cols = np.zeros((img_ndarray.shape[0], abs(col_diff)))
    if col_diff > 0:
        img_ndarray = np.hstack((img_ndarray, cols))
    elif col_diff < 0:
        img_ndarray = np.hstack((cols, img_ndarray))

    # Make image square again (add zero rows to the smaller dimension)
    dim_diff = img_ndarray.shape[0] - img_ndarray.shape[1]
    half_A = half_B = abs(int(dim_diff / 2))
    
    if dim_diff % 2 != 0:
        half_B += 1

    # Add half to each side (to keep center of mass)
    # Handle dim_diff == 1
    if half_A == 0:  # 1 line off from exactly centered
        if dim_diff > 0:
            half_B = np.zeros((img_ndarray.shape[0], half_B))
            img_ndarray = np.hstack((half_B, img_ndarray))
        else:
            half_B = np.zeros((half_B, img_ndarray.shape[1]))
            img_ndarray = np.vstack((half_B, img_ndarray))

    elif dim_diff > 0:
        half_A = np.zeros((img_ndarray.shape[0], half_A))
        half_B = np.zeros((img_ndarray.shape[0], half_B))
        img_ndarray = np.hstack((img_ndarray, half_A))
        img_ndarray = np.hstack((half_B, img_ndarray))
    else:
        half_A = np.zeros((half_A, img_ndarray.shape[1]))
        half_B = np.zeros((half_B, img_ndarray.shape[1]))
        img_ndarray = np.vstack((img_ndarray, half_A))
        img_ndarray = np.vstack((half_B, img_ndarray))
    # Add padding all around (15px of zeros)
    return np.lib.pad(img_ndarray, 15, 'constant', constant_values=(0))

def resize_img(img_ndarray,v2):
    img = Image.fromarray(img_ndarray)
    if v2 == 1:
        img.thumbnail((28, 28), Image.ANTIALIAS)
    else:
        img.thumbnail((32, 32), Image.ANTIALIAS)

    return np.array(img)

def reshape_array(img_ndarray,v2):
    if v2 == 1:
        digit = np.reshape(img_ndarray, (1, 28, 28, 1), order='C')
    else:
        digit = np.reshape(img_ndarray, (1, 32, 32, 1), order='C')
    return digit
