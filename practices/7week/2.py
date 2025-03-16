import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800 , 600))
running = True

clock = pygame.time.Clock()
FPS = 60
songs = ["Playboi Carti - BACKD00R.mp3",
         "Playboi Carti - I SEEEEEE YOU BABY BOI.mp3",
         "Playboi Carti - RATHER LIE.mp3"]
current_song = 0

pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()

music_playing = True

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if music_playing:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
            elif event.key == pygame.K_RIGHT:
                current_song += 1
                if current_song >= len(songs):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song -= 1
                if current_song < 0:
                    current_song = len(songs) - 1
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()



    pygame.display.flip()
    clock.tick(FPS)