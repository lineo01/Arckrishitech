# Arkrishitech UI editing guide

The browser app is a static frontend served from `public/` by the FastAPI application.
The `frontend/` directory is a synchronized copy for separate frontend hosting. When changing UI files, update both copies (or copy the edited `public/` file into the matching `frontend/` path).

## Main files

| What to edit | File |
|---|---|
| Page structure, section order, labels, navigation, assistant layout | `public/index.html` |
| Colours, spacing, responsive layout, cards, chat and reference panel | `public/css/style.css` |
| App navigation, API calls, chat submit, voice input/output, sensor flow | `public/js/main.js` |
| Dynamic UI rendering: crop cards, calendar, chat answer bubbles, tables | `public/js/screens.js` |
| Backend requests and API helper | `public/js/api.js` |
| Farm map and drawing controls | `public/js/map.js` |
| Brand image and favicon assets | `public/assets/` |
| Knowledge entries used by the assistant | `backend/app/knowledge.json` |
| Knowledge retrieval and answer formatting | `backend/app/kb.py` |

## Assistant layout

The assistant is in `public/index.html` inside `<section id="assistant">`.
- The main chat is `.assistant-chat-panel`.
- The right-hand evidence/reference column is `.assistant-references`.
- The desktop column ratio and responsive behaviour are controlled by `.assistant-content` in `public/css/style.css`.
- Chat messages and their rendering are handled by `addChat()` in `public/js/screens.js`.
- Sending questions and speech controls are handled by `askAssistant()` and the voice functions in `public/js/main.js`.

## Branding

Replace `public/assets/arkrishitech-logo.png` with a transparent PNG of the desired logo, keeping the same filename. Copy it to `frontend/assets/arkrishitech-logo.png` as well. The header uses the `.brand-logo` rule in `style.css`.

## Market data UI

The market-price card and its browser loader have been removed from the UI. The old `market.js` browser loader is no longer included. The dated market snapshot and update script are retained as project data/automation assets, but they are not displayed in the app.

## After editing

1. Edit the matching files under `public/`.
2. Copy the changed HTML/CSS/JS/assets to the corresponding `frontend/` paths if using that hosting target.
3. Run the backend tests: `cd backend && KS_OFFLINE=1 pytest -q`.
4. Run `node --check public/js/main.js` and `node --check public/js/screens.js`.
5. Commit and push the project; Vercel redeploys when connected to the repository.
