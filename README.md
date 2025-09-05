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
1.Clone the repo
  git clone https://github.com/your-username/WaitLess.git
cd WaitLess

2.Create and activate a virtual environment:
  python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate  # On Linux/Mac

3.Install dependencies:
  pip install -r requirements.txt

        ▶️ Usage
Run the system:
            python main.py

Expected Output:
                S001 is staff → skipped.
S002 is staff → skipped.
C101, please proceed to Desk 1 (Wing A).
C102, please proceed to Desk 2 (Wing A).
C103, please proceed to Desk 3 (Wing A).
C104, please proceed to Desk 4 (Wing A).

🎤 At the same time, each customer will also be announced via voice.

📖 Example Demo Flow
1.Customer C101 arrives → assigned to Desk 1 (Wing A) → announced by voice.

2.Staff S001 arrives → skipped automatically.

3.Customers continue arriving and are placed in order until all desks are filled.

💡 Future Enhancements
✅ Real-time arrivals (new customers every 30s).

✅ Database/logging of served customers.

✅ Integration with camera systems for automatic detection.

✅ Web dashboard for queue visualization.

👨‍💻 Author
Rooney Wandeto Maina
💼 AI & Cloud Security Enthusiast | 🚀 Building smart automation solutions.
