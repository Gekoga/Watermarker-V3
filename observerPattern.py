# https://refactoring.guru/design-patterns/observer/python/example#
from __future__ import annotations
from abc import ABC, abstractmethod

# TODO: Clear duplicate code within the different subjects
class Subject(ABC):
    # Interface for declaring a set of methods for managing subscribers
    _observers: list[Observer]

    def __init__(self) -> None:
        self._observers = []

    # Attach an Observer to the subject
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    # Detach an Observer to the subject
    def detach(self, observer: Observer) -> None:
        try:
            self._observers.remove(observer)
        except ValueError:
            print("Subject: Observer not found")

    # Notify all Observers
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
    
    def notifySingleObserver(self, observer: Observer) -> None:
        observer.update(self)


class Observer(ABC):
    # Interface for declaring the update method, used by subjects

    @abstractmethod
    def update(self, subject: Subject) -> None:
        # Receive update from subjects
        pass
