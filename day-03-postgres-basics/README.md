# Day 03 — PostgreSQL Basics 🐘

**Videos:** 9 ✅ 10 ✅ | 11 ⏳ coming soon

---

## 🧠 What I Learned

**Database** = an organised collection of data.
- **Relational** (PostgreSQL, MySQL, Oracle): rows and columns, like a spreadsheet with rules.
- **Non-relational** (MongoDB): JSON documents, key-value, graphs.

**The order of things:** server → database → table (columns) → rows

| Thing | Command | Think of it as |
|---|---|---|
| Database | `CREATE DATABASE` | a folder |
| Columns | `CREATE TABLE` | the header row |
| Rows | `INSERT` | each new line of data |
| Change a row | `UPDATE ... WHERE` | edit one cell |
| Add a column later | `ALTER TABLE ... ADD COLUMN` | add a new header |

Instead of the video's sample courses, my table tracks **my own learning**: this repo and 90 Days of DevOps. 📚

---

## 🐳 Video vs Me

The video installs Postgres with a Windows installer and uses pgAdmin. I did it the DevOps way:

| Video | Me |
|---|---|
| Installer, Next → Next → Next | One `docker run` |
| pgAdmin (GUI) | `psql` (terminal) |
| Port 5432 | Port **5433** (5432 was already taken by another project's container) |

```bash
docker volume create fastapi-pgdata
docker pull postgres:18

docker run -d \
  --name fastapi-postgres \
  -e POSTGRES_PASSWORD=<your-password> \
  -p 127.0.0.1:5433:5432 \
  -v fastapi-pgdata:/var/lib/postgresql \
  postgres:18
```

- `127.0.0.1` → only my Mac can connect, not the whole Wi-Fi 🔒
- `-v` volume → data survives container restarts
- **Two containers can both use port 5432 inside.** Only the Mac-side port must be unique.

Run the whole SQL file in one shot:

```bash
docker exec -i fastapi-postgres psql -U postgres -d mydatabase < day-03-postgres-basics/course.sql
```

(`-i` only, no `-t`: piping a file into a TTY fails.)

---

## ⌨️ psql Cheat Sheet

| Command | Does |
|---|---|
| `\pset pager off` | stop getting trapped in `(END)` 😤 |
| `\l` | list databases |
| `\c mydatabase` | switch database |
| `\d course` | describe a table |
| `\q` | quit |

All SQL lives in [`course.sql`](./course.sql).

---

## 🐛 Mistakes (a.k.a. Character Development)

- **Forgot `;`** → prompt changed from `=#` to `-#` and nothing ran. The database I "created" never existed. 👻
- **Created the table in the wrong database** (`postgres` instead of `mydatabase`). Lesson: always read the prompt.
- **`VALUE` instead of `VALUES`** → syntax error. The `^` in the error points exactly at the mistake.
- **Pressed Ctrl+C during `docker pull`** thinking it was stuck. It was at 111MB/114MB. Patience. 🧘

## 🤯 Surprise Discovery

Two failed `INSERT`s still used up ids 3 and 4, so the next row got **id 5**. `SERIAL` grabs the number *before* checking the row. Gaps in ids are normal, so never use `id` to count rows.

## ⚠️ The Video Has a Bug

It says duration can be `2.5` months but uses `INTEGER`. Postgres would silently round it to `3`. For decimals you need `NUMERIC(3,1)`.

My fix: I track my courses in days anyway, so I renamed it to `duration_days`. No decimals needed. ✅

---

## 🔗 Where This Shows Up in NexaKnow

Today I wrote `CREATE TABLE` by hand. In NexaKnow, tables come from SQLAlchemy models (`adapters/outbound/persistence/`) and Alembic migrations, but underneath it's the same SQL.

---

## ⏭️ Next Up

Video 11, then SQL queries on Day 4.