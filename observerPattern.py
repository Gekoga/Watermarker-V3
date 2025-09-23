# https://refactoring.guru/design-patterns/observer/python/example#
from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    # Interface for declaring a set of methods for managing subscribers

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        # Attach an Observer to the subject
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        # Detach an Observer to the subject
        pass

    @abstractmethod
    def notify(self) -> None:
        # Notify all Observers
        pass


class Observer(ABC):
    # Interface for declaring the update method, used by subjects

    @abstractmethod
    def update(self, subject: Subject) -> None:
        # Receive update from subjects
        pass
