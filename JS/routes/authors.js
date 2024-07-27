const express = require('express');
const router = express.Router();
const AuthorRepository = require('../repositories/AuthorRepository');

const authorRepo = new AuthorRepository();

router.get('/', async (req, res) => {
  const authors = await authorRepo.getAll();
  res.json(authors);
});

router.get('/:id', async (req, res) => {
  const author = await authorRepo.getById(req.params.id);
  if (author) {
    res.json(author);
  } else {
    res.status(404).send('Author not found');
  }
});

router.post('/', async (req, res) => {
  const newAuthor = await authorRepo.add(req.body);
  res.status(201).json(newAuthor);
});

router.put('/:id', async (req, res) => {
  await authorRepo.update(req.params.id, req.body);
  res.status(204).send();
});

router.delete('/:id', async (req, res) => {
  await authorRepo.delete(req.params.id);
  res.status(201).send('Autor eliminado correctamente');
});

module.exports = router;
