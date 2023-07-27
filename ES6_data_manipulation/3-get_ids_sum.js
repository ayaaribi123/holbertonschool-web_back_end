export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const reducer = (student, idd) => student + idd.id;

  const sum = students.reduce(reducer, 0);

  return sum;
}
