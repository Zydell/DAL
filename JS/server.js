const express = require('express');
const bodyParser = require('body-parser');

const authorRoutes = require('./routes/authors');
const bookRoutes = require('./routes/books');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

app.use('/authors', authorRoutes);
app.use('/books', bookRoutes);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});


