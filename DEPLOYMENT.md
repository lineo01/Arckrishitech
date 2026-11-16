# Vercel deployment checklist

- Import this repository as a **single FastAPI project**.
- Root Directory: `./`
- Framework Preset: **FastAPI**
- Do not select the multi-service `Services` preset.
- Leave Build Command and Output Directory blank/default.
- Keep root `pyproject.toml`, root `requirements.txt`, and root `public/`.
- No `vercel.json` rewrite is required. In particular, do not add a self-rewrite such as `/api/(.*) -> /api/$1`.
- `pyproject.toml` points to `backend.app.main:app`.
- `public/` contains the website and is configured for Vercel CDN static promotion.

After deployment, verify:
- `/` returns the Arkrishitech homepage.
- `/api/health` returns `{"ok":true}`.
- `/css/style.css` and `/js/main.js` return 200.

## Serverless storage warning

The Vercel runtime uses `/tmp` for SQLite and weather cache. It is temporary and not durable. Use a managed database for production persistence.
