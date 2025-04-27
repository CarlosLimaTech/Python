import pygame

pygame.init()

pygame.mixer.music.load('Ex21_Audio.mp3')

pygame.mixer.music.play()

pygame.event.wait()