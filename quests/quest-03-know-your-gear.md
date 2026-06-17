❗ **Quest 3 of 7 — Know Your Gear**
*Quest line: Old Goat, New Tricks*

> *"Every fight has a gear check," the old goat grunts. "Summoning's no different. Bigger minds need bigger iron. Let's see what yours can carry."*

**Requires:** Quest 1.
**Time:** ~10 minutes.
**Reward:** no loot — this is a gear check. You walk away knowing which models your rig can run, which is worth more than loot.

---

### Objectives
- ☐ See the Oracle running on your GPU *(0/1)*
- ☐ Read your VRAM — your item level *(0/1)*
- ☐ Learn to pull and vendor models *(0/1)*

---

### 1. Watch it light up your GPU

With a model loaded, check where it's running:

```powershell
ollama ps
```

Look at the **PROCESSOR** column — GPU (or a GPU/CPU split) means your graphics card is doing the thinking. Want to watch it sweat?

```powershell
nvidia-smi
```

> **Tooltip:** open Task Manager (Ctrl+Shift+Esc) → Performance → GPU while the model answers, and you'll see it spike. That spike is your proof it's **local** — your card, your power, nothing phoning home.

### 2. Your VRAM is your item level

The number that matters is your GPU's **VRAM** (video memory). It gates which models you can pull, exactly like item level gates which raids you can run. Read the total memory from `nvidia-smi`, then:

| Your VRAM (ilvl) | What you can pull |
|---|---|
| 8 GB | 7–8B models (`llama3.1:8b`) — snappy |
| 12 GB | up to ~14B |
| 16 GB | 14B comfortably |
| 24 GB+ | 32B and beyond |

Everyone can run the starter, `llama3.2` (3B). Nobody gets gated out at the door.

> **Tooltip — the trade:** bigger models are smarter but slower and hungrier for VRAM; smaller ones are faster and dumber. There's no "best," only "best that fits." A 3B that answers instantly often beats a 32B that makes you wait — especially for a chatty Discord familiar.

### 3. Manage your bags

Models eat real disk space (gigabytes each). Check your bags, pull a new one, vendor an old one:

```powershell
ollama list                 # what you've got
ollama pull llama3.1:8b     # grab a bigger one (if your ilvl allows)
ollama rm llama3.1:8b       # delete one you don't use
```

Browse the whole armory at **ollama.com/library**.

---

### ✅ Checkpoint
You've confirmed the Oracle runs on your GPU, you know your VRAM, and you can pull or remove models at will. You know your gear.

### 🆘 Stuck? `/whisper` your AI
`nvidia-smi` *"not recognized"* → you may be on integrated graphics or missing NVIDIA drivers; paste it to your AI. A model that *"runs on CPU"* or won't load → it's too big for your VRAM; pull a smaller one.

---

🏆 **Quest Complete: Know Your Gear**
*No loot — but you now know exactly what your rig can summon and how to swap models in and out. That knowledge is the quest.*

**Next:** ❗ *Quest 4 — A Temporary Outpost* — raise a hall of your own to bind a familiar in.
