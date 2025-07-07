
# ===== FUTURISTIC UI TEMPLATE =====
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeuralGuard | Biometric Access</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #00f7ff;
            --secondary: #008cff;
            --accent: #ff00aa;
            --dark: #0a0a1a;
            --darker: #050510;
            --light: #ffffff;
            --gray: #aaaaaa;
            --neon-glow: 0 0 10px var(--primary), 0 0 20px var(--primary), 0 0 30px var(--primary);
        }
        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--dark);
            color: var(--light);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }
        .header {
            background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 100%);
            padding: 1.5rem;
            text-align: center;
            border-bottom: 1px solid rgba(0, 247, 255, 0.2);
            box-shadow: 0 2px 30px rgba(0, 0, 0, 0.5);
            position: relative;
            z-index: 10;
        }
        .header h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.5rem;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin: 0;
            letter-spacing: 2px;
            text-shadow: var(--neon-glow);
        }
        .main-content {
            display: flex;
            flex: 1;
            padding: 2rem;
            gap: 2rem;
            position: relative;
        }
        .camera-container {
            flex: 2;
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 0 40px rgba(0, 247, 255, 0.15);
            border: 2px solid rgba(0, 247, 255, 0.3);
            min-height: 500px;
            background: #000;
            transition: all 0.3s ease;
            z-index: 1;
        }
        .camera-container::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            border-radius: 12px;
            background: linear-gradient(45deg, var(--primary), var(--accent), var(--secondary));
            z-index: -1;
            opacity: 0.3;
            transition: opacity 0.3s ease;
        }
        .camera-container.active::before {
            opacity: 0.7;
            animation: borderPulse 3s infinite;
        }
        .video-feed {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .camera-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 1.5rem;
            background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
            transition: all 0.3s ease;
        }
        .greeting {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            color: var(--light);
            text-align: center;
            text-shadow: var(--neon-glow);
            letter-spacing: 1px;
            margin: 0;
        }
        .sidebar {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 2rem;
            min-width: 350px;
        }
        .card {
            background: rgba(10, 10, 26, 0.7);
            border-radius: 12px;
            padding: 1.8rem;
            border: 1px solid rgba(0, 247, 255, 0.2);
            box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 247, 255, 0.2);
        }
        .card h2 {
            font-family: 'Orbitron', sans-serif;
            color: var(--primary);
            margin-top: 0;
            border-bottom: 1px solid rgba(0, 247, 255, 0.3);
            padding-bottom: 0.8rem;
        }
        .attendance-list {
            max-height: 300px;
            overflow-y: auto;
            scrollbar-width: thin;
            scrollbar-color: var(--primary) var(--darker);
        }
        .attendance-list::-webkit-scrollbar {
            width: 6px;
        }
        .attendance-list::-webkit-scrollbar-thumb {
            background-color: var(--primary);
            border-radius: 3px;
        }
        .attendance-item {
            display: flex;
            justify-content: space-between;
            padding: 1rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            transition: all 0.2s ease;
        }
        .attendance-item:hover {
            background: rgba(0, 247, 255, 0.05);
            transform: translateX(5px);
        }
        .status-indicator {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 1rem;
        }
        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: var(--gray);
        }
        .status-dot.active {
            background-color: #00ff00;
            box-shadow: 0 0 10px #00ff00;
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 100;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.9);
            overflow: auto;
        }
        .modal-content {
            background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 100%);
            margin: 5% auto;
            padding: 2.5rem;
            border: 1px solid var(--primary);
            width: 60%;
            border-radius: 12px;
            box-shadow: 0 0 50px rgba(0, 247, 255, 0.3);
            position: relative;
            animation: modalFadeIn 0.4s;
        }
        .close-btn {
            position: absolute;
            top: 1rem;
            right: 1.5rem;
            color: var(--primary);
            font-size: 1.8rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .close-btn:hover {
            transform: rotate(90deg);
            color: var(--accent);
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--primary);
            font-family: 'Orbitron', sans-serif;
        }
        .form-control {
            width: 100%;
            padding: 0.8rem;
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(0, 247, 255, 0.3);
            border-radius: 6px;
            color: var(--light);
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        .form-control:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 10px rgba(0, 247, 255, 0.3);
        }
        .btn {
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border: none;
            color: var(--dark);
            padding: 1rem 2rem;
            border-radius: 6px;
            cursor: pointer;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 247, 255, 0.3);
        }
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 247, 255, 0.4);
        }
        .btn:disabled {
            background: var(--gray);
            transform: none;
            box-shadow: none;
            cursor: not-allowed;
        }
        .progress-container {
            margin: 1.5rem 0;
        }
        .progress-bar {
            height: 6px;
            background: rgba(0, 247, 255, 0.2);
            border-radius: 3px;
            overflow: hidden;
        }
        .progress {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            width: 0%;
            transition: width 0.3s ease;
        }
        .status-message {
            padding: 0.8rem;
            border-radius: 6px;
            margin: 0.5rem 0;
            display: none;
        }
        .success-message {
            background: rgba(0, 255, 0, 0.1);
            border: 1px solid rgba(0, 255, 0, 0.3);
            color: #00ff00;
        }
        .error-message {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid rgba(255, 0, 0, 0.3);
            color: #ff0000;
        }
        .particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
        }
        .particle {
            position: absolute;
            background: rgba(0, 247, 255, 0.5);
            border-radius: 50%;
            pointer-events: none;
        }
        @keyframes borderPulse {
            0% { opacity: 0.3; }
            50% { opacity: 0.7; }
            100% { opacity: 0.3; }
        }
        @keyframes modalFadeIn {
            from { opacity: 0; transform: translateY(-50px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }
        @media (max-width: 1024px) {
            .main-content { flex-direction: column; }
            .modal-content { width: 80%; }
        }
        @media (max-width: 768px) {
            .modal-content { width: 95%; padding: 1.5rem; }
        }
    </style>
</head>
<body>
    <div class="particles" id="particles"></div>
    
    <div class="header">
        <h1>NEURALGUARD</h1>
        <div id="datetime"></div>
    </div>

    <div class="main-content">
        <div class="camera-container" id="camera-container">
            <img class="video-feed" src="{{ url_for('video_feed') }}" alt="Live Feed">
            <div class="camera-overlay">
                <div class="greeting" id="greeting">AWAITING BIOMETRIC INPUT</div>
            </div>
        </div>

        <div class="sidebar">
            <div class="card">
                <h2>ACCESS LOG</h2>
                <div class="attendance-list" id="attendance-list">
                    <!-- Log items will be inserted here -->
                </div>
            </div>
            
            <div class="card">
                <h2>SYSTEM STATUS</h2>
                <div class="status-indicator">
                    <div class="status-dot {% if camera_connected %}active{% endif %}" id="camera-status"></div>
                    <span>Camera: {% if camera_connected %}Connected{% else %}Disconnected{% endif %}</span>
                </div>
                <div class="status-indicator">
                    <div class="status-dot {% if fingerprint_connected %}active{% endif %}" id="fingerprint-status"></div>
                    <span>Fingerprint: {% if fingerprint_connected %}Connected{% else %}Disconnected{% endif %}</span>
                </div>
                <div class="status-indicator">
                    <div class="status-dot {% if arduino_connected %}active{% endif %}" id="arduino-status"></div>
                    <span>Hardware: {% if arduino_connected %}Connected{% else %}Disconnected{% endif %}</span>
                </div>
                
                <div class="progress-container">
                    <div>Registered Profiles</div>
                    <div class="progress-bar">
                        <div class="progress" id="enrollment-progress" style="width: {{ enrollment_progress }}%"></div>
                    </div>
                    <div>{{ known_faces_count }} Faces / {{ fingerprint_count }} Fingerprints</div>
                </div>
                
                <button onclick="openEnrollmentModal()" class="btn">ENROLL NEW USER</button>
            </div>
        </div>
    </div>

    <!-- Enrollment Modal -->
    <div id="enrollment-modal" class="modal">
        <div class="modal-content">
            <span class="close-btn" onclick="closeEnrollmentModal()">&times;</span>
            <h2>NEW USER ENROLLMENT</h2>
            
            <div class="form-group">
                <label for="new-user-name">FULL NAME</label>
                <input type="text" id="new-user-name" class="form-control" placeholder="Enter full name">
            </div>
            
            <div class="form-group">
                <label>FACE CAPTURE</label>
                <button id="capture-face-btn" class="btn">CAPTURE FACE IMAGE</button>
                <div id="face-capture-status" class="status-message"></div>
            </div>
            
            <div class="form-group">
                <label>FINGERPRINT REGISTRATION</label>
                <button id="capture-fingerprint-btn" class="btn" {% if not fingerprint_connected %}disabled{% endif %}>
                    SCAN FINGERPRINT
                </button>
                <div id="fingerprint-status-message" class="status-message"></div>
                <div class="progress-container">
                    <div>Scan Progress</div>
                    <div class="progress-bar">
                        <div class="progress" id="fingerprint-progress" style="width: 0%"></div>
                    </div>
                </div>
            </div>
            
            <button id="complete-enrollment-btn" class="btn" disabled>COMPLETE ENROLLMENT</button>
            <div id="enrollment-status" class="status-message"></div>
        </div>
    </div>

    <script>
        // Particle effect
        const particlesContainer = document.getElementById('particles');
        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');
            particle.style.width = `${Math.random() * 5 + 1}px`;
            particle.style.height = particle.style.width;
            particle.style.left = `${Math.random() * 100}%`;
            particle.style.top = `${Math.random() * 100}%`;
            particle.style.opacity = Math.random() * 0.5 + 0.1;
            particle.style.animation = `pulse ${Math.random() * 5 + 3}s infinite`;
            particlesContainer.appendChild(particle);
        }

        // Update datetime
        function updateDateTime() {
            const now = new Date();
            const options = { 
                weekday: 'long', 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            };
            document.getElementById('datetime').textContent = now.toLocaleDateString('en-US', options);
        }
        setInterval(updateDateTime, 1000);
        updateDateTime();

        // Modal functions
        function openEnrollmentModal() {
            document.getElementById('enrollment-modal').style.display = 'block';
            resetEnrollmentForm();
        }
        
        function closeEnrollmentModal() {
            document.getElementById('enrollment-modal').style.display = 'none';
        }
        
        function resetEnrollmentForm() {
            document.getElementById('new-user-name').value = '';
            document.getElementById('face-capture-status').textContent = '';
            document.getElementById('face-capture-status').style.display = 'none';
            document.getElementById('fingerprint-status-message').textContent = '';
            document.getElementById('fingerprint-status-message').style.display = 'none';
            document.getElementById('fingerprint-progress').style.width = '0%';
            document.getElementById('complete-enrollment-btn').disabled = true;
            document.getElementById('enrollment-status').textContent = '';
            document.getElementById('enrollment-status').style.display = 'none';
        }

        // Face capture
        document.getElementById('capture-face-btn').addEventListener('click', async () => {
            const response = await fetch('/capture_face');
            const data = await response.json();
            
            const statusElement = document.getElementById('face-capture-status');
            statusElement.style.display = 'block';
            
            if (data.success) {
                statusElement.textContent = '✔ FACE CAPTURE SUCCESSFUL';
                statusElement.className = 'status-message success-message';
            } else {
                statusElement.textContent = '✖ FACE CAPTURE FAILED: ' + (data.message || 'Unknown error');
                statusElement.className = 'status-message error-message';
            }
            
            checkEnrollmentReady();
        });

        // Fingerprint capture
        document.getElementById('capture-fingerprint-btn').addEventListener('click', async () => {
            const statusElement = document.getElementById('fingerprint-status-message');
            const progressBar = document.getElementById('fingerprint-progress');
            
            statusElement.style.display = 'block';
            statusElement.textContent = '⌛ PLEASE PLACE YOUR FINGER ON THE SENSOR...';
            statusElement.className = 'status-message';
            
            try {
                // Simulate progress (in real app, you'd update this based on actual progress)
                for (let i = 0; i <= 100; i += 10) {
                    progressBar.style.width = `${i}%`;
                    await new Promise(resolve => setTimeout(resolve, 200));
                }
                
                const response = await fetch('/capture_fingerprint');
                const data = await response.json();
                
                if (data.success) {
                    statusElement.textContent = `✔ FINGERPRINT REGISTERED (ID: ${data.fingerprint_id})`;
                    statusElement.className = 'status-message success-message';
                } else {
                    statusElement.textContent = '✖ FINGERPRINT SCAN FAILED: ' + (data.message || 'Unknown error');
                    statusElement.className = 'status-message error-message';
                    progressBar.style.width = '0%';
                }
            } catch (error) {
                statusElement.textContent = '✖ CONNECTION ERROR: ' + error.message;
                statusElement.className = 'status-message error-message';
                progressBar.style.width = '0%';
            }
            
            checkEnrollmentReady();
        });

        // Check if enrollment can be completed
        function checkEnrollmentReady() {
            const faceCaptured = document.getElementById('face-capture-status').textContent.includes('✔');
            const fingerprintCaptured = document.getElementById('fingerprint-status-message').textContent.includes('✔');
            const nameEntered = document.getElementById('new-user-name').value.trim().length > 0;
            
            document.getElementById('complete-enrollment-btn').disabled = !(faceCaptured && fingerprintCaptured && nameEntered);
        }

        // Complete enrollment
        document.getElementById('complete-enrollment-btn').addEventListener('click', async () => {
            const name = document.getElementById('new-user-name').value.trim();
            const statusElement = document.getElementById('enrollment-status');
            
            statusElement.style.display = 'block';
            statusElement.textContent = '⌛ PROCESSING ENROLLMENT...';
            statusElement.className = 'status-message';
            
            try {
                const response = await fetch('/complete_enrollment', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: name })
                });
                
                const data = await response.json();
                if (data.success) {
                    statusElement.textContent = '✔ ENROLLMENT COMPLETED SUCCESSFULLY';
                    statusElement.className = 'status-message success-message';
                    
                    // Update UI after delay
                    setTimeout(() => {
                        closeEnrollmentModal();
                        window.location.reload();
                    }, 1500);
                } else {
                    statusElement.textContent = '✖ ENROLLMENT FAILED: ' + (data.message || 'Unknown error');
                    statusElement.className = 'status-message error-message';
                }
            } catch (error) {
                statusElement.textContent = '✖ NETWORK ERROR: ' + error.message;
                statusElement.className = 'status-message error-message';
            }
        });

        // Update detection status
        function updateDetection() {
            fetch('/get_last_detected')
                .then(response => response.json())
                .then(data => {
                    if (data.name) {
                        const greeting = document.getElementById('greeting');
                        const cameraContainer = document.getElementById('camera-container');
                        
                        greeting.textContent = `ACCESS GRANTED: ${data.name.toUpperCase()}`;
                        cameraContainer.classList.add('active');
                        
                        // Add to attendance list
                        const now = new Date();
                        const listItem = document.createElement('div');
                        listItem.className = 'attendance-item';
                        listItem.innerHTML = `
                            <span>${data.name.toUpperCase()}</span>
                            <span>${now.toLocaleTimeString()}</span>
                        `;
                        document.getElementById('attendance-list').prepend(listItem);
                        
                        // Reset after delay
                        setTimeout(() => {
                            greeting.textContent = 'AWAITING BIOMETRIC INPUT';
                            cameraContainer.classList.remove('active');
                        }, 5000);
                    }
                });
        }
        setInterval(updateDetection, 1000);

        // Check hardware status
        function checkHardwareStatus() {
            fetch('/hardware_status')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('camera-status').className = 
                        `status-dot ${data.camera_connected ? 'active' : ''}`;
                    document.getElementById('fingerprint-status').className = 
                        `status-dot ${data.fingerprint_connected ? 'active' : ''}`;
                    document.getElementById('arduino-status').className = 
                        `status-dot ${data.arduino_connected ? 'active' : ''}`;
                });
        }
        setInterval(checkHardwareStatus, 5000);
    </script>
