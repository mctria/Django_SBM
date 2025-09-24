
# 📖 Django Random Blog Project

A simple **Django Blog Application** with:

- ✍️ CRUD (Create, Read, Update, Delete) for posts  
- 👤 User authentication (Signup/Login/Logout)  
- 📦 Database powered by **Supabase (PostgreSQL)**  
- 🎨 Custom UI styled with HTML/CSS (digest-style cards)  
- 🎲 Random joke post generator (using [Official Joke API](https://official-joke-api.appspot.com/random_joke))  
- 🚀 Deployment on **Vercel**  

---

## 🛠️ Tech Stack
- [Django](https://www.djangoproject.com/) (Python web framework)  
- [Supabase](https://supabase.com/) (Managed PostgreSQL database)  
- [Whitenoise](http://whitenoise.evans.io/en/stable/) (Static file serving)  
- [Vercel](https://vercel.com/) (Serverless deployment)  
- [uv](https://github.com/astral-sh/uv) (Python package manager, faster than pip)  

---

## ⚡ Features
- Users can **signup, login, and logout** (auth system).  
- Authenticated users can **create/edit/delete posts**.  
- Post list and detail views with digest card-style UI.  
- **Random Post Generator** → click a button to fetch a random joke and pre-fill the form.  
- Responsive UI, sticky footer, nice digest-style look.  

---

## 📂 Project Structure
```
DemoBlog/
│── blog/                # Blog application (models, views, urls, templates)
│── DemoBlog/            # Project root (settings, wsgi, asgi)
│── staticfiles/         # Collected static assets (committed for Vercel)
│── templates/           # Base templates and auth pages
│── manage.py
│── requirements.txt     # Exported from uv for Vercel
│── vercel.json          # Vercel config
│── pyproject.toml       # uv project definition
│── uv.lock              # uv lockfile
```

---

## 🚀 Local Development

1. Clone repository:
   ```bash
   git clone https://github.com/your-username/django-blog.git
   cd django-blog
   ```

2. Install dependencies using [uv](https://github.com/astral-sh/uv):
   ```bash
   uv sync
   ```
   or
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   uv run python manage.py migrate
   ```
   or
   ```
   python manage.py migrate
   ```

6. Create superuser:
   ```bash
   uv run python manage.py createsuperuser
   ```

7. Collect static files:
   ```bash
   uv run python manage.py collectstatic --noinput
   ```

8. Run dev server:
   ```bash
   uv run python manage.py runserver
   ```

---

## 🗄️ Supabase (Postgres) Setup

1. Create a project at [Supabase](https://supabase.com/).  
2. Go to **Settings → Database → Connection Info**.  
3. Copy your connection string, e.g.
   ```
   postgres://postgres:password@db.xxxxx.supabase.co:5432/postgres
   ```
4. Add to `.env` file:
   ```
   DATABASE_URL=postgres://postgres:password@db.xxxxx.supabase.co:5432/postgres
   DJANGO_SECRET_KEY=your-secret-key
   DEBUG=True
   ```

---

## 🎲 Random Joke Post

- Access `http://localhost:8000/post/random/`  
- A random joke will pre-fill the title/content using Official Joke API.  
- Click **Save** to store it as a post.

---

## 🌍 Deploy on Vercel (Serverless)

1. Export dependencies:
   ```bash
   uv export --output-file requirements.txt
   ```

2. Add `vercel.json`:
   ```json
   {
     "builds": [{ "src": "manage.py", "use": "@vercel/python" }],
     "routes": [
       { "src": "/static/(.*)", "dest": "/static/$1" },
       { "src": "/(.*)", "dest": "manage.py" }
     ]
   }
   ```

3. Collect static files:
   ```bash
   uv run python manage.py collectstatic --noinput
   ```

4. Deploy to Vercel:
   ```bash
   vercel
   ```

5. Add environment variables in Vercel dashboard:
   - `DATABASE_URL` (Supabase string)  
   - `DJANGO_SECRET_KEY`  
   - `DEBUG=False`

---
