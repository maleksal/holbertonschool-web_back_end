import kue from "kue"
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', 1, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
});