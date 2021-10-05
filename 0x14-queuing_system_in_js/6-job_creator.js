import kue from "kue"

const jobData= {
    phoneNumber: "00000000",
    message: "Edward snowden!",
  }


const queue = kue.createQueue();
const Job = queue.create('push_notification_code', jobData);
Job.save();
Job.on('enqueue', (id, type) => {
  console.log(`Notification job created: ${Job.id}`)
});
Job.on('complete', (result) => {
  console.log('Notification job completed');
});
Job.on('failed', (err) => {
  console.log('Notification job failed');
});