print("Dashboard Started")

import customtkinter as ctk
import customtkinter as ctk
from datetime import datetime
import os
import serial
import threading

PORT = "COM6"
BAUD = 115200

print("Opening COM6...")

try:
    esp = serial.Serial(PORT, BAUD, timeout=1)
    print("ESP Connected")
    connected = True

except Exception as e:
    print("Connection Error:", e)
    esp = None
    connected = False
    print("❌ Connection Error:", e)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Smart Personal Desk Guardian")
app.geometry("1200x700")
app.resizable(False, False)

title = ctk.CTkLabel(app,text="🛡 SMART PERSONAL DESK GUARDIAN",font=("Arial",28,"bold"))
title.pack(pady=20)

dashboard = ctk.CTkFrame(app,width=1100,height=500)
dashboard.pack(pady=10)

left = ctk.CTkFrame(dashboard,width=350,height=450)
left.place(x=20,y=20)

right = ctk.CTkFrame(dashboard,width=680,height=450)
right.place(x=390,y=20)

ctk.CTkLabel(left,text="SYSTEM STATUS",font=("Arial",20,"bold")).pack(pady=20)

connection_status = ctk.CTkLabel(left,text="🟢 ESP32 Connected" if connected else "🔴 ESP32 Disconnected",font=("Arial",18))
connection_status.pack(pady=10)

motion_status = ctk.CTkLabel(left,text="👤 Motion : No Motion",font=("Arial",18))
motion_status.pack(pady=10)

desk_status = ctk.CTkLabel(left,text="📳 Desk : Stable",font=("Arial",18))
desk_status.pack(pady=10)

alarm_status = ctk.CTkLabel(left,text="🚨 Alarm : OFF",font=("Arial",18))
alarm_status.pack(pady=10)
threat_status = ctk.CTkLabel(
    left,
    text="🟢 Threat : LOW",
    font=("Arial",18),
    text_color="green"
)
threat_status.pack(pady=10)

ctk.CTkLabel(right,text="EVENT HISTORY",font=("Arial",22,"bold")).pack(pady=15)

history_box = ctk.CTkTextbox(right,width=620,height=300,font=("Consolas",15))
history_box.pack(pady=10)

def add_history(msg):
    history_box.insert("end",datetime.now().strftime("%H:%M:%S")+"  "+msg+"\n")
    history_box.see("end")

add_history("System Started")

clock = ctk.CTkLabel(app,text="",font=("Arial",18))
clock.pack(pady=10)

def update_clock():
    clock.configure(text=datetime.now().strftime("%d-%m-%Y   %H:%M:%S"))
    app.after(1000,update_clock)

update_clock()

last=""
# ----------------------------
# Create Daily Log File
# ----------------------------

def save_log(event, threat):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    log_dir = os.path.join(project_root, "LOGS")
    os.makedirs(log_dir, exist_ok=True)

    filename = os.path.join(log_dir, datetime.now().strftime("%Y-%m-%d") + ".txt")

    with open(filename, "a", encoding="utf-8") as file:
        file.write("="*60 + "\n")
        file.write(f"Date   : {datetime.now().strftime('%d-%m-%Y')}\n")
        file.write(f"Time   : {datetime.now().strftime('%H:%M:%S')}\n")
        file.write(f"Alert  : {event}\n")
        file.write(f"Threat : {threat}\n")
        file.write("="*60 + "\n\n")

def process(data):
    global last

    if data == last:
        return

    last = data

    if data == "SAFE":
        motion_status.configure(
            text="👤 Motion : No Motion",
            text_color="white"
        )

        desk_status.configure(
            text="📳 Desk : Stable",
            text_color="white"
        )

        alarm_status.configure(
            text="🚨 Alarm : OFF",
            text_color="green"
        )
        threat_status.configure(
    text="🟢 Threat : LOW",
    text_color="green"
)
        save_log("SAFE", "LOW")

    elif data == "MOTION":
        motion_status.configure(
            text="👤 Motion : DETECTED",
            text_color="red"
        )

        desk_status.configure(
            text="📳 Desk : Stable",
            text_color="white"
        )

        alarm_status.configure(
            text="🚨 Alarm : ON",
            text_color="red"
        )

        add_history("Motion Detected")
        save_log("Motion Detected", "HIGH")
        threat_status.configure(
    text="🔴 Threat : HIGH",
    text_color="red"
)

    elif data == "VIBRATION":
        motion_status.configure(
            text="👤 Motion : No Motion",
            text_color="white"
        )

        desk_status.configure(
            text="📳 Desk : Vibration Detected",
            text_color="orange"
        )

        alarm_status.configure(
            text="🚨 Alarm : ON",
            text_color="orange"
        )

        add_history("Desk Vibration Detected")
        save_log("Desk Vibration Detected", "MEDIUM")
        threat_status.configure(
    text="🟠 Threat : MEDIUM",
    text_color="orange"
)

    elif data == "BOTH":
        motion_status.configure(
            text="👤 Motion : DETECTED",
            text_color="red"
        )

        desk_status.configure(
            text="📳 Desk : Vibration Detected",
            text_color="orange"
        )

        alarm_status.configure(
            text="🚨 Alarm : ON",
            text_color="red"
        )

        add_history("Motion + Vibration Detected")
        save_log("Motion + Vibration Detected", "CRITICAL")
        threat_status.configure(
    text="🚨 Threat : CRITICAL",
    text_color="red"
)
def serial_reader():
    if esp is None:
        return

    while True:
        try:
            if esp.in_waiting:
                data = esp.readline().decode(errors="ignore").strip()

                if data:
                    print("Received:", data)   # Prints in terminal
                    app.after(0, process, data)

        except Exception as e:
            print("Error:", e)

threading.Thread(target=serial_reader,daemon=True).start()

app.mainloop()