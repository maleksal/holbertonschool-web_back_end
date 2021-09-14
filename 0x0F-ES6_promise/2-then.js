export default function handleResponseFromAPI(promise) {
  const respond = { status: 200, body: 'success' };
  return promise
    .then(
      () => respond,
    )
    .catch(
      (error) => error,
    )
    .finally(
      () => console.log('Got a response from the API'),
    );
}
