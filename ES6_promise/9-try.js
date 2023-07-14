export default function guardrail(mathFunction) {
  let queue = [];
  let resualt;

  try {
			resualt = mathFunction();
  } catch (err) {
			resualt = err.toString();
  }

  queue.push('Guardrail was processed', resualt);

  return queue;
}
