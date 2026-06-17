❗ **Quest 5 of 7 — Bind a Familiar**
*Quest line: Old Goat, New Tricks*

> *The old goat finally stands. "Talking to the Oracle in a terminal is a parlor trick. A familiar is different — you bind a piece of it to your own hall, give it a name, and it answers your guild in your voice. Bind it well: its soul is a single key, and whoever holds that key holds the familiar."*

**Requires:** Quest 4 — *A Temporary Outpost* (a server you own) and a working Oracle (Quests 1–3).
**Time:** ~30 minutes. A real pull — bring a drink.
**Reward:** A bound familiar — **the Kid** — living in your outpost, answering every @mention, thinking on your own GPU.

---

### Objectives
- ☐ Gear up — install Python + the libraries *(0/1)*
- ☐ Forge the familiar — create the bot application *(0/1)*
- ☐ Flip the one switch everyone forgets — Message Content Intent *(0/1)*
- ☐ Bind its soul — the token, into `.env` *(0/1)*
- ☐ Summon it to your hall — invite it to your outpost *(0/1)*
- ☐ Breathe life in — run the code, get a reply *(0/1)*

---

### 0. Gear up

The Kid is written in Python, so we need Python and three small libraries. Check first:

```powershell
py --version
```

No version? Install it, then **close and reopen your terminal** so it sees the new tool:

```powershell
winget install Python.Python.3.12 -e
```

Now grab the libraries (the Kid's gear):

```powershell
py -m pip install discord.py ollama python-dotenv
```

> **Tooltip — what these are:** `discord.py` lets your code talk to Discord. `ollama` lets it talk to your local Oracle. `python-dotenv` reads secrets out of a file so they never live in your code. `py` is just the Windows launcher for Python — use it for everything.

The Kid's code already lives in your starter folder at `bot\bot.py` — you don't write it, you run it. Open it once and skim: ~40 commented lines, and you'll recognize the shape from Quest 2 (it's the same client → Oracle call, just triggered by a Discord message instead of you typing).

---

### 1. Forge the familiar

Go to the **Discord Developer Portal** → **New Application**. Name it — a fun move is `Digital_<yourname>` (that's how this questline's author bound *Digital_Flapski*). Then open the **Bot** tab on the left.

> **Tooltip — what you just made:** An "application" is your slot with Discord; the "bot" is the user account inside it that logs in and talks. Right now it has no body in any server and no soul — we add both next.

### 2. Flip the one switch everyone forgets

Still on the **Bot** tab → **Privileged Gateway Intents** → toggle **Message Content Intent → ON**. Save.

> **Tooltip — THE gotcha:** This one switch decides whether your Kid can *read what people type*. Leave it off and he connects, looks perfectly online, and replies to nothing — because every message reaches him blank. Ninety percent of "my bot is broken" is this toggle. We flip it now so it never bites you.

### 3. Bind its soul (the token)

On the same **Bot** tab → **Reset Token** → confirm → **Copy**. Discord reveals a token *once*, so copy it the moment it appears.

In your starter folder, copy `bot\.env.example` to `bot\.env`, open `.env`, and paste the token after `DISCORD_TOKEN=` (no quotes, no spaces). Save.

> **Tooltip — guard the soul:** That token is the familiar's soul and your account's key in one. Anyone who holds it controls your bot — treat it exactly like your password or your authenticator. Never paste it in a chat, never put it in your code, never commit it. It lives in `.env`, which the starter folder already tells git to ignore. If it ever leaks, hit **Reset Token** and the old one dies on the spot.

### 4. Summon it to your hall

On the **OAuth2** tab → **URL Generator**:
- **Scopes:** check `bot`.
- **Bot Permissions:** check **View Channels**, **Send Messages**, **Read Message History** — and nothing else.

Copy the **Generated URL** at the bottom, paste it in a new browser tab, choose **your outpost**, and **Authorize**.

> **Tooltip — least privilege:** You're handing the Kid a keyring, and three keys are all he needs to listen and reply. Don't tick **Administrator** "to be safe" — a familiar holding every key is how a sandbox becomes a disaster.

He'll appear in your member list **greyed-out / offline**. Correct — you've given him a body, but nobody's breathing yet.

### 5. Breathe life in

The spark. In your terminal (from inside your starter folder), run him:

```powershell
py "bot\bot.py"
```

Watch for:

```text
Digital_<yourname> is awake as ...
```

That line is `on_ready` firing — he's live.

> **Tooltip — the terminal is his heartbeat:** As long as this window stays open, the Kid is awake. Close it, or press **Ctrl+C**, and he sleeps (he wakes right back up next time you run the command — nothing is lost). Want your terminal back for other things? Open a **second tab** and leave this one running. Keeping him awake 24/7 without babysitting a window is its own fight — *Quest 7*.

### 6. Pull him

In any channel he can see, type `@` + his name (pick him from the autocomplete so it's a real, blue mention) and ask something:

```text
@Digital_<yourname> in two lines, why do pugs wipe on Patchwerk?
```

The **typing indicator** appears — that's `llama3.2` loading into your GPU on the first hit (the cast time) — then his reply lands in-channel.

> **Tooltip — what just happened:** Your message → discord.py → your local Oracle on your GPU → his reply, back in the channel. The exact loop from Quest 2, now wearing a familiar's face. Nothing left your machine but the round trip to Discord.

---

### ✅ Checkpoint
The Kid replied to your @mention in-channel, and his name shows **online** while your terminal runs. Screenshot that first reply — that's your **Ding** for the board.

### 🆘 Stuck? `/whisper` your AI
If he's silent, it's almost always one of three, in this order:
1. **Message Content Intent is off** (Step 2) — he hears only silence.
2. **The token is wrong** (Step 3) — check the terminal for a login error, then Reset and re-paste.
3. **You typed his name instead of @mentioning him** — it has to be the blue mention picked from autocomplete.

Paste the exact terminal error into your free AI with the buff: *"I'm on Windows running a discord.py bot, never used the command line. I get `<paste>`. What does it mean and exactly what do I fix?"*

---

🏆 **Quest Complete: Bind a Familiar**
*You have bound a familiar:* **the Kid** *(Rank 1).*
> *A spark of the Oracle, given a name and a home in your hall. He answers only you, thinks on your own iron, and costs nothing to keep.*

**Next:** ❗ *Quest 6 — Teach the Kid.* Right now he runs on general knowledge and a 3-billion-parameter brain, so he'll be confidently, gloriously **wrong** sometimes — ask him about Patchwerk's "adds" and watch. That's not a flaw to fix; it's the door to everything interesting. Quest 6 feeds him **your** data. And beyond the chain, learning to *steer* him — ask him to write a story, then change three words of how you ask and watch the whole thing shift — is a questline all its own.
