import pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.time.wait(15000)  
pygame.mixer.music.stop()
