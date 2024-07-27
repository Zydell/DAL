'use strict';
module.exports = (sequelize, DataTypes) => {
  const Book = sequelize.define('Book', {
    title: DataTypes.STRING,
    authorId: DataTypes.INTEGER
  }, {});
  Book.associate = function(models) {
    Book.belongsTo(models.Author, { foreignKey: 'authorId' });
  };
  return Book;
};
