# Final Submission & Deployment Guide

Follow these steps to deploy your backend 24/7 and build your final APK for the professors.

## Step 1: Deploy Backend to Koyeb (24/7 Free)

Koyeb is a free platform that does not require a credit card.

1.  **Sign up** at [Koyeb.com](https://www.koyeb.com).
2.  **Connect your GitHub** or upload the `d:\ai-career-mentor-backend` folder.
3.  **Create a New Service**:
    *   **Builder**: Choose "Buildpack".
    *   **Port**: 8000.
    *   **Environment Variables**: 
        *   `DATABASE_URL`: (Your database link).
        *   `SECRET_KEY`: (Your JWT secret).
4.  **Deploy**: Once finished, you will get a URL like `https://ai-mentor-xxxx.koyeb.app`.
5.  **Test**: Open `https://ai-mentor-xxxx.koyeb.app/health` in your browser. If you see "healthy", it works!

---

## Step 2: Update Android App with Cloud URL

1.  Open `Constants.kt` in your Android project.
2.  Change `BASE_URL` to your new Koyeb URL:
    ```kotlin
    const val BASE_URL = "https://your-app-name.koyeb.app/" 
    ```

---

## Step 3: Build the Final APK

I have created a script for you. 

1.  Go to `d:\ai-career-mentor-backend\build_apk.bat` (which I just created).
2.  **Move/Copy** this file into your **Android Project folder** (where `gradlew.bat` is).
3.  **Double-click** `build_apk.bat`.
4.  It will create the file at: `app\build\outputs\apk\debug\app-debug.apk`.

---

## Step 4: Final Submission Package

Collect these files into a single ZIP folder to give to your professors:

1.  `app-debug.apk` (The app they will install).
2.  `Project_Documentation.docx` (The professional report I generated).
3.  `TEST_CREDENTIALS.txt` (Your test login info).

---
**Good luck with your submission!**
