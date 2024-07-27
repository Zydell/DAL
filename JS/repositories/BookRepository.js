const { Book } = require('../models');

class BookRepository {
  async getAll() {
    return await Book.findAll();
  }

  async getById(id) {
    return await Book.findByPk(id);
  }

  async add(book) {
    return await Book.create(book);
  }

  async update(id, book) {
    await Book.update(book, {
      where: { id }
    });
  }

  async delete(id) {
    await Book.destroy({
      where: { id }
    });
  }
}

module.exports = BookRepository;
