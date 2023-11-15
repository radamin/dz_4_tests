from abc import ABC, abstractmethod


class BookRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> dz_4_tests:
        pass

    @abstractmethod
    def find_all(self) -> list[dz_4_tests]:
        pass
