❗ **Quest 6 of 7 — Teach the Kid**
*Quest line: Old Goat, New Tricks*

> *"He answers well enough," says the old goat, "but he knows nothing of you. A familiar earns its keep when it knows what you know. Teach him — and learn where his memory ends."*

**Requires:** Quest 5 — Bind a Familiar (a working Kid).
**Time:** ~20 minutes.
**Reward:** **Choose your spec** — point the Kid at the data that's *yours*.

---

### Objectives
- ☐ Give the Kid a domain (edit his system prompt) *(0/1)*
- ☐ Feed him a document and watch him analyze it *(0/1)*
- ☐ Find the edge of his memory (the context window) *(0/1)*
- ☐ Choose your spec *(0/1)*

---

### 1. A buff before the pull: the system prompt

Open `bot\bot.py` and find the `SYSTEM = (...)` block. That text is the Kid's standing orders — his **pre-pull buff** — applied before every single answer. Right now it makes him a dry old goat. Make him *yours*. For a combat-log analyst:

```python
SYSTEM = (
    "You are the guild's combat-log analyst. You are blunt and specific, you cite "
    "numbers, and you never sugar-coat a wipe. If you don't have the data, you say so."
)
```

Save, stop the bot (**Ctrl+C** in its terminal), run it again (`py "bot\bot.py"`), and @mention him. Different goat.

> **Tooltip — this *is* prompt engineering:** you changed *who he is* without touching the model. Change three words of those orders and his whole voice shifts. That skill — shaping the answer by shaping the ask — is most of what "AI engineering" actually is.

### 2. Feed him a document

The system prompt sets his *attitude*. To give him *knowledge*, you hand him data in the message itself. Your starter folder has a worked example — a raid pull, analyzed. Run it:

```powershell
py "examples\analyze-a-pull.py"
```

It reads `data\pull-14-naxx-example.txt` (a parse summary), hands it to the Oracle, and asks why the raid wiped. Read his verdict. Then open that `.txt`, change the numbers, and run it again — the analysis follows your data.

> **Tooltip — data in, analysis out:** this is the entire "plug in your own dataset" move. The file is the data; the script feeds it in; the model reasons over it. Swap the file, keep the script.

### 3. Find the edge of his memory

Try to feed him *everything* — your full raw `WoWCombatLog.txt`, all two million lines — and he'll choke. That wall is the **context window**: how much text a model can hold in mind at once. Your VRAM was your item level; the context window is **how big a pull you can feed him in one go.**

That's exactly why the example fed a *summary of one pull*, not the whole log. The skill of choosing what to feed — and summarizing the rest — is called **context management**, and it's a questline of its own.

> **Tooltip — catch him lying:** small models state wrong things with total confidence (ask yours about Patchwerk's "adds" and watch). That's not a bug to rage at — it's the sport. Noticing it is the first rung; steering him past it is the climb.

### 4. Choose your spec

The pattern — *system prompt for attitude, a document for knowledge* — works on **any** data. Pick the one that's yours:

- 🗡️ **Combat Logs** — why you wiped, who stood in the fire (you just did this one)
- 💰 **Finance** — a CSV of your trades or dividends
- 🏈 **Sports** — a roster, a box score, a fantasy lineup
- 🚗 **Cars** — maintenance logs, spec sheets
- 🌦️ **Weather** — a station's history

Drop your file in `data\`, point a copy of `analyze-a-pull.py` at it, change the question. Same machine, your world.

---

### ✅ Checkpoint
You've re-specced the Kid's system prompt, fed him a document and gotten real analysis back, and you understand why you feed summaries instead of raw logs. Post his sharpest line to the **#ding-board**.

### 🆘 Stuck? `/whisper` your AI
Edited `bot.py` and he won't start? Paste the red error — it's usually a stray quote or comma. He ignores your file? Make sure you actually read the file *into* the prompt (copy how `analyze-a-pull.py` does it).

---

🏆 **Quest Complete: Teach the Kid**
*Spec chosen.* The Kid now reasons over **your** data, in a voice **you** set.
> *A familiar that knows what you know is worth ten that don't.*

**Next:** ❗ *Quest 7 — Attuned* — keep him alive, and claim the title.
