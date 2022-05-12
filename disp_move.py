import skimage
import cv2 
import numpy as np 

def disp_move(index_list, pola, start_position, start_color, move):

    if start_position[fun.pola[index_list[0]]]!="None" and start_position[fun.pola[index_list[1]]]!="None" and move%2 == 1 and start_color[fun.pola[index_list[0]]] == 1: #ruch bia³ych
        print(start_position[fun.pola[index_list[0]]]," ", fun.pola[index_list[0]], " x ", fun.pola[index_list[1]])
        start_position[fun.pola[index_list[1]]] = start_position[fun.pola[index_list[0]]]
        start_position[fun.pola[index_list[0]]] = "None"
        start_color[fun.pola[index_list[1]]] = start_color[fun.pola[index_list[0]]]
        start_color[fun.pola[index_list[0]]] = 2
        sfmove = str(fun.pola[index_list[0]])+str(fun.pola[index_list[1]])
                    
    elif start_position[fun.pola[index_list[0]]]!="None" and start_position[fun.pola[index_list[1]]]!="None" and move%2 == 1 and start_color[fun.pola[index_list[1]]] == 1: #ruch bia³ych
        print(start_position[fun.pola[index_list[0]]]," ", fun.pola[index_list[1]], " x ", fun.pola[index_list[0]])
        start_position[fun.pola[index_list[0]]] = start_position[fun.pola[index_list[1]]]
        start_position[fun.pola[index_list[1]]] = "None"  
        start_color[fun.pola[index_list[0]]] = start_color[fun.pola[index_list[1]]]
        start_color[fun.pola[index_list[1]]] = 2
        sfmove = str(fun.pola[index_list[1]])+str(fun.pola[index_list[0]])
                
    elif start_position[fun.pola[index_list[0]]]!="None" and start_position[fun.pola[index_list[1]]]!="None" and move%2 == 0 and start_color[fun.pola[index_list[0]]] == 0: #ruch czarnych
        print(start_position[fun.pola[index_list[0]]]," ", fun.pola[index_list[0]], " x ", fun.pola[index_list[1]])
        start_position[fun.pola[index_list[0]]] = start_position[fun.pola[index_list[0]]]
        start_position[fun.pola[index_list[1]]] = "None"
        start_color[fun.pola[index_list[0]]] = start_color[fun.pola[index_list[0]]]
        start_color[fun.pola[index_list[1]]] = 2
        sfmove = str(fun.pola[index_list[0]])+str(fun.pola[index_list[1]])
                    
    elif start_position[fun.pola[index_list[0]]]!="None" and start_position[fun.pola[index_list[1]]]!="None" and move%2 == 0 and start_color[fun.pola[index_list[1]]] == 0: #ruch czarnych
        print(start_position[fun.pola[index_list[1]]]," ", fun.pola[index_list[1]], " x ", fun.pola[index_list[0]])
        start_position[fun.pola[index_list[0]]] = start_position[fun.pola[index_list[1]]]
        start_position[fun.pola[index_list[1]]] = "None"  
        start_color[fun.pola[index_list[0]]] = start_color[fun.pola[index_list[1]]]
        start_color[fun.pola[index_list[1]]] = 2
        sfmove = str(fun.pola[index_list[1]])+str(fun.pola[index_list[0]])
                    
    elif start_position[fun.pola[index_list[0]]]!="None":
        print(start_position[fun.pola[index_list[0]]]," ", fun.pola[index_list[0]], " - ", fun.pola[index_list[1]])
        start_position[fun.pola[index_list[1]]] = start_position[fun.pola[index_list[0]]]
        start_position[fun.pola[index_list[0]]] = "None"
        start_color[fun.pola[index_list[1]]] = start_color[fun.pola[index_list[0]]]
        start_color[fun.pola[index_list[0]]] = 2
        sfmove = str(fun.pola[index_list[0]])+str(fun.pola[index_list[1]])
                    
    else:
        print(start_position[fun.pola[index_list[1]]]," ", fun.pola[index_list[1]], " - ", fun.pola[index_list[0]])
        start_position[fun.pola[index_list[0]]] = start_position[fun.pola[index_list[1]]]
        start_position[fun.pola[index_list[1]]] = "None"  
        start_color[fun.pola[index_list[0]]] = start_color[fun.pola[index_list[1]]]
        start_color[fun.pola[index_list[1]]] = 2
        sfmove = str(fun.pola[index_list[1]])+str(fun.pola[index_list[0]])

    return start_color, start_position, sfmove