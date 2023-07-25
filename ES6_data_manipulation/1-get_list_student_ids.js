export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const idd = students.map((item) => item.id);

  return idd;
}
