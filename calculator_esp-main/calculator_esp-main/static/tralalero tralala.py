import time
import os

shark = r"""
               __         
              /  \~~~/  \  
        ,----(     . . )   
       /      \__     @ )  
     /|         (    \/    
    ^ \   /___\  /\|        
       |__|   |__|           
"""
# Función para animar el tiburón nadando
def shark_swim():
    for i in range(10):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
        print(" " * i + shark)
        print(" " * i + "El tiburón se acerca... 🦈 tralalero tralala!")
        time.sleep(0.9)

shark_swim()