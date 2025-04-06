import pygame

class EventQueue:
    """class responsible for the event queue
    """
    def get(self):
        """gets and returns the events
        """
        return pygame.event.get()