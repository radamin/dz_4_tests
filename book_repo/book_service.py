from dz_4_tests.book_repo.book import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository: BookRepository = book_repository

    def find_book_by_id(self, id: str) -> BookRepository:
        return self.book_repository.find_by_id(id)

    def find_all_books(self) -> list[BookRepository]:
        return self.book_repository.find_all()
