import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  let promise1 = null;
  let promise2 = null;

  const user = await signUpUser(firstName, lastName);
  promise1 = { status: 'fulfilled', value: user };

  try {
    promise2 = { status: 'rejected', value: await uploadPhoto(fileName) };
  } catch (error) {
    promise2 = { status: 'rejected', value: `${error.name}: ${error.message}` };
  }
  return [promise1, promise2];
}
