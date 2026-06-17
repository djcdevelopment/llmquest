🍞 **Breadcrumb — A Sharper Blade**
*Quest line: Old Goat, New Tricks*

> *An old goat by the road doesn't even look up. "Before you summon anything, you'll want a sharper blade than the one Windows hands you. Go get the good terminal. Then come back, and we'll begin."*

**Requires:** nothing. This is where you start.
**Time:** ~3 minutes.
**Reward:** none — a breadcrumb just points you at the hub. Real loot starts at Quest 1.

---

### What a "terminal" is, and why you want a better one

A terminal is a window where you type commands instead of clicking buttons. That's the whole mystery. If you ever edited `autoexec.bat` to free up conventional memory for a DOS game, you've already done something harder than anything in this entire questline. Welcome back to the command line.

Windows hands you an old, clunky terminal. We'll grab the modern one — **Windows Terminal** — because copy-paste actually works, you get tabs, and it won't fight you.

### 1. Draw the heirloom sword

Click **Start**, type `powershell`, press **Enter**. A window opens with a `>` prompt — that's the heirloom blade Windows handed you. Serviceable, but rusty. Let's get you a sharper one.

### 2. Install the better blade

Paste this and press **Enter**:

```powershell
winget install Microsoft.WindowsTerminal -e
```

The first time, winget will likely ask you to accept its terms — *"Do you agree to all the source agreements terms?"* Type **`y`** and press **Enter** to continue. Then it downloads and installs on its own.

> **Tooltip:** `winget` is Windows' built-in app installer — an app store you type to. You'll use it again for Ollama and Python. No hunting for download buttons. *(No winget? Grab Windows Terminal from the Microsoft Store — one click.)*

### 3. Swing the new blade

**Start** → type `terminal` → open **Windows Terminal**. Give it a swing — this is home from now on.

### The five things you'll ever actually need

- **Run a command:** type it, press Enter.
- **Copy / paste:** Ctrl+Shift+C / Ctrl+Shift+V (or just right-click).
- **Repeat your last command:** press the **Up arrow**.
- **Stop something that's running:** **Ctrl+C**.
- **Where am I?** the text before the `>` is the folder you're in.

> **Tooltip — you can't break it by typing:** a command that doesn't exist just errors and does nothing. Poke around. The terminal is patient.

---

### ✅ Checkpoint
Windows Terminal opens to a dark window with a prompt ending in `>`. That's all you need.

**Next:** ❗ *Quest 1 — Summoning the Oracle.*
