import { useEffect, useState } from "react";
import { createClient } from "@supabase/supabase-js";
import { motion, AnimatePresence } from "motion/react";
import { Send, MessageSquare, CheckCircle, XCircle } from "lucide-react";

const supabase = createClient(
  "https://yzyzoultqmuxhbnujqkt.supabase.co",
  "sb_publishable_-Ts93NuJv4iUTGqP_xkkLg_pXV7CaHt"
);

type Entry = {
  id: string;
  name: string;
  message: string;
  created_at: string;
};

function timeAgo(dateStr: string) {
  const diff = Date.now() - new Date(dateStr).getTime();
  const mins = Math.floor(diff / 60000);
  const hours = Math.floor(diff / 3600000);
  const days = Math.floor(diff / 86400000);
  if (mins < 1) return "just now";
  if (mins < 60) return mins + "m ago";
  if (hours < 24) return hours + "h ago";
  return days + "d ago";
}

function getInitials(name: string) {
  return name.split(" ").map(n => n[0]).join("").toUpperCase().slice(0, 2);
}

function getColor(name: string) {
  const colors = ["bg-blue-500", "bg-purple-500", "bg-green-500", "bg-orange-500", "bg-pink-500", "bg-cyan-500", "bg-red-500", "bg-yellow-500"];
  const idx = name.charCodeAt(0) % colors.length;
  return colors[idx];
}

export default function Guestbook() {
  const [entries, setEntries] = useState<Entry[]>([]);
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchEntries();

    const channel = supabase
      .channel("guestbook-changes")
      .on("postgres_changes", { event: "INSERT", schema: "public", table: "guestbook" }, (payload) => {
        setEntries(prev => [payload.new as Entry, ...prev]);
      })
      .subscribe();

    return () => { supabase.removeChannel(channel); };
  }, []);

  const fetchEntries = async () => {
    const { data } = await supabase
      .from("guestbook")
      .select("*")
      .order("created_at", { ascending: false })
      .limit(20);
    if (data) setEntries(data);
    setLoading(false);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim() || !message.trim()) return;
    setStatus("loading");
    const { error } = await supabase.from("guestbook").insert([{ name: name.trim(), message: message.trim() }]);
    if (error) {
      setStatus("error");
      setTimeout(() => setStatus("idle"), 3000);
    } else {
      setStatus("success");
      setName("");
      setMessage("");
      setTimeout(() => setStatus("idle"), 3000);
    }
  };

  return (
    <section id="guestbook" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Community</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Guestbook</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Leave a message, say hi, or share your thoughts. Everyone is welcome.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10">
          <div className="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 p-6">
            <div className="flex items-center gap-2 mb-6">
              <MessageSquare className="w-4 h-4 text-blue-500" />
              <h3 className="font-semibold text-gray-900 dark:text-white">Leave Your Mark</h3>
            </div>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1.5">Your Name *</label>
                <input
                  value={name}
                  onChange={e => setName(e.target.value)}
                  placeholder="John Doe"
                  maxLength={50}
                  required
                  className="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all text-sm"
                />
              </div>
              <div>
                <label className="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1.5">Message *</label>
                <textarea
                  value={message}
                  onChange={e => setMessage(e.target.value)}
                  placeholder="Say something nice..."
                  maxLength={500}
                  required
                  rows={4}
                  className="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all text-sm resize-none"
                />
                <p className="text-xs text-gray-400 text-right mt-1">{message.length}/500</p>
              </div>
              <button
                type="submit"
                disabled={status === "loading"}
                className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-60 transition-all text-sm font-medium shadow-lg shadow-blue-500/20"
              >
                {status === "loading" ? (
                  <><div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" /> Posting...</>
                ) : (
                  <><Send className="w-4 h-4" /> Post Message</>
                )}
              </button>
              {status === "success" && (
                <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="flex items-center gap-2 text-green-600 dark:text-green-400 text-sm font-medium">
                  <CheckCircle className="w-4 h-4" /> Message posted!
                </motion.div>
              )}
              {status === "error" && (
                <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="flex items-center gap-2 text-red-500 text-sm font-medium">
                  <XCircle className="w-4 h-4" /> Something went wrong. Try again!
                </motion.div>
              )}
            </form>
          </div>

          <div className="space-y-3 max-h-[500px] overflow-y-auto pr-1">
            {loading ? (
              Array.from({ length: 3 }).map((_, i) => (
                <div key={i} className="bg-white dark:bg-gray-950 rounded-xl border border-gray-200 dark:border-gray-800 p-4 animate-pulse">
                  <div className="flex items-center gap-3 mb-2">
                    <div className="w-8 h-8 rounded-full bg-gray-200 dark:bg-gray-700" />
                    <div className="h-3 w-24 bg-gray-200 dark:bg-gray-700 rounded" />
                  </div>
                  <div className="h-3 w-full bg-gray-100 dark:bg-gray-800 rounded" />
                </div>
              ))
            ) : entries.length === 0 ? (
              <div className="flex flex-col items-center justify-center py-16 text-center">
                <MessageSquare className="w-8 h-8 text-gray-300 dark:text-gray-600 mb-3" />
                <p className="text-gray-400 dark:text-gray-500 text-sm">No messages yet. Be the first!</p>
              </div>
            ) : (
              <AnimatePresence>
                {entries.map((entry) => (
                  <motion.div
                    key={entry.id}
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="bg-white dark:bg-gray-950 rounded-xl border border-gray-200 dark:border-gray-800 p-4 hover:border-blue-200 dark:hover:border-blue-800 transition-colors"
                  >
                    <div className="flex items-center gap-3 mb-2">
                      <div className={"w-8 h-8 rounded-full flex items-center justify-center text-white text-xs font-bold flex-shrink-0 " + getColor(entry.name)}>
                        {getInitials(entry.name)}
                      </div>
                      <div className="flex items-center gap-2 min-w-0">
                        <p className="text-sm font-medium text-gray-900 dark:text-white truncate">{entry.name}</p>
                        <span className="text-xs text-gray-400 dark:text-gray-500 flex-shrink-0">{timeAgo(entry.created_at)}</span>
                      </div>
                    </div>
                    <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed pl-11">{entry.message}</p>
                  </motion.div>
                ))}
              </AnimatePresence>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}
