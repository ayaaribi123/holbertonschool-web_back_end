import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((result) => {
      const { body } = result[0];
      const { firstName } = result[1];
      const { lastName } = result[2];
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
