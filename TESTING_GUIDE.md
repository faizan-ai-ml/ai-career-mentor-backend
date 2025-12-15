# 🧪 Quick Test Guide - Phase 1 Backend

## Test Using Swagger UI (Easiest Method)

1. **Start the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Open Swagger docs**: http://localhost:8000/docs

3. **Test Signup**:
   - Click on `POST /auth/signup`
   - Click "Try it out"
   - Enter:
     ```json
     {
       "email": "test@example.com",
       "password": "Password123",
       "full_name": "Test User"
     }
     ```
   - Click "Execute"
   - **Copy the `access_token` from response!**

4. **Authorize with token**:
   - Click the green "Authorize" button (top right)
   - Enter: `Bearer YOUR_ACCESS_TOKEN_HERE`
   - Click "Authorize", then "Close"

5. **Test protected endpoint**:
   - Click on `GET /auth/me`
   - Click "Try it out"
   - Click "Execute"
   - Should see your user info!

6. **Test login**:
   - Click on `POST /auth/login`
   - Use same credentials
   - Get new token

---

## Test Using Postman (Alternative)

### 1. Signup
```
POST http://localhost:8000/auth/signup
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "Password123",
  "full_name": "Test User"
}
```

### 2. Login
```
POST http://localhost:8000/auth/login
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "Password123"
}
```

**Save the access_token from response!**

### 3. Get Current User (Protected)
```
GET http://localhost:8000/auth/me
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## Test Using cURL (Command Line)

```bash
# Signup
curl -X POST "http://localhost:8000/auth/signup" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"Password123\",\"full_name\":\"Test User\"}"

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"Password123\"}"

# Get current user (replace TOKEN with your actual token)
curl -X GET "http://localhost:8000/auth/me" \
  -H "Authorization: Bearer TOKEN"
```

---

## Expected Responses

### Successful Signup/Login
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "test@example.com",
    "full_name": "Test User",
    "created_at": "2024-01-15T10:30:00"
  }
}
```

### Get Current User
```json
{
  "id": 1,
  "email": "test@example.com",
  "full_name": "Test User",
  "created_at": "2024-01-15T10:30:00"
}
```

### Error: Email Already Exists
```json
{
  "detail": "Email already registered"
}
```

### Error: Invalid Credentials
```json
{
  "detail": "Invalid email or password"
}
```

### Error: Invalid Token
```json
{
  "detail": "Could not validate credentials"
}
```

---

## ✅ Checklist

- [ ] Server starts without errors
- [ ] Can create new user (signup)
- [ ] Can login with credentials
- [ ] Receive valid access token
- [ ] Can access protected endpoint with token
- [ ] Get error with invalid credentials
- [ ] Get error when email already exists

---

## 🐛 Common Issues

**Port already in use**:
```bash
# Kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Database not found**:
- Run migrations: `alembic upgrade head`
- Check DATABASE_URL in .env

**Import errors**:
- Run from project root
- Activate virtual environment

---

Once all tests pass, you're ready for Android Phase 1! 🎉
