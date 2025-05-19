# 🗓️ Score Notification CLI App

A **Python-based command-line tool** for scheduling events and automatically detecting time conflicts. Designed to help students, professionals, or anyone manage their time effectively by avoiding overlapping classes, meetings, or study sessions.

---

##  Features

-  Add events with title, start/end time, and description
-  Automatically detects **conflicts** with existing events
-  View all scheduled events sorted by start time
-  Delete events by title
-  All data is stored locally using JSON (no database required)

---

##  Technologies Used

- **Python 3.7+**
- Standard libraries only: `argparse`, `datetime`, `json`, `os`, `bisect`

---

##  Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EmmaRams/score-notification-cli.git
   cd score-notification-cli
