# ETTORE

```
----------------------------------------------------------
########  ########  ########  ########  #######   ########
##           ##        ##     ####  ##  ##    ##  ##
########     ##        ##     ## ## ##  ######    ########
##           ##        ##     ##  ####  ##  ###   ##
########     ##        ##     ########  ##   ###  ########
----------------------------------------------------------
```

**Intelligent Wordlist Generator** — a lightweight, pattern-aware wordlist generator for authorized password-strength testing, CTFs, and security research.

> ⚠️ **Legal & Ethical Use Only**
> This tool is built for educational purposes, CTF practice, and authorized penetration testing / red-team engagements. Only use it against systems and accounts you own or have explicit written permission to test. Unauthorized access attempts are illegal.

---

## ✨ Features

- 🔹 **Admin/Standard Mode** — Generates common administrative credential guesses (`admin`, `root`, `user`, etc.) with number and symbol variations.
- 🔹 **Targeted Profile Mode** — Builds a personalized wordlist from OSINT-style profile data (name, nickname, pet name, birth month, age) — the same logic real attackers use for social-engineering-aware password guessing, useful for demonstrating *why* personal info shouldn't inform passwords.
- 🔹 **Pattern Mutation Engine** — Applies capitalization, leetspeak-adjacent digit suffixes, and special-character injection to mimic realistic human password habits.
- 🔹 **Deduplicated Output** — Uses a `set()` internally so every generated entry is unique.
- 🔹 **Zero Dependencies** — Pure Python standard library (`random` only). No `pip install` required.

---

## 🧰 Requirements

- Python 3.7+
- No external packages

---

## 🚀 Usage

```bash
python ettore.py
```

You'll be greeted with the banner, then prompted to choose a mode:

```
Enter the number of Iterations: 20

Select the profile type:
1. Standard / Admin wordlist
2. Targeted profile wordlist
Enter choice (1/2):
```

### Mode 1 — Standard / Admin Wordlist

Generates generic admin-style credentials, ideal for testing default/weak admin panel passwords in a lab environment.

```
admin2024
Root!7
3admin
Administrator9
```

### Mode 2 — Targeted Profile Wordlist

Walks you through collecting a mock profile (first name, last name, age, pet name, nickname, birth month) and produces a wordlist built from realistic personal-info-based password patterns.

```
First name: John
Last name: Doe
Age: 23
Pet name: Max
Has a nickname? (y/n): y
Nickname: Johnny
Month of birth (name or number): March
```

```
Johnny23
max@2024
John#March
23doe
```

---

## 🧠 How It Works

| Component | Purpose |
|---|---|
| `generate_admin_wordlist()` | Combines a base word, digit, and special character using randomized patterns (`word+num`, `Capitalized+num`, `word+char+num`, `num+word`) |
| `generate_profile_wordlist()` | Pulls from profile fields + a pool of digits/specials/years, capped by a `max_attempts` safety limit to avoid infinite loops on sparse input |
| `main()` | CLI entry point — handles banner display, input validation, and mode routing |

---

## 📂 Project Structure

```
ettore/
├── ettore.py        # Main script
└── README.md        # You are here
```

---

## 🗺️ Roadmap

- [ ] Export wordlist directly to `.txt`
- [ ] CLI flags (`argparse`) instead of interactive prompts
- [ ] Configurable pattern rules via JSON/YAML
- [ ] Leetspeak substitution mode (`a→4`, `e→3`, `o→0`)
- [ ] Common year-range injection (birth year ± N)

---

## 👤 Credits

**Created by:** Umair Ansari (Um41r 4n$ar1)

---

## 📜 License

For educational and authorized security testing use only. No warranty provided — use responsibly.
