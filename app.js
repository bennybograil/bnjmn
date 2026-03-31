console.log("get the fuck out of my dev tools!!!")

async function run() {
  const res = await fetch("https://circulation-claims-appliance-assumed.trycloudflare.com")
  const data = await res.text()
  console.log(data)
}
run()
