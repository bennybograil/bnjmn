const apiBase =
  document.querySelector('meta[name="api-base-url"]')?.content?.trim() ||
  window.location.origin

async function loadApiRoot() {
  try {
    const res = await fetch(`${apiBase}/`)

    if (!res.ok) {
      throw new Error(`Request failed with status ${res.status}`)
    }

    const contentType = res.headers.get("content-type") || ""
    const data = contentType.includes("application/json")
      ? await res.json()
      : await res.text()

    console.log("API response:", data)
  } catch (error) {
    console.error(`Failed to fetch ${apiBase}/`, error)
  }
}

await loadApiRoot()
