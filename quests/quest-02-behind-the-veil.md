❗ **Quest 2 of 7 — Behind the Veil**
*Quest line: Old Goat, New Tricks*

> *"You spoke to the Oracle and thought it lived in that window," the old goat says. "It doesn't. It's been a server this whole time — sitting quiet, waiting. Let me show you the strings."*

**Requires:** Quest 1 — Summoning the Oracle.
**Time:** ~10 minutes.
**Reward:** Recipe learned — **Whisper to the Oracle** (send data in, read it out, yourself).

---

### Objectives
- ☐ Find the server that was running the whole time *(0/1)*
- ☐ Send the Oracle a prompt with raw code *(0/1)*
- ☐ Read its answer out of the reply *(0/1)*

---

### 1. It was a server all along

Look at your system tray (bottom-right, by the clock). See the little llama? That's **the Ollama server** — a program that's been running quietly since you installed it, listening on your machine at an address called `localhost:11434`.

Now — back **in your terminal** — type this and press **Enter** to see what the server's holding right now:

```powershell
ollama ps
```

> **Tooltip — server vs client:** a *server* is just a program that waits for requests and answers them. When you ran `ollama run llama3.2` in Quest 1, *that* was a **client** — it shipped your words to the server and printed what came back. The server did the thinking; the chat window was only a messenger.

### 2. Whisper to it yourself

Now *you* be the client. Paste this — it sends a prompt straight to the server, no chat window in the middle:

```powershell
$body = @{ model = "llama3.2"; prompt = "In one sentence, why does a raid need a main tank?"; stream = $false } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:11434/api/generate -Method Post -Body $body
```

You'll get back a block of fields — the model name, some timings, and a **`response`** field with the actual answer.

### 3. Read just the answer

Same call, but pluck out the `response`:

```powershell
(Invoke-RestMethod -Uri http://localhost:11434/api/generate -Method Post -Body $body).response
```

There's your answer, clean.

> **Tooltip — this is the whole game:** you just did by hand exactly what the ChatGPT website does — package a prompt as data, POST it to a model server, read the reply. The only differences: their server is in a datacenter and bills you; yours is in your tray and free. **Data in (prompt as JSON) → server → data out (JSON reply).** Everything left in this questline — the Discord bot included — is just this call, dressed up.

---

### ✅ Checkpoint
You sent a prompt with `Invoke-RestMethod` and read the model's answer back. You've now reached the Oracle two ways — the chat window *and* the raw door — and it was the same server both times.

### 🆘 Stuck? `/whisper` your AI
*"Unable to connect" / "connection refused"* almost always means the server isn't running: open Ollama from the Start menu (the llama returns to your tray), wait a few seconds, try again. Any other error → paste it into your free AI with the Windows/PowerShell buff.

---

🏆 **Quest Complete: Behind the Veil**
*Recipe learned:* **Whisper to the Oracle.**
> *You can send data to the model and read its answer with nobody's app in the way. The veil's gone — it was only ever a server.*

**Next:** ❗ *Quest 3 — Know Your Gear* — find out how big a mind your rig can actually summon.
