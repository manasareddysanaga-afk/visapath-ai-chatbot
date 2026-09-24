'use client'

import { useState, useRef, useEffect } from 'react'

const API_URL = 'http://127.0.0.1:8000'

export default function ChatPage() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  async function sendMessage() {
    const question = input.trim()

    if (!question || loading) {
      return
    }

    setInput('')

    setMessages((old) => [
      ...old,
      {
        role: 'user',
        content: question
      }
    ])

    setLoading(true)

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: question
        })
      })

      const data = await response.json()

      setMessages((old) => [
        ...old,
        {
          role: 'assistant',
          content: data.response || 'Sorry, I could not generate a response.'
        }
      ])
    } catch (error) {
      setMessages((old) => [
        ...old,
        {
          role: 'assistant',
          content:
            'Sorry, I could not connect to the VisaPath backend.'
        }
      ])
    }

    setLoading(false)
  }

  function handleKeyDown(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault()
      sendMessage()
    }
  }

  function clearChat() {
    setMessages([])
    setInput('')
  }

  return (
    <main className="page">

      <div className="chat">

        {/* HEADER */}
        <header className="header">

          <div className="logoCircle">
            V
          </div>

          <div>
            <h1>VisaPath</h1>
            <p>Your AI Immigration Assistant</p>
          </div>

          <div className="status">
            <span></span>
            Online
          </div>

        </header>


        {/* WELCOME */}
        {messages.length === 0 && (
          <section className="welcome">

            <div className="welcomeIcon">
              ✦
            </div>

            <h2>Welcome to VisaPath</h2>

            <p>
              Your AI assistant for UK visas, jobs,
              sponsors, employers and relocation.
            </p>

            <div className="suggestions">

              <button
                onClick={() =>
                  setInput('What visa options might I have to work in the UK?')
                }
              >
                🇬🇧 UK work visa options
              </button>

              <button
                onClick={() =>
                  setInput('How can I find a UK employer who sponsors visas?')
                }
              >
                💼 Find a sponsored job
              </button>

              <button
                onClick={() =>
                  setInput('What is the Skilled Worker visa?')
                }
              >
                📋 Skilled Worker visa
              </button>

            </div>

          </section>
        )}


        {/* MESSAGES */}
        <section className="messages">

          {messages.map((message, index) => (

            <div
              key={index}
              className={
                message.role === 'user'
                  ? 'message user'
                  : 'message assistant'
              }
            >

              {message.role === 'assistant' && (
                <div className="avatar">
                  V
                </div>
              )}

              <div className="messageContent">

                <div className="messageName">
                  {message.role === 'user'
                    ? 'You'
                    : 'VisaPath'}
                </div>

                <div className="bubble">
                  {message.content}
                </div>

              </div>

            </div>

          ))}

          {loading && (
            <div className="message assistant">

              <div className="avatar">
                V
              </div>

              <div className="messageContent">

                <div className="messageName">
                  VisaPath
                </div>

                <div className="bubble typing">
                  Thinking...
                </div>

              </div>

            </div>
          )}

          <div ref={bottomRef}></div>

        </section>


        {/* INPUT */}
        <section className="inputSection">

          <div className="inputBox">

            <textarea
              value={input}
              onChange={(event) => setInput(event.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask VisaPath about UK visas..."
              rows={1}
            />

            <button
              className="send"
              onClick={sendMessage}
              disabled={loading}
            >
              ↑
            </button>

          </div>

          <div className="bottomRow">

            <span>
              VisaPath provides general immigration information.
            </span>

            {messages.length > 0 && (
              <button
                className="clear"
                onClick={clearChat}
              >
                Clear chat
              </button>
            )}

          </div>

        </section>

      </div>


      <style jsx>{`

        * {
          box-sizing: border-box;
        }

        .page {
          min-height: 100vh;
          background: #f4f8f8;
          color: #17323a;
          font-family:
            Inter,
            ui-sans-serif,
            system-ui,
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            sans-serif;

          display: flex;
          justify-content: center;
          align-items: center;

          padding: 32px 20px;
        }


        .chat {
          width: 100%;
          max-width: 920px;
          height: 88vh;
          min-height: 600px;

          background: #ffffff;

          border: 1px solid #dce8e8;
          border-radius: 24px;

          box-shadow:
            0 20px 60px rgba(22, 70, 76, 0.10);

          display: flex;
          flex-direction: column;

          overflow: hidden;
        }


        /* HEADER */

        .header {
          height: 76px;

          display: flex;
          align-items: center;

          padding: 0 28px;

          border-bottom: 1px solid #e5eeee;

          background: #ffffff;
        }


        .logoCircle {
          width: 42px;
          height: 42px;

          border-radius: 50%;

          background: #0b7a8e;
          color: white;

          display: flex;
          align-items: center;
          justify-content: center;

          font-size: 18px;
          font-weight: 700;

          margin-right: 12px;
        }


        .header h1 {
          margin: 0;

          font-size: 20px;
          font-weight: 700;

          color: #123b43;
        }


        .header p {
          margin: 3px 0 0;

          font-size: 12px;
          color: #718589;
        }


        .status {
          margin-left: auto;

          display: flex;
          align-items: center;
          gap: 6px;

          font-size: 12px;
          color: #6b7d80;
        }


        .status span {
          width: 7px;
          height: 7px;

          border-radius: 50%;

          background: #27ae78;
        }


        /* WELCOME */

        .welcome {
          text-align: center;

          max-width: 650px;

          margin: auto;

          padding: 40px 24px;
        }


        .welcomeIcon {
          width: 54px;
          height: 54px;

          margin: 0 auto 18px;

          border-radius: 16px;

          background: #e4f3f3;
          color: #0b7a8e;

          display: flex;
          align-items: center;
          justify-content: center;

          font-size: 25px;
        }


        .welcome h2 {
          margin: 0;

          font-size: 30px;
          line-height: 1.2;

          color: #123b43;
        }


        .welcome p {
          max-width: 500px;

          margin: 12px auto 28px;

          color: #6b7d80;

          font-size: 15px;
          line-height: 1.6;
        }


        .suggestions {
          display: flex;
          justify-content: center;
          flex-wrap: wrap;
          gap: 10px;
        }


        .suggestions button {
          background: #f7fbfb;

          border: 1px solid #d7e7e7;

          color: #27545c;

          border-radius: 12px;

          padding: 11px 14px;

          cursor: pointer;

          font-size: 13px;

          transition: 0.2s;
        }


        .suggestions button:hover {
          background: #e9f5f5;
          border-color: #a9d1d1;
        }


        /* MESSAGES */

        .messages {
          flex: 1;

          overflow-y: auto;

          padding: 28px 32px;

          background: #f8fbfb;
        }


        .message {
          display: flex;

          margin-bottom: 24px;

          gap: 10px;
        }


        .message.user {
          justify-content: flex-end;
        }


        .message.assistant {
          justify-content: flex-start;
        }


        .avatar {
          flex-shrink: 0;

          width: 32px;
          height: 32px;

          border-radius: 50%;

          background: #0b7a8e;

          color: white;

          display: flex;
          align-items: center;
          justify-content: center;

          font-size: 13px;
          font-weight: 700;
        }


        .messageContent {
          max-width: 70%;
        }


        .user .messageContent {
          max-width: 70%;
          text-align: right;
        }


        .messageName {
          margin-bottom: 5px;

          font-size: 11px;
          font-weight: 600;

          color: #7a8c90;
        }


        .bubble {
          padding: 13px 16px;

          border-radius: 16px;

          font-size: 14px;

          line-height: 1.6;

          white-space: pre-wrap;

          color: #263f44;

          background: white;

          border: 1px solid #dce8e8;

          box-shadow:
            0 3px 10px rgba(30, 70, 75, 0.04);
        }


        .user .bubble {
          background: #0b7a8e;

          color: white;

          border: none;

          border-bottom-right-radius: 5px;

          text-align: left;
        }


        .assistant .bubble {
          border-bottom-left-radius: 5px;
        }


        .typing {
          color: #708488;
          font-style: italic;
        }


        /* INPUT */

        .inputSection {
          padding: 16px 20px 12px;

          background: white;

          border-top: 1px solid #e3eeee;
        }


        .inputBox {
          display: flex;
          align-items: flex-end;

          gap: 10px;

          background: #f6fafa;

          border: 1px solid #d5e4e4;

          border-radius: 16px;

          padding: 8px 8px 8px 14px;
        }


        textarea {
          flex: 1;

          border: none;
          outline: none;

          resize: none;

          background: transparent;

          color: #17323a;

          font-family: inherit;

          font-size: 14px;

          line-height: 1.5;

          padding: 7px 0;

          min-height: 24px;
        }


        textarea::placeholder {
          color: #8da0a3;
        }


        .send {
          width: 38px;
          height: 38px;

          border: none;

          border-radius: 11px;

          background: #0b7a8e;

          color: white;

          font-size: 20px;

          cursor: pointer;

          display: flex;
          align-items: center;
          justify-content: center;
        }


        .send:hover {
          background: #096879;
        }


        .send:disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }


        .bottomRow {
          display: flex;

          justify-content: space-between;
          align-items: center;

          padding: 8px 2px 0;

          font-size: 10px;

          color: #87999c;
        }


        .clear {
          border: none;

          background: transparent;

          color: #0b7a8e;

          cursor: pointer;

          font-size: 11px;

          padding: 3px;
        }


        /* MOBILE */

        @media (max-width: 700px) {

          .page {
            padding: 0;
          }


          .chat {
            height: 100vh;
            min-height: 100vh;

            border-radius: 0;

            border: none;
          }


          .header {
            padding: 0 18px;
          }


          .messages {
            padding: 20px 16px;
          }


          .messageContent,
          .user .messageContent {
            max-width: 85%;
          }


          .welcome {
            padding: 30px 18px;
          }


          .welcome h2 {
            font-size: 25px;
          }


          .suggestions {
            flex-direction: column;
          }


          .suggestions button {
            width: 100%;
          }


          .status {
            display: none;
          }

        }

      `}</style>

    </main>
  )
}
