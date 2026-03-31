console.log("get the fuck out of my dev tools you thief!!!")

const res = await fetch("http://127.0.0.1:8000/")
const data = await res.text()
console.log(data)
