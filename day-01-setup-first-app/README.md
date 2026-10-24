# Day 01 — Setup & First App 🚀

**Videos:** 1, 2, 3 ✅ | Video 4 (first app) ⏳ coming soon

---

## 🧠 What I Learned

**FastAPI** is a modern, high-performance Python framework for building APIs. Fast to run, fast to write.

**API (Application Programming Interface)** is the middleman between software systems. A mobile app never touches the database directly (that's how you get hacked 💀). It sends a request to the API, and the API hands back *only* the data that's needed. Clean, controlled, secure.

**Virtual environment** is a private sandbox for each project.
Project A wants FastAPI v0.95, Project B wants v0.115? No fight. Each one lives in its own bubble 🫧, and nothing leaks into the system Python.

---

## ⌨️ Commands

```bash
python3 -m venv venv          # build the sandbox
source venv/bin/activate      # step inside (prompt shows "(venv)")
pip install fastapi uvicorn   # bring in the framework + the server
```

**Proof it worked:** `Successfully installed fastapi-0.162.0 uvicorn-0.54.0` 🎉

---

## 🍎 Video vs My Mac

| Video (Windows) | Me (macOS) |
|---|---|
| `python` | `python3` |
| `env\Scripts\activate` | `source venv/bin/activate` |
| folder named `env` | folder named `venv` (any name works) |

---

## 🐛 Mistakes (a.k.a. Character Development)

- Said "done" without actually running `pip install`. 🙃 **Lesson:** no output = not done.
- Almost pushed the entire `venv/` folder (thousands of files) to GitHub. **Fix:** added `venv/` to `.gitignore`. Crisis averted. 🛡️

---

## 🔗 Where This Shows Up in NexaKnow

- The NexaKnow backend needs these same packages (FastAPI, Uvicorn, etc.). **TODO:** find where its dependencies are listed (`requirements.txt` or `pyproject.toml`?).
- Inside Docker, the container itself plays the "isolated sandbox" role, so a venv isn't really needed there. 🐳

---

## ⏭️ Next Up

Video 4: write `main.py`, run it with `uvicorn`, and open `/docs` for the free interactive API docs. 👀