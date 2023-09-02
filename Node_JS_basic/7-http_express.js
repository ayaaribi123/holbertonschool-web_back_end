const express = require('express');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const students = await countStudents(args[0]);
    res.send(`${'This is the list of our students\n'}${students.join('\n')}`);
  } catch (error) {
    res.send(`${'This is the list of our students\n'}${error.message}`);
  }
});

module.exports = app;
