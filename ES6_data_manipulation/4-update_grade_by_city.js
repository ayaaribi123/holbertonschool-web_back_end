export default function updateStudentGradeByCity(students, city, newGrades) {
	if (!Array.isArray(students)) {
		return [];
}
if (!Array.isArray(newGrades)) {
		return [];
}

  return students.filter((student) => student.location === city).map((student) => {
    const grade = newGrades.filter((newGrade) => newGrade.studentId === student.id);

    let grades;

    if (grade[0]) {
      grades = grade[0].grades;
    } else {
      grades = 'N/A';
    }

    return {
      ...student, grades,
    };
  });
}
