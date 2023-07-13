import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((result) => {
      const { body } = result;
      const { firstName } = result;
      const { lastName } = result;
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch((error) => console.log('Signup system offline', error));
}
