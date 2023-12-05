import { useState } from 'react'
import './App.css'


const url = "https://sentimentanalysispython-547kwfnkdq-ue.a.run.app";

function App() {
  const [text, setText] = useState('');
  const [model, setModel] = useState('distilbert-multilingual-sentiments');
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);

  const handleSubmit = () => {
    if (!text || !model) return;

    setLoading(true);
    setData(null);

    let path = '';

    if (model === "distilbert-multilingual-sentiments") {
      path = '/analysis';
    } else if (model === "gpt-4") {
      path = '/analysis_v2';
    }

    fetch(`${url}${path}?text=${text}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(res => res.json())
      .then(data => {
        setData(data);
      }).catch(err => {
        console.log(err);
      }).finally(() => {
        setLoading(false);
      })
  }

  return (
    <div className="App">
      <div className="container">
        <h3>Get complete sentiment analysis of your text</h3>
        <h4>Choose a model</h4>
        <select value={model} onChange={(e) => setModel(e.target.value)}>
          <option value="distilbert-multilingual-sentiments">distilbert-multilingual-sentiments</option>
          <option value="gpt-4">gpt-4</option>
        </select>
        <textarea value={text} onChange={(e) => setText(e.target.value)} />
        <button onClick={handleSubmit} disabled={!text || !model}>
          Submit
        </button>
      </div>

      <div className="results">
        {loading && <p className="loading">Loading...</p>}
        {data && (
          <div className="result" style={{ display: 'flex', justifyContent: 'space-between' }}>
            <div className="result-text" style={{ textAlign: 'left', width: '50%', marginRight: '20px' }}>
              <h3>Results</h3>
              <p><b>Text analyzed:</b> {data.text_analyzed}</p>
              <p><b>Sentiment score:</b> {data.sentiment?.score.toFixed(2)}</p>
              <p><b>Sentiment category:</b> {data.sentiment?.category}</p>
              <p><b>Inference time:</b> {data.inference_time_s.toFixed(2)}s</p>
              <p><b>Inference time formatted:</b> {data.inference_time_formatted}</p>

              <h4 className="parts-of-speech">Parts of speech tagging</h4>
              <p>[
                {data.pos_tagging.map((item, index) => (
                  <span key={index}>
                    {item[0]} - {item[1]}
                    {index !== data.pos_tagging.length - 1 && ', '}
                  </span>
                ))}
              ]</p>

              <h4 className="named-entity">Named entity recognition</h4>
              <p>[
                {data.ner.map((item, index) => (
                  <span key={index}>
                    {item[0]} - {item[1]}
                    {index !== data.ner.length - 1 && ', '}
                  </span>
                ))}
              ]</p>
          </div>

          <div className="result-arrays" style={{ textAlign: 'left', width: '50%' }}>
              <h4 className="embeddings">Embeddings</h4>
              <p>[
                {data.embeddings.map((item, index) => (
                  <span key={index}>
                    {item.toFixed(2)}
                    {index !== data.embeddings.length - 1 && ', '}
                  </span>
                ))}
              ]</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App
