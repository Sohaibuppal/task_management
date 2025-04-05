from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from auth import authenticate_user
import secrets

web_router = APIRouter()

@web_router.get("/login", response_class=HTMLResponse)
def login_page():
    return """<form action='/login' method='post'>
              Email: <input type='text' name='email'/>
              Password: <input type='password' name='password'/>
              <input type='submit' value='Login'/>
              </form>"""

@web_router.post("/login")
def web_login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    response = RedirectResponse(url="/dashboard", status_code=302)
    response.set_cookie(key="session_token", value=secrets.token_hex(16))
    return response