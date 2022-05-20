class Enemy(pygame.sprite.Sprite): 
    """Enemy class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        #Appel du constructeur de Sprite
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        

    def update(self):
        # Update