export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }

  const outcome = students.filter((item) => item.location === city);

  return outcome;
}
