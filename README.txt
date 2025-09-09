# DJ's Copyright Companion

### A desktop application that helps DJs manage copyright claims on their music before they upload a mix.

---

## 🎧 What is DJ's Copyright Companion?

The **DJ's Copyright Companion** is an open-source, community-driven desktop application for DJs. It automatically scans your local music library, checks it against a community-sourced database of verified copyright information, and tags your tracks with their YouTube claim status.

Stop guessing which songs are safe for your mixes and start creating with confidence.

## ⚠️ The Problem It Solves

As a DJ, you spend hours creating the perfect mix, only to have it muted or blocked on YouTube due to a copyright claim. Manually testing every track is time-consuming and inefficient.

This application automates that process by leveraging a collective database of tracks that have already been tested by other DJs, saving you countless hours and preventing frustrating copyright issues.

---

## ✨ Features

- **Automated Scanning:** The application runs in the background and automatically detects new music added to your library.
- **Community-Driven Data:** Queries an online database populated with copyright statuses from the community.
- **Rekordbox Integration:** Automatically tags your tracks within your Rekordbox library, allowing you to create smart playlists based on a track's copyright status.
- **Simple Workflow:** Turns a tedious, manual task into a seamless, background process.

---

## 🚀 Getting Started

Follow these steps to set up the application on your computer.

### **Prerequisites**

- **Python 3.10** or higher.
- A virtual environment is highly recommended.

### **Installation**

1.  **Clone the Repository:**
    ```
    git clone [https://github.com/yourusername/djs-copyright-companion.git](https://github.com/yourusername/djs-copyright-companion.git)
    cd djs-copyright-companion
    ```
2.  **Activate Virtual Environment:**
    ```
    # On macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    python -m venv venv
    venv\Scripts\activate
    ```
3.  **Install Dependencies:**
    ```
    pip install -r requirements.txt
    ```

### **Usage**

1.  **Run the application:**
    ```
    python main.py
    ```
2.  **Configure Folders:** The first time you run the script, it will prompt you to configure the folders to watch (e.g., your music folder) and the path to your Rekordbox XML file.
3.  **Add Music & Watch the Magic:** Simply add new music files to your designated music folder. The application will automatically detect the new tracks, query the community database, and update your Rekordbox library.
4.  **Check your Rekordbox Library:** Look for the new tags and playlists that have been created, such as `DJCC-SAFE` and `DJCC-BLOCKED`.

---

## 🤝 How to Contribute

This project is entirely open-source and depends on the community! You can contribute in several ways:

-   **Submit a Test Result:** If you test a track and find it’s safe (or not), you can submit your result to the community database through the app.
-   **Report a Bug:** Find a bug? Report it by opening a new issue on GitHub.
-   **Contribute Code:** Check out our `CONTRIBUTING.md` file for details on how to submit a Pull Request.