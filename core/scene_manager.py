"""
This module contains the SceneManager class.
"""

from core.input_manager import InputManager
from core.scene import Scene

class SceneManager:
    """
    Manages the scenes in the game and handles transitions.

    Attributes:
        current_scene (Scene): The active scene.
        running (bool): Flag to indicate if the game is running.
    """

    def __init__(self):
        self.current_scene = None
        self.running = True

    def set_initial_scene(self, scene: Scene):
        """Set the initial scene for the game."""
        self.current_scene = scene

    def update(self, input_manager: InputManager):
        """
        Updates the current scene and checks for transitions.

        Args:
            input_manager (InputManager): The input manager to query input states.
        """
        if self.current_scene:
            self.current_scene.update(input_manager)
            if not self.current_scene.running:  # Check if the current scene should stop
                self.running = False

    def render(self):
        """Renders the current scene."""
        if self.current_scene:
            self.current_scene.render()

    def transition_to(self, new_scene: Scene):
        """Transition to a new scene."""
        self.current_scene = new_scene
