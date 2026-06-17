# analyze-a-pull.py
# The hero move: feed ONE raid pull to your local Oracle and ask why you wiped.
# Data in (a parse summary) -> analysis out -> observed in your terminal.
#
# Requires:
#   - Ollama installed and running        (Quest 1)
#   - Python + the ollama package          (Quest 4 installs these: `pip install ollama`)
#
# Run it from anywhere:  python analyze-a-pull.py

from pathlib import Path
import ollama  # the library just makes the same HTTP call you'll learn to do by hand in Quest 2

# --- 1. DATA IN -----------------------------------------------------------
# We feed a SUMMARY of one pull, not the raw 2-million-line WoWCombatLog.txt.
# That raw log won't fit in the model's context window (Quest 3 explains why).
# A parse summary is the right-sized "pull" to hand it.
data_file = Path(__file__).parent.parent / "data" / "pull-14-naxx-example.txt"
pull = data_file.read_text(encoding="utf-8")

# --- 2. THE PRE-PULL BUFF -------------------------------------------------
# A system prompt tells the model who it is before the fight. Think raid buff.
system = (
    "You are a hardcore WoW raid analyst. You read parse summaries and explain, "
    "bluntly and specifically, why the raid wiped and what each role must change. "
    "Cite the actual numbers from the data. No fluff, no praise. Raiders can take it."
)

# --- 3. THE PULL ----------------------------------------------------------
question = "Why did we wipe on this pull, and what are the 3 specific changes for next pull?"

print("Summoning the Oracle... (first reply has a cast time while the model loads)\n")

response = ollama.chat(
    model="llama3.2",  # 3B gives a decent read. Pulled an 8B in Quest 3? Swap the name here for a sharper one.
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": f"{question}\n\n--- PULL DATA ---\n{pull}"},
    ],
)

# --- 4. DATA OUT ----------------------------------------------------------
print(response["message"]["content"])
