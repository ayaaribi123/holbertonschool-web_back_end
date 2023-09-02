export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const grade = newGrades.filter((newGrade) => newGrade.studentId === student.id);

    let	grades;

    if (grade[0]) {
      grades = grade[0].grades;
    } else {
      grades = 'N/A';
    }

    return {
      ...student, grades
					};
  });
}
