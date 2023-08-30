const fs = require('fs');

function countStudents(path) {
	let content;

  try {
		  content = fs.readFileSync(path);
	 } catch (err) {
		  throw new Error('Cannot load the database');
  }
	content = content.toString().split('\n');

  let student = content.filter((item) => item);

  student = student.map((item) => item.split(','));

  const number= student.length ? student.length - 1 : 0;
  console.log(`Number of students: ${number}`);

  const field = {};
  for (const i in student) {
    if (i !== 0) {
    if (!field[student[i][3]]) field[student[i][3]] = [];

			field[student[i][3]].push(student[i][0]);
		}
	}

	delete field.field;

	for (const key of Object.keys(field)) {
		console.log(
			`Number of students in ${key}: ${field[key].length}. List: ${field[
				key
			].join(', ')}`,
		);
	}
}

module.exports = countStudents;
