from abc import ABC, abstractmethod
from typing import ClassVar

class MainView(ABC):
    """ABC for all main page views, bringing common functionality across them."""

    state: ClassVar[str]

    @abstractmethod
    def load_custom_js(self) -> str:
        """Javascript to be embedded into gradio interface."""
        raise NotImplementedError

    @abstractmethod
    def build_layout(self) -> None:
        raise NotImplementedError