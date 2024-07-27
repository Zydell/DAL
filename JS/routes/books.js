const express = require('express');
const router = express.Router();
const BookRepository = require('../repositories/BookRepository');

const bookRepo = new BookRepository();

router.get('/', async (req, res) => {
  const books = await bookRepo.getAll();
  res.json(books);
});

router.get('/:id', async (req, res) => {
  const book = await bookRepo.getById(req.params.id);
  if (book) {
    res.json(book);
  } else {
    res.status(404).send('Book not found');
  }
});

router.post('/', async (req, res) => {
  const newBook = await bookRepo.add(req.body);
  res.status(201).json(newBook);
});

router.put('/:id', async (req, res) => {
  await bookRepo.update(req.params.id, req.body);
  res.status(204).send();
});

router.delete('/:id', async (req, res) => {
  await bookRepo.delete(req.params.id);
  res.status(204).send();
});

module.exports = router;
