import {createClient, print} from "redis";
const client = createClient();

client.on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.toString()}`);
  });
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

const vals = [
    ("Portland", 50),
    ("Seattle", 80),
    ("New York", 20),
    ("Bogota", 20),
    ("Cali", 40),
    ("Paris", 2)
]

const hash = "HolbertonSchools"

for (const t of vals) {
    client.hset(hash, t[0], t[1], print);

}
client.hgetAll(hash, function(err, response) {
  console.log(response)
});