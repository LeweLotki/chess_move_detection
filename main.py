from skimage.metrics import structural_similarity
import os
import skimage
import cv2 
import numpy as np 
import time
from disp_move import disp_move
from image_division import subdivided, cord_division
from chess_var import pola, start_position, start_color
from stockfish import Stockfish

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if (cap.isOpened() == False):  
    print("Error opening video  file")
ret, frame = cap.read()  

dirname = os.path.dirname(__file__)
stockfish_path = 'stockfish\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe'
stockfish_abs_path = os.path.join(dirname, stockfish_path)

stockfish = Stockfish(stockfish_abs_path)
chessboard_exist = False
move = 0
sfposition = [] #lista ruchow dla stockfisha
sfmove = ''

def circularity_coef(A, R): return 4*np.pi*A / R**2

while(cap.isOpened()): 

    ret, frame = cap.read()
    if ret == True: 
        if cv2.waitKey(25) & 0xFF == ord('q'):  break
        if cv2.waitKey(25) & 0xFF == ord('s'): 
            ## Segmentation
            logical_mask = frame[:, :, 0] > 150
            logical_mask = skimage.img_as_ubyte(logical_mask)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10, 10))
            logical_mask = cv2.morphologyEx(logical_mask,cv2.MORPH_CLOSE,kernel)
            logical_mask = logical_mask > 0

            ## Getting labels
            labels = skimage.measure.label(logical_mask, connectivity=2)
            features = skimage.measure.regionprops(labels)

            ## Subdividing chessboard
            if len(features) == 2:
                chessboard_exist = True
                frame_cropped = frame[int(np.minimum(features[0].centroid[0], features[1].centroid[0])):int(np.maximum(features[0].centroid[0], features[1].centroid[0])),
                                      int(np.minimum(features[0].centroid[1], features[1].centroid[1])):int(np.maximum(features[0].centroid[1], features[1].centroid[1])), :]

                squares_list, squares_cord_list = subdivided(frame_cropped)

        cv2.imshow('Frame', frame)

        if chessboard_exist: 
            time.sleep(1e-2)
            old_frame_cropped = frame_cropped.copy()
            old_squares_list = squares_list.copy()

            frame_temp = frame_cropped.copy()
            squares_list_temp = squares_list.copy()

            frame_cropped = frame[int(np.minimum(features[0].centroid[0], features[1].centroid[0])):int(np.maximum(features[0].centroid[0], features[1].centroid[0])),
                                    int(np.minimum(features[0].centroid[1], features[1].centroid[1])):int(np.maximum(features[0].centroid[1], features[1].centroid[1])), :]

            squares_list = cord_division(frame_cropped, squares_cord_list)
        
            index_list = []
            for index, square in enumerate(squares_list):

                ## Filtering images
                new_square = cv2.bilateralFilter(cv2.cvtColor(squares_list[index], 
                               cv2.COLOR_BGR2GRAY), 9, 75, 75)
                old_square = cv2.bilateralFilter(cv2.cvtColor(old_squares_list[index], 
                               cv2.COLOR_BGR2GRAY), 9, 75, 75)
                
                ## Checking similarity
                (ssim, diff) = structural_similarity(new_square, old_square, full=True)
                               
                ssim = round(100*(ssim), 3)

                ## Similarity smaller than 90 percent
                if ssim < 90:   

                    ## Getting shape of diff
                    diff = skimage.img_as_ubyte(diff)
                    logical_mask_diff = diff < 50

                    labels_diff = skimage.measure.label(logical_mask_diff, connectivity=2)
                    features_diff = skimage.measure.regionprops(labels_diff)

                    i = 0
                    temp_index = 0
                    temp_shape = 0
                    for shape in features_diff:
                        if shape.area_filled > temp_shape:
                            temp_shape = shape.area_filled
                            temp_index = i
                        i += 1

                    if circularity_coef(features_diff[temp_index].area_filled, features_diff[temp_index].perimeter):
                        
                        index_list.append(index)

                if len(index_list) == 2:

                    move += 1
                    if move%2 == 1: print("move: ", int(((move - 1)/2) + 1))

                    ## Displaying move
                    start_color, start_position, sfmove = disp_move(index_list, pola, start_position, start_color, move)

                    ## Evaluating position
                    sfposition.append(sfmove)
                    stockfish.set_position(sfposition)
                    print("Best move: ", stockfish.get_best_move_time(500))
                    print("Evaluation: ", (stockfish.get_evaluation()["value"])/100)

                else:
                    frame_cropped = frame_temp.copy()
                    index_list.clear()
                    squares_list.clear()
                    squares_list = squares_list_temp.copy()
    else:   break

cap.release() 

cv2.destroyAllWindows() 
                        








                
                
