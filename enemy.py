class Enemy(pygame.sprite.Sprite): 
    """Enemy class"""
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)        #Appel du constructeur de Sprite
        self.coordinates = (star_x, start_y)
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        

    def update(self):
        # Update