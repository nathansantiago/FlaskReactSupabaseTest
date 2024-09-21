import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api')
      .then((res) => res.json())
      .then(data => setData(data))
      .catch(console.error);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {data ? <p>{data.message}</p> : <p>Loading...</p>}
      </header>
    </div>
  )
}

export default App
