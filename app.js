console.log("get the fuck out of my dev tools!!!")

async function run() {
  const res = await fetch("https://your-url")
  const data = await res.text()
  console.log(data)
}
run()
