import React, {useState, useEffect} from 'react'
import './App.css';

function App() {

  const [state, setState] = useState([])

  useEffect(() => {
     // fetch("/members").then(res => res.json()).then(data => setState(data))
     fetch("/api/school/all").then(res => res.json()).then(data => setState({"data":data.schools}))
  },[]);
  return (
    <div className="App">
      <h2>Flask - React Test Application</h2>
      { !state.data ? (<p>Loading...</p>):(
          state.data?.map((d, i)=> (
            <p key={`${i}-m`}>{d.name}</p>
          ))
        )}
    </div>
  );
}

export default App;