</body>
</html>
"""
import os
import cv2
import csv
import time
import serial
import numpy as np
import face_recognition
from datetime import datetime
from ultralytics import YOLO
from flask import Flask, render_template_string, Response, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from importlib.metadata import files
import threading
import hashlib
from collections import deque

# Enhanced fingerprint handling with retry logic
try:
    from pyfingerprint.pyfingerprint import PyFingerprint, FINGERPRINT_CHARBUFFER1, FINGERPRINT_CHARBUFFER2
    FINGERPRINT_ENABLED = True
except ImportError:
    FINGERPRINT_ENABLED = False

app = Flask(__name__)

# ===== CONFIGURATION =====
BASE_DIR = os.path.expanduser("~/Desktop/server_CMRL")
KNOWN_FACE_PATHS = {
    "sam": os.path.join(BASE_DIR, "image_path/sam.jpeg"),
    "yuthish": os.path.join(BASE_DIR, "image_path/yuthis.jpeg"),
    "sai": os.path.join(BASE_DIR, "image_path/sai.jpeg")
}
LOG_FILE = os.path.join(BASE_DIR, "attendance_log/attendance_log.csv")
FINGERPRINT_DB = os.path.join(BASE_DIR, "fingerprint_db.csv")
MODEL_PATH = "yolov8n.pt"
CAMERA_INDEX = 0
FINGERPRINT_SENSOR_PORT = '/dev/ttyACM0'
FINGERPRINT_BAUDRATE = 57600
FINGERPRINT_ENROLLMENT_TIMEOUT = 30  # seconds
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Create required directories
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
os.makedirs(os.path.dirname(FINGERPRINT_DB), exist_ok=True)
for path in KNOWN_FACE_PATHS.values():
    os.makedirs(os.path.dirname(path), exist_ok=True)

# Initialize hardware connections
try:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2)
    ARDUINO_CONNECTED = True
except Exception as e:
    ARDUINO_CONNECTED = False
    print(f"Arduino connection error: {str(e)}")

# Enhanced fingerprint initialization with retry logic
FINGERPRINT_CONNECTED = False
if FINGERPRINT_ENABLED:
    for attempt in range(3):
        try:
            fingerprint = PyFingerprint(FINGERPRINT_SENSOR_PORT, FINGERPRINT_BAUDRATE)
            if fingerprint.verifyPassword():
                FINGERPRINT_CONNECTED = True
                print("Fingerprint sensor initialized successfully")
                break
            else:
                print("Fingerprint sensor password verification failed")
        except Exception as e:
            print(f"Fingerprint sensor initialization attempt {attempt + 1} failed: {str(e)}")
            time.sleep(2)
    else:
        print("Failed to initialize fingerprint sensor after 3 attempts")
        

# ===== BIOMETRIC SYSTEM CLASS =====
class BiometricSystem:
    def __init__(self):
        self.known_faces = self.load_known_faces()
        self.fingerprint_db = self.load_fingerprint_db()
        self.model = self.load_yolo_model()
        self.camera = self.initialize_camera()
        self.logged_names = set()
        self.last_detected = None
        self.last_detection_time = 0
        self.enrollment_data = {
            'face_image': None,
            'fingerprint_template': None,
            'name': None,
            'fingerprint_id': None
        }
        self.detection_history = deque(maxlen=10)
        self.lock = threading.Lock()
        self.fingerprint_cache = {}
        self.system_status = {
            'camera': self.camera is not None,
            'fingerprint': FINGERPRINT_CONNECTED,
            'arduino': ARDUINO_CONNECTED,
            'last_check': time.time()
        }

    def load_known_faces(self):
        known_faces = {}
        for name, path in KNOWN_FACE_PATHS.items():
            if not os.path.exists(path):
                continue
            try:
                image = face_recognition.load_image_file(path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    known_faces[name] = encodings[0]
                    print(f"Loaded face encoding for {name}")
                else:
                    print(f"No faces found in {path}")
            except Exception as e:
                print(f"Error loading {path}: {str(e)}")
        return known_faces

    def load_fingerprint_db(self):
        fingerprint_db = {}
        if os.path.exists(FINGERPRINT_DB):
            try:
                with open(FINGERPRINT_DB, mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if len(row) >= 2:
                            fingerprint_db[int(row[0])] = row[1]
                print(f"Loaded {len(fingerprint_db)} fingerprint mappings")
            except Exception as e:
                print(f"Error loading fingerprint DB: {str(e)}")
        return fingerprint_db

    def save_fingerprint_db(self):
        try:
            with open(FINGERPRINT_DB, mode='w', newline='') as file:
                writer = csv.writer(file)
                for fid, name in self.fingerprint_db.items():
                    writer.writerow([fid, name])
        except Exception as e:
            print(f"Error saving fingerprint DB: {str(e)}")

    def load_yolo_model(self):
        if not os.path.exists(MODEL_PATH):
            print("Downloading YOLOv8n model...")
            os.system(f"wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt -O {MODEL_PATH}")
        return YOLO(MODEL_PATH)

    def initialize_camera(self):
        for i in range(3):
            try:
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    print(f"Camera found at index {i}")
                    global CAMERA_INDEX
                    CAMERA_INDEX = i
                    return cap
            except Exception as e:
                print(f"Error opening camera index {i}: {str(e)}")
        
        print("Warning: No camera found - running in demo mode")
        return None

    def check_hardware_status(self):
        current_time = time.time()
        if current_time - self.system_status['last_check'] > 5:  # Check every 5 seconds
            self.system_status['camera'] = self.camera is not None and self.camera.isOpened()
            self.system_status['arduino'] = ARDUINO_CONNECTED
            
            if FINGERPRINT_ENABLED:
                try:
                    self.system_status['fingerprint'] = fingerprint.verifyPassword()
                except:
                    self.system_status['fingerprint'] = False
            
            self.system_status['last_check'] = current_time
        return self.system_status

    def capture_face_for_enrollment(self):
        if not self.camera:
            return {'success': False, 'message': 'Camera not available'}
        
        try:
            ret, frame = self.camera.read()
            if not ret:
                return {'success': False, 'message': 'Failed to capture frame'}
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            
            if not face_locations:
                return {'success': False, 'message': 'No face detected in frame'}
            
            if len(face_locations) > 1:
                return {'success': False, 'message': 'Multiple faces detected'}
            
            self.enrollment_data['face_image'] = frame
            return {'success': True, 'face_count': len(face_locations)}
        except Exception as e:
            return {'success': False, 'message': str(e)}

    def enroll_fingerprint(self):
        if not FINGERPRINT_CONNECTED:
            return {'success': False, 'message': 'Fingerprint sensor not connected'}
        
        start_time = time.time()
        try:
            print("Waiting for finger...")
            
            # Wait for finger with timeout
            while time.time() - start_time < FINGERPRINT_ENROLLMENT_TIMEOUT:
                try:
                    if fingerprint.readImage():
                        break
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Read image error: {str(e)}")
                    time.sleep(1)
            else:
                return {'success': False, 'message': 'Finger not detected (timeout)'}
            
            # Convert and check quality
            fingerprint.convertImage(FINGERPRINT_CHARBUFFER1)
            
            # Check if fingerprint already exists
            result = fingerprint.searchTemplate()
            if result[0] >= 0:
                existing_name = self.fingerprint_db.get(result[0], "Unknown")
                return {
                    'success': False, 
                    'message': f'Fingerprint already exists (ID: {result[0]}, Name: {existing_name})'
                }
            
            # Wait for finger to be removed
            print("Please remove finger")
            time.sleep(2)
            
            # Get second reading
            print("Place same finger again")
            for _ in range(int(FINGERPRINT_ENROLLMENT_TIMEOUT / 0.5)):
                try:
                    if fingerprint.readImage():
                        break
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Second read error: {str(e)}")
                    time.sleep(1)
            else:
                return {'success': False, 'message': 'Second reading failed (timeout)'}
            
            # Convert second image
            fingerprint.convertImage(FINGERPRINT_CHARBUFFER2)
            
            # Compare both fingerprints
            if not fingerprint.compareCharacteristics():
                return {'success': False, 'message': 'Fingerprints do not match'}
            
            # Create and store template
            fingerprint.createTemplate()
            position = fingerprint.storeTemplate()
            
            # Get template for local storage
            fingerprint.downloadTemplate(position, FINGERPRINT_CHARBUFFER1)
            template = fingerprint.downloadCharacteristics(FINGERPRINT_CHARBUFFER1)
            template_hash = hashlib.sha256(str(template).encode()).hexdigest()
            
            with self.lock:
                self.enrollment_data['fingerprint_id'] = position
                self.enrollment_data['fingerprint_template'] = template_hash
            
            return {
                'success': True, 
                'fingerprint_id': position,
                'template_hash': template_hash
            }
        except Exception as e:
            return {'success': False, 'message': str(e)}

    def verify_fingerprint(self):
        if not FINGERPRINT_CONNECTED:
            return None
        
        try:
            # Check cache first
            cached_result = self.check_fingerprint_cache()
            if cached_result:
                return cached_result
            
            # Read fingerprint
            if not fingerprint.readImage():
                return None
            
            fingerprint.convertImage(FINGERPRINT_CHARBUFFER1)
            result = fingerprint.searchTemplate()
            
            if result[0] >= 0:
                # Update cache
                self.fingerprint_cache[result[0]] = time.time()
                return result[0]
            return None
        except Exception as e:
            print(f"Fingerprint verification error: {str(e)}")
            return None

    def check_fingerprint_cache(self, fid=None):
        current_time = time.time()
        if fid:
            # Check specific fingerprint in cache
            return fid in self.fingerprint_cache and current_time - self.fingerprint_cache[fid] < 30
        else:
            # Check all cached fingerprints
            for fid, timestamp in list(self.fingerprint_cache.items()):
                if current_time - timestamp > 30:  # 30 second cache timeout
                    del self.fingerprint_cache[fid]
            return None

    def complete_enrollment(self, name):
        try:
            if not name or not name.strip():
                return {'success': False, 'message': 'Name is required'}
            
            name = name.strip()
            
            # Validate enrollment data
            if not self.enrollment_data['face_image']:
                return {'success': False, 'message': 'No face image captured'}
            
            if self.enrollment_data['fingerprint_id'] is None:
                return {'success': False, 'message': 'No fingerprint captured'}
            
            # Save face image
            face_path = os.path.join(BASE_DIR, f"image_path/{name.lower()}.jpeg")
            cv2.imwrite(face_path, self.enrollment_data['face_image'])
            
            # Update known faces
            image = face_recognition.load_image_file(face_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                self.known_faces[name] = encodings[0]
            
            # Update fingerprint DB
            with self.lock:
                self.fingerprint_db[self.enrollment_data['fingerprint_id']] = name
                self.save_fingerprint_db()
            
            # Reset enrollment data
            self.enrollment_data = {
                'face_image': None,
                'fingerprint_template': None,
                'name': None,
                'fingerprint_id': None
            }
            
            return {'success': True}
        except Exception as e:
            return {'success': False, 'message': str(e)}

    def verify_face(self, frame):
        try:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    list(self.known_faces.values()), 
                    face_encoding,
                    tolerance=0.4
                )
                
                if True in matches:
                    index = matches.index(True)
                    name = list(self.known_faces.keys())[index]
                    return name
            return None
        except Exception as e:
            print(f"Face verification error: {str(e)}")
            return None

    def process_frame(self):
        if not self.camera:
            # Generate demo frame
            frame = np.zeros((480, 640, 3), dtype=np.uint8)
            cv2.putText(frame, "DEMO MODE: NO CAMERA", (50, 240), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes(), None

        try:
            ret, frame = self.camera.read()
            if not ret:
                print("Failed to capture frame")
                return None, None

            current_name = None
            results = self.model(frame, verbose=False)

            for r in results:
                for box in r.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cropped = frame[y1:y2, x1:x2]

                    name = self.verify_face(cropped)
                    if name:
                        current_name = name
                        cv2.putText(frame, f"VERIFIED: {name.upper()}", (x1, y1 - 40), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                        self.last_detected = name
                        self.last_detection_time = time.time()
                        
                        if name not in self.logged_names:
                            self.log_attendance(name)
                            self.logged_names.add(name)
                            if ARDUINO_CONNECTED:
                                try:
                                    arduino.write(b'G')  # Signal success to Arduino
                                except:
                                    ARDUINO_CONNECTED = False
                        
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, name if name else "UNKNOWN", (x1, y1 - 10), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes(), current_name
        except Exception as e:
            print(f"Frame processing error: {str(e)}")
            return None, None

    def log_attendance(self, name):
        try:
            with open(LOG_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    name, 
                    datetime.now().strftime("%Y-%m-%d"),
                    datetime.now().strftime("%H:%M:%S"),
                    "FACE"  # Authentication method
                ])
            self.detection_history.append({
                'name': name,
                'time': datetime.now().strftime("%H:%M:%S"),
                'method': 'Face'
            })
        except Exception as e:
            print(f"Error writing to log file: {str(e)}")

    def log_fingerprint_attendance(self, fingerprint_id):
        name = self.fingerprint_db.get(fingerprint_id, f"Unknown (ID: {fingerprint_id})")
        try:
            with open(LOG_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    name, 
                    datetime.now().strftime("%Y-%m-%d"),
                    datetime.now().strftime("%H:%M:%S"),
                    "FINGERPRINT"
                ])
            self.detection_history.append({
                'name': name,
                'time': datetime.now().strftime("%H:%M:%S"),
                'method': 'Fingerprint'
            })
        except Exception as e:
            print(f"Error writing fingerprint log: {str(e)}")

    def get_recent_detections(self, count=5):
        return list(self.detection_history)[-count:]

# Initialize the biometric system
system = BiometricSystem()

# ===== FLASK ROUTES =====
@app.route('/')
def index():
    fingerprint_count = 0
    if FINGERPRINT_CONNECTED:
        try:
            fingerprint_count = fingerprint.getTemplateCount()
        except:
            pass
    
    hardware_status = system.check_hardware_status()
    
    return render_template_string(HTML_TEMPLATE, 
                               known_faces_count=len(system.known_faces),
                               fingerprint_count=fingerprint_count,
                               enrollment_progress=min(100, len(system.known_faces) * 10),
                               camera_connected=hardware_status['camera'],
                               fingerprint_connected=hardware_status['fingerprint'],
                               arduino_connected=hardware_status['arduino'])

@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
            frame, name = system.process_frame()
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture_face')
def capture_face():
    result = system.capture_face_for_enrollment()
    return jsonify(result)

@app.route('/capture_fingerprint')
def capture_fingerprint():
    result = system.enroll_fingerprint()
    return jsonify(result)

@app.route('/complete_enrollment', methods=['POST'])
def complete_enrollment():
    name = request.json.get('name', '').strip()
    result = system.complete_enrollment(name)
    return jsonify(result)

@app.route('/get_last_detected')
def get_last_detected():
    if time.time() - system.last_detection_time > 5:
        system.last_detected = None
    
    return jsonify({
        'name': system.last_detected,
        'timestamp': system.last_detection_time
    })

@app.route('/hardware_status')
def hardware_status():
    status = system.check_hardware_status()
    return jsonify(status)

@app.route('/get_attendance_log')
def get_attendance_log():
    try:
        with open(LOG_FILE, mode='r') as file:
            reader = csv.reader(file)
            log_data = list(reader)
        return jsonify({'success': True, 'log': log_data[-10:]})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/get_recent_detections')
def get_recent_detections():
    return jsonify({
        'success': True,
        'detections': system.get_recent_detections()
    })

@app.route('/verify_fingerprint')
def verify_fingerprint():
    fid = system.verify_fingerprint()
    if fid is not None:
        system.log_fingerprint_attendance(fid)
        if ARDUINO_CONNECTED:
            try:
                arduino.write(b'G')
            except:
                ARDUINO_CONNECTED = False
        return jsonify({
            'success': True,
            'fingerprint_id': fid,
            'name': system.fingerprint_db.get(fid, f"Unknown (ID: {fid})")
        })
    return jsonify({'success': False, 'message': 'No matching fingerprint found'})

@app.route('/list_fingerprints')
def list_fingerprints():
    if not FINGERPRINT_CONNECTED:
        return jsonify({'success': False, 'message': 'Fingerprint sensor not connected'})
    
    try:
        count = fingerprint.getTemplateCount()
        fingerprints = []
        for position in range(count):
            try:
                fingerprint.loadTemplate(position, FINGERPRINT_CHARBUFFER1)
                name = system.fingerprint_db.get(position, "Unknown")
                fingerprints.append({
                    'id': position,
                    'name': name
                })
            except:
                continue
        return jsonify({
            'success': True,
            'count': count,
            'fingerprints': fingerprints
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/delete_fingerprint/<int:fingerprint_id>', methods=['DELETE'])
def delete_fingerprint(fingerprint_id):
    if not FINGERPRINT_CONNECTED:
        return jsonify({'success': False, 'message': 'Fingerprint sensor not connected'})
    
    try:
        if fingerprint.deleteTemplate(fingerprint_id):
            with system.lock:
                if fingerprint_id in system.fingerprint_db:
                    del system.fingerprint_db[fingerprint_id]
                    system.save_fingerprint_db()
            return jsonify({'success': True})
        return jsonify({'success': False, 'message': 'Failed to delete template'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_face', methods=['POST'])
def upload_face():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        name = request.form.get('name', '').strip()
        if not name:
            return jsonify({'success': False, 'message': 'Name is required'})
        
        try:
            # Save the file temporarily
            temp_path = os.path.join(BASE_DIR, "temp_upload.jpg")
            file.save(temp_path)
            
            # Process the image
            image = face_recognition.load_image_file(temp_path)
            encodings = face_recognition.face_encodings(image)
            
            if not encodings:
                os.remove(temp_path)
                return jsonify({'success': False, 'message': 'No face detected in image'})
            
            if len(encodings) > 1:
                os.remove(temp_path)
                return jsonify({'success': False, 'message': 'Multiple faces detected'})
            
            # Save to known faces
            face_path = os.path.join(BASE_DIR, f"image_path/{name.lower()}.jpeg")
            cv2.imwrite(face_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
            system.known_faces[name] = encodings[0]
            
            os.remove(temp_path)
            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
    
    return jsonify({'success': False, 'message': 'Invalid file type'})

def cleanup():
    if system.camera:
        system.camera.release()
    if ARDUINO_CONNECTED:
        arduino.close()
    print("System resources cleaned up")

if __name__ == '__main__':
    try:
        # Start hardware status monitoring thread
        def hardware_monitor():
            while True:
                system.check_hardware_status()
                time.sleep(5)
        
        monitor_thread = threading.Thread(target=hardware_monitor, daemon=True)
        monitor_thread.start()
        
        # Start the Flask app
        app.run(host='0.0.0.0', port=5000, threaded=True)
    finally:
        cleanup()

# HTML Template 