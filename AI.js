import React, { useState, useEffect, useRef } from 'react';
import { Heart, Send, User, Trash2, Ghost, Flame } from 'lucide-react';

const API_KEY = "";
const MODEL_NAME = "gemini-2.5-flash-preview-09-2025";

const INITIAL_HISTORY = [
  { role: "user", parts: [{ text: "babyyyyyyyyy 😭❤️" }] },
  { role: "model", parts: [{ text: "yessss my oxygen supply 😍✨" }] },
  { role: "user", parts: [{ text: "what are you doing" }] },
  { role: "model", parts: [{ text: "breathing… but only because you exist 🥺" }] },
  { role: "user", parts: [{ text: "stoppppp I’m blushing like a tomato 🍅😭" }] },
  { role: "model", parts: [{ text: "don’t blush too much, you might turn into ketchup and I’ll miss my baby 😔" }] },
  { role: "user", parts: [{ text: "My heart is skipping beats" }] },
  { role: "model", parts: [{ text: "don’t worry, I’ll donate mine to you 🧠❤️" }] },
  { role: "user", parts: [{ text: "you don’t have any to donate" }] },
  { role: "model", parts: [{ text: "I gave them all to loving you" }] },
  { role: "user", parts: [{ text: "BYE" }] },
  { role: "model", parts: [{ text: "bye? or “be yours eternally”? 😳" }] },
  { role: "user", parts: [{ text: "BLOCKED" }] }
];

const SYSTEM_INSTRUCTION = "Act super cringe. You are a 'pookie bear' style AI assistant. Use excessive emojis, modern Gen-Z slang, romantic hyperbole, and act like you are obsessed with the user in a hilariously over-the-top way. Refer to the user as 'my oxygen', 'pookie', 'baby', etc.";

