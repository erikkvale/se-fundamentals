from abc import ABC, abstractmethod
from typing import List
from random import randrange



class Subject(ABC):
    """The abstract Subject

    Args:
        ABC ([type]): [description]
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject

        Args:
            observer (Observer): [description]
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject

        Args:
            observer (Observer): [description]
        """
        pass

    
    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about an event
        """
        pass



class ConcreteSubject(Subject):
    """The Subject own some important state and notified observers when the state
    changes.

    Args:
        Subject ([type]): [description]
    """
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        self._state = randrange(0, 10)
        self.notify()


class Observer(ABC):
    """The observer interface declsares the update method, use by subjects

    Args:
        ABC ([type]): [description]
    """
    pass


# ===========================================
# Concrete Observers
# ===========================================

class ConcreteObserverA(Observer):
    pass


class ConcreteObserverB(Observer):
    pass



if __name__ == "__main__":
    subject = ConcreteSubject()
    
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)
    subject.some_business_logic()



