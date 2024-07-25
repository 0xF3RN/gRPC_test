import React, { useState } from 'react';
import './App.css';


function App() {
    const [data, setData] = useState([]);

    const fetchData = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/v1/get_data');
            const result = await response.json();
            setData(result);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="container">
            <button onClick={fetchData}>А что интересного расскажешь?</button>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Text</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map(item => (
                        <tr key={item.id}>
                            <td>{item.id}</td>
                            <td>{item.text}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;