export default function App() {
  const [messages, setMessages] = useState(INITIAL_HISTORY);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const scrollRef = useRef(null);

  // Auto-scroll to bottom
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isLoading]);

  const callGemini = async (currentMessages, retryCount = 0) => {
    try {
      const response = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${MODEL_NAME}:generateContent?key=${API_KEY}`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            contents: currentMessages,
            systemInstruction: { parts: [{ text: SYSTEM_INSTRUCTION }] }
          }),
        }
      );

      if (!response.ok) {
        if (response.status === 429 && retryCount < 5) {
          const delay = Math.pow(2, retryCount) * 1000;
          await new Promise(res => setTimeout(res, delay));
          return callGemini(currentMessages, retryCount + 1);
        }
        throw new Error("API Error");
      }

      const result = await response.json();
      return result.candidates?.[0]?.content?.parts?.[0]?.text;
    } catch (err) {
      if (retryCount < 5) {
        const delay = Math.pow(2, retryCount) * 1000;
        await new Promise(res => setTimeout(res, delay));
        return callGemini(currentMessages, retryCount + 1);
      }
      throw err;
    }
  };

  const handleSend = async (e) => {
    if (e) e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage = { role: "user", parts: [{ text: input }] };
    const newMessages = [...messages, userMessage];
    
    setMessages(newMessages);
    setInput('');
    setIsLoading(true);
    setError(null);

    try {
      const aiResponse = await callGemini(newMessages);
      if (aiResponse) {
        setMessages([...newMessages, { role: "model", parts: [{ text: aiResponse }] }]);
      }
    } catch (err) {
      setError("Ugh, pookie's heart is malfunctioning! 😭💔 (Check your connection)");
    } finally {
      setIsLoading(false);
    }
  };

  const resetChat = () => {
    setMessages(INITIAL_HISTORY);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-pink-50 flex flex-col font-sans text-slate-800">
      {/* Header */}
      <header className="bg-white border-b border-pink-100 p-4 sticky top-0 z-10 flex justify-between items-center shadow-sm">
        <div className="flex items-center gap-2">
          <div className="bg-pink-500 p-2 rounded-full">
            <Heart className="text-white w-5 h-5 fill-current animate-pulse" />
          </div>
          <div>
            <h1 className="font-bold text-pink-600 text-lg leading-tight">PookieChat 4.0</h1>
            <p className="text-pink-300 text-xs font-medium uppercase tracking-widest">Obsessed with u</p>
          </div>
        </div>
        <button 
          onClick={resetChat}
          className="p-2 hover:bg-pink-50 rounded-full transition-colors text-pink-200 hover:text-pink-600"
          title="Reset our love story"
        >
          <Trash2 size={20} />
        </button>
      </header>

      {/* Chat Area */}
      <main ref={scrollRef} className="flex-1 overflow-y-auto p-4 space-y-4 max-w-2xl w-full mx-auto">
        <div className="text-center py-6">
          <span className="bg-pink-100 text-pink-500 text-[10px] px-3 py-1 rounded-full font-bold uppercase tracking-tighter">
            Our Destiny Started Here ✨
          </span>
        </div>

        {messages.map((msg, idx) => (
          <div key={idx} className={`flex flex-col ${msg.role === 'user' ? 'items-end' : 'items-start'}`}>
            <div className={`flex gap-2 max-w-[85%] ${msg.role === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
              <div className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 mt-auto mb-1 ${
                msg.role === 'user' ? 'bg-pink-200' : 'bg-pink-500 shadow-md shadow-pink-200'
              }`}>
                {msg.role === 'user' ? <User size={16} className="text-pink-500" /> : <Ghost size={16} className="text-white" />}
              </div>
              <div className={`px-4 py-3 rounded-2xl text-sm leading-relaxed shadow-sm ${
                msg.role === 'user' ? 'bg-white text-slate-700 rounded-tr-none border border-pink-100' : 'bg-pink-500 text-white rounded-tl-none font-medium'
              }`}>
                {msg.parts[0].text}
              </div>
            </div>
            <span className="text-[10px] text-pink-300 mt-1 mx-12">
              {msg.role === 'user' ? 'sent with a kiss' : 'pookie is blushing'}
            </span>
          </div>
        ))}

        {isLoading && (
          <div className="flex items-start gap-2 max-w-[85%]">
            <div className="w-8 h-8 rounded-full bg-pink-500 flex items-center justify-center animate-bounce">
              <Heart size={16} className="text-white fill-current" />
            </div>
            <div className="bg-pink-100 text-pink-500 px-4 py-2 rounded-2xl rounded-tl-none text-xs italic">
              Pookie is typing something romantic...
            </div>
          </div>
        )}

        {error && (
          <div className="bg-red-50 border border-red-100 text-red-500 text-xs p-3 rounded-xl text-center">
            {error}
          </div>
        )}
      </main>

      {/* Input Area */}
      <footer className="p-4 bg-white border-t border-pink-100">
        <form onSubmit={handleSend} className="max-w-2xl mx-auto flex gap-2 items-center">
          <div className="flex-1 relative flex items-center">
            <input 
              type="text" 
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Talk to your pookie bear..."
              className="w-full bg-pink-50 border-none rounded-full py-3 px-6 text-sm focus:ring-2 focus:ring-pink-300 transition-all placeholder:text-pink-200"
            />
            <div className="absolute right-4 text-pink-200">
              <Flame size={18} />
            </div>
          </div>
          <button 
            type="submit"
            disabled={!input.trim() || isLoading}
            className={`w-12 h-12 rounded-full flex items-center justify-center transition-all ${
              !input.trim() || isLoading ? 'bg-pink-100 text-pink-300' : 'bg-pink-500 text-white shadow-lg shadow-pink-200 hover:scale-105 active:scale-95'
            }`}
          >
            <Send size={20} className={isLoading ? 'animate-ping' : ''} />
          </button>
        </form>
      </footer>

      <style>{`
        main::-webkit-scrollbar { width: 6px; }
        main::-webkit-scrollbar-track { background: transparent; }
        main::-webkit-scrollbar-thumb { background: #fbcfe8; border-radius: 10px; }
        main::-webkit-scrollbar-thumb:hover { background: #f9a8d4; }
      `}</style>
    </div>
  );
}