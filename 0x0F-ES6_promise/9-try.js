export default function guardrail(mathFunction) {
  const thisQueue = [];
  try {
    thisQueue.push(mathFunction());
  } catch (error) {
    thisQueue.push(`${error.name}: ${error.message}`);
  }
  thisQueue.push('Guardrail was processed');
  return thisQueue;
}
