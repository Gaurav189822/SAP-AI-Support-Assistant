import { useState } from "react";
import axios from "axios";
import PdfUploader from "./PdfUploader";

export default function Chatbot() {

  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {

    if (!query.trim()) return;

    const userMessage = {
      type: "user",
      text: query,
      time: new Date().toLocaleTimeString(),
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {

      const response = await axios.post(
        "http://localhost:8000/chat",
        {
          query: query,
        }
      );

      const aiMessage = {
        type: "ai",
        text: response.data.answer,
        references: response.data.references || [],
        time: new Date().toLocaleTimeString(),
      };

      setMessages((prev) => [...prev, aiMessage]);

    } catch {

      const errorMessage = {
        type: "ai",
        text: "Unable to connect to backend.",
        time: new Date().toLocaleTimeString(),
      };

      setMessages((prev) => [...prev, errorMessage]);
    }

    setQuery("");
    setLoading(false);
  };

  return (

    <div className="flex flex-col h-screen text-white p-6">

      <PdfUploader />

      <div className="flex-1 overflow-y-auto space-y-6 mb-6 mt-4">

        {messages.length === 0 && (

          <div className="h-full flex flex-col items-center justify-center text-center">

            <div className="text-7xl mb-6">
              🤖
            </div>

            <h2 className="text-4xl font-bold mb-4">
              SAP AI Support Assistant
            </h2>

            <p className="text-gray-400 max-w-2xl text-lg">
              Ask SAP troubleshooting questions, upload SAP PDFs,
              and retrieve AI-powered enterprise support answers.
            </p>

          </div>
        )}

        {messages.map((msg, index) => (

          <div
            key={index}
            className={`flex ${
              msg.type === "user"
                ? "justify-end"
                : "justify-start"
            }`}
          >

            <div
              className={`max-w-[80%] p-5 rounded-3xl shadow-2xl
                ${
                  msg.type === "user"
                    ? "bg-blue-600"
                    : "bg-[#111827] border border-white/10"
                }
              `}
            >

              <div className="flex justify-between items-center mb-3">

                <span className="font-bold text-cyan-300">
                  {msg.type === "user"
                    ? "You"
                    : "SAP AI"}
                </span>

                <span className="text-xs text-gray-400">
                  {msg.time}
                </span>

              </div>

              <p className="leading-relaxed whitespace-pre-wrap">
                {msg.text}
              </p>

              {msg.references &&
                msg.references.length > 0 && (

                <div className="mt-6">

                  <h3 className="font-bold mb-4 text-cyan-300">
                    Retrieved References
                  </h3>

                  <div className="space-y-3">

                    {msg.references.map((ref, idx) => (

                      <div
                        key={idx}
                        className="bg-white/5 border border-white/10 rounded-2xl p-4"
                      >

                        <p className="text-sm text-gray-300 leading-relaxed">
                          {ref.chunk}
                        </p>

                        <div className="mt-3 flex justify-between items-center">

                          <span className="text-xs text-gray-400">
                            Semantic Match Score
                          </span>

                          <span className="bg-green-500/10 text-green-400 px-3 py-1 rounded-full text-sm font-semibold">

                            {typeof ref.score === "number"
                              ? ref.score.toFixed(2)
                              : ref.score}

                          </span>

                        </div>

                      </div>
                    ))}

                  </div>

                </div>
              )}

            </div>

          </div>
        ))}

        {loading && (

          <div className="flex justify-start">

            <div className="bg-[#111827] border border-white/10 rounded-3xl p-5">

              <div className="flex gap-2">

                <div className="w-3 h-3 rounded-full bg-blue-400 animate-bounce"></div>

                <div className="w-3 h-3 rounded-full bg-blue-400 animate-bounce delay-100"></div>

                <div className="w-3 h-3 rounded-full bg-blue-400 animate-bounce delay-200"></div>

              </div>

            </div>

          </div>
        )}

      </div>

      <div className="bg-white/5 border border-white/10 rounded-3xl p-4">

        <div className="flex gap-4">

          <input
            type="text"
            placeholder="Ask SAP issue..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
            className="flex-1 bg-[#0f172a] border border-white/10 rounded-2xl px-5 py-4 outline-none text-white"
          />

          <button
            onClick={sendMessage}
            disabled={loading}
            className="bg-blue-600 hover:bg-blue-700 transition-all px-8 py-4 rounded-2xl font-bold"
          >
            Send
          </button>

        </div>

      </div>

    </div>
  );
}