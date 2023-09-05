import kue from 'kue';

const queue = kue.createQueue();

const Data = {
	phoneNumber: '2001111207',
	message: 'here is your code'
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  send(phoneNumber, message);
  done('Notification job completed');
});
