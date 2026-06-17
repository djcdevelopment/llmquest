❗ **Quest 5 of 7 — Bind a Familiar**
*Quest line: Old Goat, New Tricks*

> *The old goat finally stands. "Talking to the Oracle in a terminal is a parlor trick. A familiar is different — you bind a piece of it, give it a name, and it answers your guild in your voice. Bind it well: its soul is a single key, and whoever holds that key holds the familiar."*

**Requires:** Quest 4 (the outpost's keys), a working Oracle (Quests 1–3), and **this repo's files on your PC** — see *How to follow this* in the README (it's a Download-ZIP, no git needed).
**Time:** ~20 minutes — most of it is now double-clicks.
**Reward:** A bound familiar — **the Kid** — answering your @mentions from the outpost, thinking on your own GPU.

---

### Objectives
- ☐ Gear up — one double-click *(0/1)*
- ☐ Forge the familiar — create the bot application *(0/1)*
- ☐ Flip the one switch everyone forgets — Message Content Intent *(0/1)*
- ☐ Bind its soul — the token, into `.env` *(0/1)*
- ☐ Summon it to the outpost *(0/1)*
- ☐ Breathe life in — one double-click, then @mention *(0/1)*

---

### 0. Gear up — double-click `setup.bat`

In the `bot` folder (inside the `llmquest-main` folder you downloaded), **double-click `setup.bat`**. It installs Python (if you don't have it), installs the Kid's three libraries, and creates your `.env` file — all on its own.

> **Tooltip — the one wrinkle:** if it had to install Python from scratch, it'll say *"close this window and double-click setup.bat once more."* Do exactly that — Windows needs a fresh window to see the new Python, and the second run finishes the job. *(Prefer to type it? The slow way still works: `winget install Python.Python.3.12 -e`, then `py -m pip install discord.py ollama python-dotenv`.)*

### 1. Forge the familiar

Go to the **Discord Developer Portal** → **New Application**. Name it `Digital_<yourname>` (that's how *Digital_Flapski* was bound), agree to the terms, and click **Create**. *(Discord may pop a "Wait — are you human?" check; tick **I am human** and carry on.)* Then open the **Bot** tab on the left.

### 2. Flip the one switch everyone forgets

On the **Bot** tab, scroll to **Privileged Gateway Intents** → toggle **Message Content Intent → ON** → then click the green **Save Changes** bar that slides up at the bottom. *(Skip that save and the toggle silently won't stick — and your Kid will hear nothing.)*

> **Tooltip — THE gotcha:** this switch decides whether your Kid can *read what people type*. Off = he connects, looks perfectly online, and replies to nothing. Ninety percent of "my bot is broken" is this toggle.

### 3. Bind its soul (the token)

On the **Bot** tab → **Reset Token** → confirm → **Copy**. Discord shows a token *once*, so copy it the moment it appears.

Open `.env` (setup.bat made it for you, in the `bot` folder) in Notepad, paste the token after `DISCORD_TOKEN=` (no quotes, no spaces), and save.

> **Tooltip — guard the soul:** that token is the familiar's soul and your account's key in one. Treat it like your password — never in a chat, never in your code, never committed. It lives in `.env`, which is already set to be ignored. If it ever leaks, hit **Reset Token** and the old one dies on the spot.

### 4. Summon it to the outpost

Copy this link and replace `YOUR_APP_ID` with your **Application ID** (Dev Portal → **General Information** → Application ID → Copy):

```
https://discord.com/oauth2/authorize?client_id=YOUR_APP_ID&permissions=68608&scope=bot
```

Open it in your browser, pick the **guild outpost** from the dropdown (you have the keys from Quest 4), and **Authorize**.

> **Tooltip — no checkbox wrestling:** that link already has the exact scope and three permissions baked in — see channels, send messages, read history, nothing more. Your Kid shows up in the outpost **offline** until you wake him next.

### 5. Breathe life in — double-click `start-kid.bat`

Back in the `bot` folder, **double-click `start-kid.bat`**. A window opens, and within a few seconds you'll see:

```text
Digital_<yourname> is awake as ...
```

He's live.

> **Tooltip — the window is his heartbeat:** leave it open, he's awake; close it (or press Ctrl+C), he sleeps — double-click `start-kid.bat` to wake him again. Keeping him up 24/7 *without* babysitting that window is its own fight, *Quest 7*.

### 6. Pull him

In the outpost, type `@` + his name (pick him from the autocomplete so it's a real, blue mention) and ask:

```text
@Digital_<yourname> in two lines, why do pugs wipe on Patchwerk?
```

The **typing indicator** appears — that's `llama3.2` loading into your GPU (the cast time) — then his reply lands in-channel.

> **Tooltip — what just happened:** your message → discord.py → your local Oracle on your GPU → his reply. The exact loop from Quest 2, now wearing a familiar's face. Nothing left your machine but the round trip to Discord.

---

### ✅ Checkpoint
The Kid replied to your @mention in the outpost, and his name shows **online** while `start-kid.bat` is running. Screenshot that first reply — that's your **Ding** for the board.

### 🆘 Stuck? `/whisper` your AI
If he's silent, it's almost always one of three, in this order:
1. **Message Content Intent is off** (Step 2) — he hears only silence.
2. **The token is wrong** (Step 3) — check the `start-kid.bat` window for a login error, then Reset and re-paste.
3. **You typed his name** instead of a real, blue @mention.

Paste the exact error from the window into your free AI with the buff: *"I'm on Windows running a discord.py bot, never used the command line. I get `<paste>`. What does it mean and exactly what do I fix?"*

---

🏆 **Quest Complete: Bind a Familiar**
*You have bound a familiar:* **the Kid** *(Rank 1).*
> *A spark of the Oracle, given a name and a home in the outpost. Answers only to you, thinks on your own iron, costs nothing to keep.*

**Next:** ❗ *Quest 6 — Teach the Kid.* He runs on a 3B brain, so he'll be confidently, gloriously **wrong** sometimes — ask about Patchwerk's "adds" and watch. Not a flaw; the door to everything. Quest 6 feeds him **your** data.
