export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }

		students.map((item) => item.id);

  return students.map;
}
