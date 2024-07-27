const { Author } = require('../models');

class AuthorRepository {
  async getAll() {
    return await Author.findAll();
  }

  async getById(id) {
    return await Author.findByPk(id);
  }

  async add(author) {
    return await Author.create(author);
  }

  async update(id, author) {
    await Author.update(author, {
      where: { id }
    });
  }

  async delete(id) {
    await Author.destroy({
      where: { id }
    });
  }
}

module.exports = AuthorRepository;
