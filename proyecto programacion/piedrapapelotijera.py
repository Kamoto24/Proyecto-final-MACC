import random
import cv2
import numpy as np

def jugar():
    
    def si_jugador_gana(player, opponent):
        if (player == 'piedra' and opponent == 'tijera') or (player == 'tijera' and opponent == 'papel') or (player == 'papel' and opponent == 'piedra'):
            return True
        return 'You lost!'
   
        
        jugador = input("Con que elemento deseas jugar? \n recuerda que las opciones que puedes escoger son: 'piedra'. 'papel' o 'tijera'\n Tu opcion es: ")
        ordenador = random.choice(['piedra', 'papel', 'tijera'])
        
        if (jugador=="piedra"):
            piedra=cv2.imread("piedra.png",1)
            cv2.imshow("PIEDRA",piedra)
            cv2.waitkey(0)
            cv2.destroyAllWindows()
        if (jugador=="papel"):
            piedra=cv2.imread("papel.png",1)
            cv2.imshow("PAPEL",piedra)
            cv2.waitkey(0)
            cv2.destroyAllWindows()
        if (jugador=="tijera"):
            piedra=cv2.imread("tijera.png",1)
            cv2.imshow("TIJERA",piedra)
            cv2.waitkey(0)
            cv2.destroyAllWindows()
            
        if si_jugador_gana(jugador, ordenador):
            
            piedra=cv2.imread("ganaste.png",1)
            cv2.imshow("GANASTE",piedra)
            cv2.waitkey(0)
            cv2.destroyAllWindows() 
            return 'GANASTEE!'
        
        piedra=cv2.imread("perdiste.png",1)
        cv2.imshow("PERDISTE",piedra)
        cv2.waitkey(0)
        cv2.destroyAllWindows()
    
        return 'PERDISTEE!'
    
        if jugador == ordenador:
            piedra=cv2.imread("empate.png",1)
            cv2.imshow("EMPATE",piedra)
            cv2.waitkey(0)
            cv2.destroyAllWindows()
            return 'EMPATEE'

    
    



print(jugar())
