pola = []
for val in range(1, 9):
    pola.extend(["h"+str(val), "g"+str(val), "f"+str(val), "e"+str(val), "d"+str(val),"c"+str(val), "b"+str(val), "a"+str(val)])
    

start_position = { "a1":"Rook", "b1":"Knight", "c1":"Bishop", "d1":"Queen", "e1":"King", "f1":"Bishop", "g1":"Knight", "h1":"Rook",
                   "a2":"Pawn", "b2":"Pawn", "c2":"Pawn", "d2":"Pawn", "e2":"Pawn", "f2":"Pawn", "g2":"Pawn", "h2":"Pawn",
                   "a3":"None", "b3":"None", "c3":"None", "d3":"None", "e3":"None", "f3":"None", "g3":"None", "h3":"None",
                   "a4":"None", "b4":"None", "c4":"None", "d4":"None", "e4":"None", "f4":"None", "g4":"None", "h4":"None",
                   "a5":"None", "b5":"None", "c5":"None", "d5":"None", "e5":"None", "f5":"None", "g5":"None", "h5":"None",
                   "a6":"None", "b6":"None", "c6":"None", "d6":"None", "e6":"None", "f6":"None", "g6":"None", "h6":"None",
                   "a7":"Pawn", "b7":"Pawn", "c7":"Pawn", "d7":"Pawn", "e7":"Pawn", "f7":"Pawn", "g7":"Pawn", "h7":"Pawn",
                   "a8":"Rook", "b8":"Knight", "c8":"Bishop", "d8":"Queen", "e8":"King", "f8":"Bishop", "g8":"Knight", "h8":"Rook"
                   }
                   
start_color = { "a1":1, "b1":1, "c1":1, "d1":1, "e1":1, "f1":1, "g1":1, "h1":1,
                   "a2":1, "b2":1, "c2":1, "d2":1, "e2":1, "f2":1, "g2":1, "h2":1,
                   "a3":2, "b3":2, "c3":2, "d3":2, "e3":2, "f3":2, "g3":2, "h3":2,
                   "a4":2, "b4":2, "c4":2, "d4":2, "e4":2, "f4":2, "g4":2, "h4":2,
                   "a5":2, "b5":2, "c5":2, "d5":2, "e5":2, "f5":2, "g5":2, "h5":2,
                   "a6":2, "b6":2, "c6":2, "d6":2, "e6":2, "f6":2, "g6":2, "h6":2,
                   "a7":0, "b7":0, "c7":0, "d7":0, "e7":0, "f7":0, "g7":0, "h7":0,
                   "a8":0, "b8":0, "c8":0, "d8":0, "e8":0, "f8":0, "g8":0, "h8":0
                   }