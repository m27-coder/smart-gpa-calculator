# Deploy as a public website (Streamlit Community Cloud)

**Smart GPA Calculator and Prediction System** is ready to host for free on [Streamlit Community Cloud](https://streamlit.io/cloud). Your public URL will look like:

`https://YOUR-APP-NAME.streamlit.app`

---

## What you need

1. A **GitHub** account ([sign up](https://github.com/signup))
2. This project pushed to a **public** GitHub repository
3. A **Streamlit Cloud** account ([sign up](https://share.streamlit.io/) — use “Continue with GitHub”)

No credit card is required for the free tier.

---

## Step 1 — Push code to GitHub

### Option A: GitHub website (no terminal)

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `smart-gpa-calculator` (or any name)
3. Visibility: **Public**
4. Do **not** add README, .gitignore, or license (this project already has them)
5. Click **Create repository**
6. On the new repo page, follow **“uploading an existing file”** and upload these files/folders:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `verify_calculations.py`
   - `PPT-003_SCREENSHOTS.md`
   - `DEPLOY.md`
   - `.gitignore`
   - `.python-version`
   - `.streamlit/` folder (`config.toml` only — **not** `secrets.toml`)

### Option B: Git commands (recommended)

Open PowerShell in the project folder:

```powershell
cd "c:\Users\MICHAEL\.gemini\antigravity\scratch\smart-gpa-calculator"

git init
git add app.py requirements.txt README.md verify_calculations.py PPT-003_SCREENSHOTS.md DEPLOY.md .gitignore .python-version .streamlit/config.toml
git commit -m "Prepare Smart GPA Calculator for Streamlit Cloud deployment"

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/smart-gpa-calculator.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. Create the empty repo on GitHub first (Step 1 in Option A, items 1–4 only).

---

## Step 2 — Deploy on Streamlit Cloud

1. Open **[share.streamlit.io](https://share.streamlit.io/)** and sign in with GitHub
2. Click **Create app** (or **New app**)
3. Fill in:
   | Field | Value |
   |-------|--------|
   | Repository | `YOUR_USERNAME/smart-gpa-calculator` |
   | Branch | `main` |
   | Main file path | `app.py` |
   | App URL (optional) | e.g. `smart-gpa-calculator` |
4. Click **Deploy**

Build usually takes 2–5 minutes. When it finishes, your app is live at the URL shown on the dashboard.

---

## Step 3 — Share the link

Copy the app URL from Streamlit Cloud and use it in:

- Your course presentation (PPT-003)
- README or portfolio
- Social / project submission

Example: `https://smart-gpa-calculator.streamlit.app`

---

## Updating the live site

After you change code locally:

```powershell
git add .
git commit -m "Describe your change"
git push
```

Streamlit Cloud rebuilds automatically on each push to `main`.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Build fails on `requirements.txt` | Ensure all four packages are listed; do not commit `venv/` |
| App shows blank / error | Open **Manage app → Logs** on Streamlit Cloud |
| Matplotlib charts missing | Wait for full deploy; refresh the page |
| Custom domain | Available on paid Streamlit plans; free tier uses `.streamlit.app` |

---

## Alternative hosts (optional)

| Platform | Notes |
|----------|--------|
| [Hugging Face Spaces](https://huggingface.co/spaces) | Select **Streamlit** as SDK; upload same files |
| [Render](https://render.com) | Use a Web Service with `streamlit run app.py --server.port=$PORT` |

For this project, **Streamlit Community Cloud** is the simplest option.

---

## Security note

Do **not** commit `.streamlit/secrets.toml` or `.env` files. This app does not need API keys for public deployment.
