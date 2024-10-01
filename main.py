import pygame

screen = pygame.display.set_mode((640, 480))
run = True


class Table:
    def __init__(self, max_players, current_players, color):
        self.max_players = max_players
        self.current_players = current_players
        self.color = color

    def render(self):
        pass

class Player:
    def __init__(self, bank, money_in_pot, hand, has_folded, table_position):
        self.bank = bank
        self.money_in_pot = money_in_pot
        self.hand = hand
        self.has_folded = has_folded
        self.table_position = table_position

    def render(self):
        pass

    

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(screen, (0,0,53), (0, 0, 640, 480))

    pygame.display.update()
pygame.quit()