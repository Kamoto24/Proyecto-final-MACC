import random
import cv2
##importa modulo random y cv2, que proviene de opencv
##El modulo cv2 lo utilizamos para hacer aparecer una ventana emergente que tendra de imagen, la imagen dada. Al presionar cualquier tecla dicha ventana se cerrará.
def si_jugador_gana(player, opponent):
    if (player == 'piedra' and opponent == 'tijera') or (player == 'tijera' and opponent == 'papel') or (
            player == 'papel' and opponent == 'piedra'):
        return True
    elif (player == opponent):
        return "EMPATE"
    else:
        return False
def jugar(jugador):
    ordenador = random.choice(['piedra', 'papel', 'tijera'])

    if (jugador=="piedra"):
        piedra=cv2.imread("piedra.png",1)
        cv2.imshow("PIEDRA",piedra)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    elif (jugador=="papel"):
        piedra=cv2.imread("papel.png",1)
        cv2.imshow("PAPEL",piedra)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    elif (jugador=="tijera"):
        piedra=cv2.imread("tijera.png",1)
        cv2.imshow("TIJERA",piedra)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    if si_jugador_gana(jugador, ordenador)==True:
        piedra=cv2.imread("ganaste.png",1)
        cv2.imshow("GANASTE",piedra)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
        return '¡Has ganado!'
    elif si_jugador_gana(jugador, ordenador) == False:
        piedra=cv2.imread("perdiste.png",1)
        cv2.imshow("PERDISTE",piedra)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
        return 'Has perdido...'
    elif si_jugador_gana(jugador, ordenador) == "EMPATE":
        piedra=cv2.imread("empate.png",1)
        cv2.imshow("EMPATE",piedra)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
        return 'Empataste'

