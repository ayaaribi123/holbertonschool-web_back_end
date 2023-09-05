import kue from 'kue';

const queue = kue.createQueue();

const Data = {
	phoneNumber: '9165219225',
	message: 'here is your code'
}

function send(Data) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`,
  );
}


queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  send(phoneNumber, message);
  done('Notification job completed');
});
