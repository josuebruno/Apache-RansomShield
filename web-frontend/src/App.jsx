import { useEffect, useState } from 'react'

function App() {
  const [events, setEvents] = useState([])

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://172.18.250.28:5000/api/events")
        .then(res => res.json())
        .then(data => setEvents(data.reverse()))
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h1>🛡️ Apache RansomShield Dashboard</h1>
      <table border="1" cellPadding="10" cellSpacing="0" width="100%">
        <thead>
          <tr>
            <th>⏱️ Timestamp</th>
            <th>📂 Tipo</th>
            <th>📝 Detalhes</th>
            <th>🧠 Classificação</th>
          </tr>
        </thead>
        <tbody>
          {events.map((e, i) => (
            <tr key={i} style={{ backgroundColor: e.status === "threat" ? "#ffcfcf" : "#cfffcc" }}>
              <td>{new Date(e.timestamp * 1000).toLocaleString()}</td>
              <td>{e.type}</td>
              <td>{e.details}</td>
              <td>{e.status === "threat" ? "🚨 Ameaça" : "✅ Normal"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App
