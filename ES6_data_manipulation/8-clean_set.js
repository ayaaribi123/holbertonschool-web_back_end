export default function cleanSet(set, startString) {
  if (
    typeof set !== 'object' || typeof startString !== 'string' || startString.length === 0
  ) {
    return '';
  }
  const arr = [];
  for (const item of set) {
    if (item && item.startsWith(startString)) {
      arr.push(item.slice(startString.length));
    }
  }
  return arr.join('-');
}
