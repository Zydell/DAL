'use strict';
module.exports = (sequelize, DataTypes) => {
  const Author = sequelize.define('Author', {
    firstName: DataTypes.STRING,
    lastName: DataTypes.STRING
  }, {});
  Author.associate = function(models) {
    Author.hasMany(models.Book, { foreignKey: 'authorId' });
  };
  return Author;
};
