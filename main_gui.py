# Python GUI placeholder

### **Block Diagram**
![Block Diagram](assets/block_diagram.png)

---

## 🛠 Hardware Used
- **ESP32 DevKit**  
- **NEO-6M GPS Module**  
- **16x2 / LED Display / TFT Display**  
- **Power Supply Module**  
- **Audio Output (optional)**  

---

## 💻 Software & Technologies
- **Python 3.x**
- **Tkinter GUI for Frontend Dashboard**
- **Firebase (Realtime Database)**
- **Google Maps API**
- **ESP32 Arduino Framework**
- **GPS Parsing (TinyGPS++)**
- **Edge Algorithms** (Distance + ETA + Speed Filtering)

---

## 🚀 How the System Works
1. The GPS module continuously reads latitude & longitude.  
2. ESP32 formats the data and pushes it to **Firebase**.  
3. Python processing engine fetches data, computes:  
   - Distance to bus stop  
   - Estimated Time of Arrival (ETA)  
   - Bus occupancy (if enabled)  
4. Display system shows arrival time + status.  
5. Audio + blinking color indicators assist all passenger groups.  

---

# 🧪 Setup & Installation

## 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/RTBIS.git
cd RTBIS
