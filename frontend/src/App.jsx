import { useState } from 'react'
import './App.css'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  async function sendMessage() {
    if (!input.trim() || loading) return

    const question = input.trim()

    setMessages((prev) => [
      ...prev,
      { role: 'user', content: question }
    ])

    setInput('')
    setLoading(true)

    try {
      const response = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: question
        })
      })

      const data = await response.json()

      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: data.response
        }
      ])
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: 'Unable to connect to VisaPath. Make sure the backend is running.'
        }
      ])
    }

    setLoading(false)
  }

  function handleKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  function clearChat() {
    setMessages([])
  }

  return (
    <div className="app">

      <div className="chat-container">

        {/* HEADER */}
        <header className="header">
          <div className="logo">
            🐦
          </div>

          <div>
            <h1>VisaPath</h1>
            <p>Your AI Immigration Assistant</p>
          </div>
        </header>

        {/* WELCOME */}
        {messages.length === 0 && (
          <div className="welcome">

            <div className="welcome-icon">
              🐦
            </div>

            <h2>Welcome to VisaPath</h2>

            <p>
              Your AI assistant for UK visa eligibility,
              jobs, sponsors, employers and relocation.
            </p>

            <button
              className="suggestion"
              onClick={() =>
                setInput(
                  'I want to work in the UK. What visa options might I have?'
                )
              }
            >
              I want to work in the UK. What visa options might I have?
            </button>

          </div>
        )}

        {/* MESSAGES */}
        <div className="messages">

          {messages.map((message, index) => (

            <div
              key={index}
              className={
                message.role === 'user'
                  ? 'message user-message'
                  : 'message assistant-message'
              }
            >

              {message.role === 'assistant' && (
                <div className="assistant-label">
                  VisaPath
                </div>
              )}

              <div className="message-content">
                {message.content}
              </div>

            </div>

          ))}

          {loading && (
            <div className="message assistant-message">

              <div className="assistant-label">
                VisaPath
              </div>

              <div className="message-content">
                Thinking...
              </div>

            </div>
          )}

        </div>

        {/* INPUT */}
        <div className="input-section">

          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask VisaPath about UK visas..."
            rows="1"
          />

          <button
            className="send-button"
            onClick={sendMessage}
            disabled={loading}
          >
            {loading ? '...' : 'Send'}
          </button>

          <button
            className="clear-button"
            onClick={clearChat}
          >
            Clear
          </button>

        </div>

        <div className="disclaimer">
          VisaPath provides general UK immigration information and is not legal advice.
        </div>

      </div>

    </div>
  )
}

export default App
