export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (!success) {
      reject(Error('The fake API is not working currently'));
    } else {
      resolve({ status: 200, body: 'Success' });
    }
  });
}
