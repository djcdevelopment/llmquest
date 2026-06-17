❗ **Quest 1 of 7 — Summoning the Oracle**
*Quest line: Old Goat, New Tricks*

> *"So. You want to learn a new trick." The old goat doesn't look up from the fire. "Everyone starts the same way — you summon something that answers only to you. No internet. No subscription. No one reading over your shoulder. Speak the words, and see for yourself."*

**Requires:** Breadcrumb — *A Sharper Blade* (a working terminal window)
**Time:** ~10 minutes. One pull.
**Reward:** New ability — **Summon Local Intelligence**

---

### Objectives

- ☐ Install Ollama *(0/1)*
- ☐ Summon a model: `llama3.2` *(0/1)*
- ☐ Receive the Oracle's first reply *(0/1)*

---

### 1. Install the Oracle's engine

In your terminal, paste this and press **Enter**:

```powershell
winget install --id Ollama.Ollama -e
```

If winget can't find it (older Windows), grab the installer instead — same result, just the click-the-button version:
→ **https://ollama.com/download** → run `OllamaSetup.exe` → click through → done.

> **Tooltip — what just happened:** You installed a program called Ollama. It does two jobs: it *downloads* AI models, and it *runs* them. When the install finished, a small llama appeared in your system tray (bottom-right, by the clock). That llama is a **server** — a program sitting quietly in the background, waiting for you to ask it something. It's already running. Hold that thought; it's the whole game in Quest 2.

### 2. Summon your first model

```powershell
ollama run llama3.2
```

The first time, this **downloads** the model (~2 GB — one-time, go refill your drink). Every time after, it's instant.

> **Tooltip — cast time:** That download is a one-time cast. After it lands, summoning the model takes a couple of seconds while it loads into your graphics card's memory — *that's the cast bar, not a freeze.* `llama3.2` is a small 3B model: it runs on **any** NVIDIA card, so nobody in the guild gets gated out at step one. Which bigger models your rig can pull is the gear check in Quest 3.

### 3. Speak to it

When you see the `>>>` prompt, the Oracle is listening. Type anything and press **Enter**:

```text
>>> explain a raid wipe to someone who has never played WoW, in two sentences
```

It answers. On your machine. With your GPU. No browser tab, no account, no bill.

Run one more, then we'll get out cleanly:

```text
>>> /bye
```

`/bye` ends the conversation and drops you back at the normal terminal prompt.

> **Tooltip — what just happened:** You just ran a large language model — the same *kind* of thing behind ChatGPT — entirely on your own hardware. Your text went **in**, the model's answer came **out**, and you watched it happen live. Data in, data out, observed. That is the entire shape of everything that follows. The rest of this chain only changes *what* goes in and *where* the answer comes out.

---

### ✅ Checkpoint

You should be back at a normal `PS C:\…>` prompt, and you can re-summon the Oracle any time with `ollama run llama3.2`. If that's true, the objective's clear — move to Quest 2.

### 🆘 Stuck? `/whisper` your AI

You've got a free copilot in your browser — ChatGPT, Gemini, or Claude (claude.ai). Before you ask, apply the buff so it doesn't waste your time:

> *"I'm on Windows 11 using PowerShell. I've never used the command line before. I ran `<the command>` and got this exact error: `<paste the exact red text>`. What does it mean, and exactly what do I type to fix it?"*

Paste the **exact** error. Half of fixing a wipe is reading the log — same here.

---

🏆 **Quest Complete: Summoning the Oracle**

*You have learned a new ability:* **Summon Local Intelligence** *(Rank 1).*

> *Calls forth an intelligence that answers from your own machine. Requires no internet. Costs no gold. Watched by no one.*

**Next:** ❗ *Quest 2 — Behind the Veil* — where you find out the Oracle was a server the whole time, and learn to whisper to it without the terminal.
