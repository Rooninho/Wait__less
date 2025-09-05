# WaitLess 🕒🤖  
**Smart AI-Powered Customer Queue Management System**  

WaitLess is an AI-inspired customer service assistant that helps manage queues in an orderly and efficient manner.  

It automatically:  
- Skips staff (detected by staff ID).  
- Assigns customers systematically to available desks (first-come, first-served).  
- Announces customers via **voice guidance** (Windows SAPI Speech).  
- Prevents traffic by ensuring sequential flow.  

---

## 🚀 Features
- **Dynamic Seating**: Customers are assigned to Wing A (Desks 1–7) or Wing B (Desks 8–14).  
- **First Come, First Served**: Queue system ensures fairness.  
- **Staff Detection**: Staff IDs are skipped automatically.  
- **Voice Announcements**: Customers are guided by voice to their desk.  
- **Cross-Platform Ready**: Voice works on Windows out-of-the-box (SAPI). Mac/Linux fallback available via `say` or `espeak`.  

---

## 📂 Project Structure
WaitLess/
│── main.py # Entry point – runs the queue system
│── seating.py # Manages seating & queue assignment
│── announcer.py # Handles voice + print announcements
│── requirements.txt # Python dependencies
│── README.md # Project documentation
|__pycache

🛠 Installation

