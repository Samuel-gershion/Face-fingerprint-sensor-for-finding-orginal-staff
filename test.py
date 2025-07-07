# ===== FUTURISTIC UI TEMPLATE =====
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus Biometric System | CMRL</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #00f0ff;
            --primary-dark: #0077ff;
            --secondary: #ff2d75;
            --dark: #0a0a1a;
            --darker: #050510;
            --light: #e0e0ff;
            --success: #00ff88;
            --warning: #ffaa00;
            --danger: #ff3860;
            --card-bg: rgba(10, 20, 40, 0.6);
            --glow: 0 0 10px rgba(0, 240, 255, 0.7);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--dark);
            color: var(--light);
            background-image: 
                radial-gradient(circle at 20% 30%, rgba(0, 112, 255, 0.1) 0%, transparent 30%),
                radial-gradient(circle at 80% 70%, rgba(255, 45, 117, 0.1) 0%, transparent 30%);
            min-height: 100vh;
            overflow-x: hidden;
        }

        h1, h2, h3, h4, .tech-font {
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 1px;
            font-weight: 500;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            border-bottom: 1px solid rgba(0, 240, 255, 0.2);
            margin-bottom: 30px;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--glow);
        }

        .logo-text h1 {
            font-size: 1.8rem;
            background: linear-gradient(to right, var(--primary), var(--light));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-bottom: 5px;
        }

        .logo-text span {
            font-size: 0.9rem;
            color: rgba(224, 224, 255, 0.7);
            letter-spacing: 2px;
        }

        .status-bar {
            display: flex;
            gap: 20px;
        }

        .status-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.9rem;
        }

        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: var(--danger);
            box-shadow: 0 0 5px var(--danger);
        }

        .status-indicator.active {
            background-color: var(--success);
            box-shadow: 0 0 5px var(--success);
        }

        .status-indicator.warning {
            background-color: var(--warning);
            box-shadow: 0 0 5px var(--warning);
        }

        .main-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }

        @media (max-width: 1024px) {
            .main-grid {
                grid-template-columns: 1fr;
            }
        }

        .card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 25px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 240, 255, 0.1);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .card:hover {
            border-color: rgba(0, 240, 255, 0.3);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
            transform: translateY(-5px);
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .card-title {
            font-size: 1.3rem;
            color: var(--primary);
        }

        .card-badge {
            background: rgba(0, 240, 255, 0.1);
            color: var(--primary);
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .video-container {
            position: relative;
            width: 100%;
            height: 400px;
            border-radius: 8px;
            overflow: hidden;
            background-color: #000;
        }

        .video-feed {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .video-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 15px;
            background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .detection-status {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .detection-indicator {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: var(--danger);
            animation: pulse 2s infinite;
        }

        .detection-indicator.active {
            background-color: var(--success);
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.3; }
            100% { opacity: 1; }
        }

        .detection-text {
            font-size: 0.9rem;
        }

        .detection-name {
            font-weight: bold;
            color: var(--primary);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-bottom: 25px;
        }

        .stat-card {
            background: rgba(0, 10, 30, 0.5);
            border-radius: 8px;
            padding: 15px;
            text-align: center;
            border: 1px solid rgba(0, 240, 255, 0.1);
        }

        .stat-value {
            font-size: 2rem;
            font-weight: bold;
            background: linear-gradient(to right, var(--primary), var(--light));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin: 10px 0;
        }

        .stat-label {
            font-size: 0.8rem;
            color: rgba(224, 224, 255, 0.7);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .progress-container {
            margin: 20px 0;
        }

        .progress-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            font-size: 0.9rem;
        }

        .progress-bar {
            height: 8px;
            background: rgba(0, 240, 255, 0.1);
            border-radius: 4px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(to right, var(--primary), var(--primary-dark));
            border-radius: 4px;
            width: {{ enrollment_progress }}%;
            transition: width 0.5s ease;
            position: relative;
            overflow: hidden;
        }

        .progress-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(255, 255, 255, 0.3) 50%, 
                transparent 100%);
            animation: shimmer 2s infinite;
        }

        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }

        .activity-log {
            max-height: 300px;
            overflow-y: auto;
            padding-right: 10px;
        }

        .activity-item {
            display: flex;
            gap: 15px;
            padding: 12px 0;
            border-bottom: 1px solid rgba(0, 240, 255, 0.1);
        }

        .activity-item:last-child {
            border-bottom: none;
        }

        .activity-icon {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(0, 240, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .activity-details {
            flex-grow: 1;
        }

        .activity-name {
            font-weight: 500;
            margin-bottom: 3px;
        }

        .activity-meta {
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            color: rgba(224, 224, 255, 0.7);
        }

        .activity-method {
            background: rgba(0, 240, 255, 0.1);
            color: var(--primary);
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 0.7rem;
        }

        .tabs {
            display: flex;
            border-bottom: 1px solid rgba(0, 240, 255, 0.2);
            margin-bottom: 20px;
        }

        .tab {
            padding: 10px 20px;
            cursor: pointer;
            position: relative;
            color: rgba(224, 224, 255, 0.7);
            font-size: 0.9rem;
        }

        .tab.active {
            color: var(--primary);
        }

        .tab.active::after {
            content: '';
            position: absolute;
            bottom: -1px;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
            border: none;
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 1px;
            font-size: 0.9rem;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: var(--darker);
            box-shadow: 0 2px 10px rgba(0, 240, 255, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 240, 255, 0.4);
        }

        .btn-secondary {
            background: rgba(0, 240, 255, 0.1);
            color: var(--primary);
            border: 1px solid rgba(0, 240, 255, 0.3);
        }

        .btn-secondary:hover {
            background: rgba(0, 240, 255, 0.2);
            border-color: rgba(0, 240, 255, 0.5);
        }

        .btn-danger {
            background: rgba(255, 56, 96, 0.1);
            color: var(--danger);
            border: 1px solid rgba(255, 56, 96, 0.3);
        }

        .btn-danger:hover {
            background: rgba(255, 56, 96, 0.2);
            border-color: rgba(255, 56, 96, 0.5);
        }

        .btn-group {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: rgba(224, 224, 255, 0.9);
        }

        .form-control {
            width: 100%;
            padding: 12px 15px;
            background: rgba(10, 20, 40, 0.5);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 6px;
            color: var(--light);
            font-family: 'Roboto', sans-serif;
            transition: all 0.2s ease;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(0, 240, 255, 0.2);
        }

        .file-upload {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 30px;
            border: 2px dashed rgba(0, 240, 255, 0.3);
            border-radius: 8px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
            margin-bottom: 20px;
        }

        .file-upload:hover {
            border-color: var(--primary);
            background: rgba(0, 240, 255, 0.05);
        }

        .file-upload-icon {
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 10px;
        }

        .file-upload-text {
            font-size: 0.9rem;
            color: rgba(224, 224, 255, 0.7);
            margin-bottom: 5px;
        }

        .file-upload-hint {
            font-size: 0.8rem;
            color: rgba(224, 224, 255, 0.5);
        }

        .fingerprint-list {
            max-height: 300px;
            overflow-y: auto;
            margin-top: 20px;
        }

        .fingerprint-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 15px;
            background: rgba(10, 20, 40, 0.3);
            border-radius: 6px;
            margin-bottom: 10px;
            border: 1px solid rgba(0, 240, 255, 0.1);
        }

        .fingerprint-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .fingerprint-icon {
            color: var(--primary);
        }

        .fingerprint-id {
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 1px;
            color: var(--primary);
        }

        .fingerprint-name {
            font-weight: 500;
        }

        .modal {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(5, 5, 16, 0.9);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
            backdrop-filter: blur(5px);
        }

        .modal.active {
            opacity: 1;
            pointer-events: all;
        }

        .modal-content {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 30px;
            max-width: 500px;
            width: 90%;
            border: 1px solid rgba(0, 240, 255, 0.2);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            transform: translateY(20px);
            transition: transform 0.3s ease;
            position: relative;
        }

        .modal.active .modal-content {
            transform: translateY(0);
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .modal-title {
            font-size: 1.5rem;
            color: var(--primary);
        }

        .modal-close {
            background: none;
            border: none;
            color: rgba(224, 224, 255, 0.7);
            font-size: 1.5rem;
            cursor: pointer;
            transition: color 0.2s ease;
        }

        .modal-close:hover {
            color: var(--primary);
        }

        .modal-body {
            margin-bottom: 25px;
        }

        .modal-footer {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
        }

        .enrollment-steps {
            display: flex;
            justify-content: space-between;
            margin-bottom: 30px;
            position: relative;
        }

        .enrollment-steps::before {
            content: '';
            position: absolute;
            top: 15px;
            left: 0;
            right: 0;
            height: 2px;
            background: rgba(0, 240, 255, 0.2);
            z-index: 1;
        }

        .step {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            z-index: 2;
        }

        .step-number {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: rgba(0, 240, 255, 0.1);
            color: rgba(224, 224, 255, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 8px;
            border: 2px solid rgba(0, 240, 255, 0.2);
            transition: all 0.3s ease;
        }

        .step.active .step-number {
            background: var(--primary-dark);
            color: var(--light);
            border-color: var(--primary);
            box-shadow: 0 0 10px rgba(0, 112, 255, 0.5);
        }

        .step.completed .step-number {
            background: var(--success);
            color: var(--darker);
            border-color: var(--success);
        }

        .step-label {
            font-size: 0.8rem;
            color: rgba(224, 224, 255, 0.7);
            text-align: center;
        }

        .step.active .step-label {
            color: var(--primary);
        }

        .step.completed .step-label {
            color: var(--success);
        }

        .alert {
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .alert-success {
            background: rgba(0, 255, 136, 0.1);
            border: 1px solid rgba(0, 255, 136, 0.3);
            color: var(--success);
        }

        .alert-danger {
            background: rgba(255, 56, 96, 0.1);
            border: 1px solid rgba(255, 56, 96, 0.3);
            color: var(--danger);
        }

        .alert-warning {
            background: rgba(255, 170, 0, 0.1);
            border: 1px solid rgba(255, 170, 0, 0.3);
            color: var(--warning);
        }

        .alert-info {
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid rgba(0, 240, 255, 0.3);
            color: var(--primary);
        }

        .scan-animation {
            position: relative;
            width: 100%;
            height: 200px;
            background: rgba(0, 10, 30, 0.5);
            border-radius: 8px;
            overflow: hidden;
            margin: 20px 0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }

        .scan-line {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(to right, 
                transparent, 
                var(--primary), 
                transparent);
            box-shadow: 0 0 10px var(--primary);
            animation: scan 3s infinite ease-in-out;
        }

        @keyframes scan {
            0% { top: 0; }
            100% { top: 100%; }
        }

        .scan-text {
            color: var(--primary);
            margin-top: 20px;
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 2px;
        }

        .fingerprint-icon-large {
            font-size: 4rem;
            color: rgba(0, 240, 255, 0.3);
        }

        .face-preview {
            width: 150px;
            height: 150px;
            border-radius: 8px;
            background: rgba(0, 10, 30, 0.5);
            margin: 0 auto 20px;
            overflow: hidden;
            border: 2px solid rgba(0, 240, 255, 0.2);
        }

        .face-preview img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .no-face {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: rgba(224, 224, 255, 0.5);
        }

        .terminal {
            background: rgba(0, 5, 15, 0.8);
            border-radius: 8px;
            padding: 15px;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            color: var(--primary);
            height: 200px;
            overflow-y: auto;
            margin-top: 20px;
            border: 1px solid rgba(0, 240, 255, 0.2);
        }

        .terminal-line {
            margin-bottom: 5px;
            line-height: 1.4;
        }

        .terminal-prompt {
            color: var(--success);
        }

        .terminal-command {
            color: var(--light);
        }

        .terminal-output {
            color: rgba(224, 224, 255, 0.7);
        }

        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(0, 240, 255, 0.3);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 240, 255, 0.5);
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        .floating {
            animation: float 3s ease-in-out infinite;
        }

        .grid-bg {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: 
                linear-gradient(rgba(0, 240, 255, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 240, 255, 0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            z-index: -1;
        }

        .particles {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: -1;
            overflow: hidden;
        }

        .particle {
            position: absolute;
            background: rgba(0, 240, 255, 0.3);
            border-radius: 50%;
            pointer-events: none;
        }

        @media (max-width: 768px) {
            .main-grid {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
            
            header {
                flex-direction: column;
                align-items: flex-start;
                gap: 15px;
            }
            
            .status-bar {
                width: 100%;
                justify-content: space-between;
            }
        }
    </style>
</head>
<body>
    <div class="grid-bg"></div>
    <div class="particles" id="particles"></div>
    
    <div class="container">
        <header>
            <div class="logo">
                <div class="logo-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 2L3 7L12 12L21 7L12 2Z" fill="white" stroke="var(--darker)" stroke-width="2"/>
                        <path d="M3 12L12 17L21 12" stroke="white" stroke-width="2"/>
                        <path d="M3 17L12 22L21 17" stroke="white" stroke-width="2"/>
                    </svg>
                </div>
                <div class="logo-text">
                    <h1>NEXUS BIOMETRICS</h1>
                    <span>CMRL ATTENDANCE SYSTEM</span>
                </div>
            </div>
            <div class="status-bar">
                <div class="status-item">
                    <div class="status-indicator {% if camera_connected %}active{% endif %}"></div>
                    <span>Camera</span>
                </div>
                <div class="status-item">
                    <div class="status-indicator {% if fingerprint_connected %}active{% else %}warning{% endif %}"></div>
                    <span>Fingerprint</span>
                </div>
                <div class="status-item">
                    <div class="status-indicator {% if arduino_connected %}active{% else %}warning{% endif %}"></div>
                    <span>Access Control</span>
                </div>
            </div>
        </header>

        <div class="main-grid">
            <div class="card">
                <div class="card-header">
                    <h3 class="card-title">LIVE RECOGNITION</h3>
                    <div class="card-badge">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="12" cy="12" r="5" fill="var(--primary)"/>
                        </svg>
                        ACTIVE
                    </div>
                </div>
                <div class="video-container">
                    <img class="video-feed" src="{{ url_for('video_feed') }}">
                    <div class="video-overlay">
                        <div class="detection-status">
                            <div class="detection-indicator"></div>
                            <span class="detection-text">AWAITING DETECTION</span>
                        </div>
                        <div class="detection-name" id="detection-name">-</div>
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <h3 class="card-title">SYSTEM DASHBOARD</h3>
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-label">Registered Faces</div>
                        <div class="stat-value">{{ known_faces_count }}</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Fingerprints</div>
                        <div class="stat-value">{{ fingerprint_count }}</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Today's Logs</div>
                        <div class="stat-value" id="today-logs">-</div>
                    </div>
                </div>
                <div class="progress-container">
                    <div class="progress-label">
                        <span>System Enrollment Progress</span>
                        <span>{{ enrollment_progress }}%</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {{ enrollment_progress }}%;"></div>
                    </div>
                </div>
                <div class="card-header" style="margin-top: 25px;">
                    <h3 class="card-title">RECENT ACTIVITY</h3>
                </div>
                <div class="activity-log" id="activity-log">
                    <!-- Activity items will be inserted here by JavaScript -->
                </div>
            </div>
        </div>

        <div class="card">
            <div class="tabs">
                <div class="tab active" data-tab="enrollment">Enrollment</div>
                <div class="tab" data-tab="fingerprints">Fingerprint Management</div>
                <div class="tab" data-tab="logs">Attendance Logs</div>
                <div class="tab" data-tab="system">System Status</div>
            </div>

            <div class="tab-content active" id="enrollment-tab">
                <div class="enrollment-steps">
                    <div class="step active" id="step1">
                        <div class="step-number">1</div>
                        <div class="step-label">Capture Face</div>
                    </div>
                    <div class="step" id="step2">
                        <div class="step-number">2</div>
                        <div class="step-label">Scan Fingerprint</div>
                    </div>
                    <div class="step" id="step3">
                        <div class="step-number">3</div>
                        <div class="step-label">Complete</div>
                    </div>
                </div>

                <div id="step1-content">
                    <div class="form-group">
                        <label class="form-label">Full Name</label>
                        <input type="text" class="form-control" id="enrollment-name" placeholder="Enter full name">
                    </div>
                    <div class="form-group">
                        <label class="form-label">Face Capture</label>
                        <div class="face-preview" id="face-preview">
                            <div class="no-face">No face captured</div>
                        </div>
                        <div class="btn-group">
                            <button class="btn btn-primary" id="capture-face-btn">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;">
                                    <path d="M12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" fill="currentColor"/>
                                    <path d="M20 4H16.8L15.2 2H8.8L7.2 4H4C2.9 4 2 4.9 2 6V18C2 19.1 2.9 20 4 20H20C21.1 20 22 19.1 22 18V6C22 4.9 21.1 4 20 4ZM12 17C9.2 17 7 14.8 7 12C7 9.2 9.2 7 12 7C14.8 7 17 9.2 17 12C17 14.8 14.8 17 12 17Z" fill="currentColor"/>
                                </svg>
                                Capture Face
                            </button>
                            <button class="btn btn-secondary" id="upload-face-btn">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;">
                                    <path d="M19 13H13V19H11V13H5V11H11V5H13V11H19V13Z" fill="currentColor"/>
                                </svg>
                                Upload Image
                            </button>
                        </div>
                    </div>
                    <div class="btn-group" style="justify-content: flex-end;">
                        <button class="btn btn-primary" id="next-step1" disabled>Next</button>
                    </div>
                </div>

                <div id="step2-content" style="display: none;">
                    <div class="alert alert-info">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM13 17H11V11H13V17ZM13 9H11V7H13V9Z" fill="currentColor"/>
                        </svg>
                        Place your finger on the scanner when prompted. You'll need to scan twice for verification.
                    </div>
                    <div class="scan-animation">
                        <div class="scan-line"></div>
                                                <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="fingerprint-icon-large">
                            <path d="M18.1 7.9C16.3 6.1 13.7 5 11 5C6 5 2 9.1 2 14C2 18.9 6 23 11 23H12V21H11C7.1 21 4 17.9 4 14C4 10.1 7.1 7 11 7C13.1 7 15.1 8.1 16.4 9.8L18.1 7.9Z" fill="currentColor"/>
                            <path d="M11 11C9.3 11 8 12.3 8 14V18C8 19.7 9.3 21 11 21C12.7 21 14 19.7 14 18V14C14 12.3 12.7 11 11 11ZM11 13C11.6 13 12 13.4 12 14V18C12 18.6 11.6 19 11 19C10.4 19 10 18.6 10 18V14C10 13.4 10.4 13 11 13Z" fill="currentColor"/>
                            <path d="M16.2 3.5C13.7 1.5 10.2 1.1 7.3 2.8L5.8 1.3C9.3 -0.8 13.7 -0.4 16.9 2.3L16.2 3.5Z" fill="currentColor"/>
                            <path d="M20.9 6.1C19.2 4.4 16.9 3.5 14.6 3.5C13.4 3.5 12.2 3.7 11 4.1V6.2C11.9 5.8 12.8 5.5 13.7 5.5C15.5 5.5 17.2 6.2 18.5 7.5L20.9 6.1Z" fill="currentColor"/>
                        </svg>
                        <div class="scan-text">WAITING FOR FINGERPRINT...</div>
                    </div>
                    <div class="terminal">
                        <div class="terminal-line"><span class="terminal-prompt">>></span> <span class="terminal-command">fingerprint_scanner --initialize</span></div>
                        <div class="terminal-line terminal-output">Scanner initialized successfully</div>
                        <div class="terminal-line terminal-output">Ready for fingerprint capture</div>
                        <div class="terminal-line"><span class="terminal-prompt">>></span> <span class="terminal-command">awaiting_input()</span></div>
                    </div>
                    <div class="btn-group">
                        <button class="btn btn-secondary" id="prev-step2">Back</button>
                        <button class="btn btn-primary" id="next-step2" disabled>Next</button>
                    </div>
                </div>

                <div id="step3-content" style="display: none;">
                    <div class="alert alert-success">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM10 17L5 12L6.41 10.59L10 14.17L17.59 6.58L19 8L10 17Z" fill="currentColor"/>
                        </svg>
                        Enrollment complete! The new biometric profile has been successfully added to the system.
                    </div>
                    <div class="form-group">
                        <label class="form-label">Employee ID</label>
                        <input type="text" class="form-control" id="employee-id" value="CMRL-2023-0482" readonly>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Access Level</label>
                        <select class="form-control" id="access-level">
                            <option>Level 1 - Basic Access</option>
                            <option>Level 2 - Departmental Access</option>
                            <option selected>Level 3 - Full Access</option>
                            <option>Level 4 - Admin Access</option>
                        </select>
                    </div>
                    <div class="btn-group">
                        <button class="btn btn-secondary" id="prev-step3">Back</button>
                        <button class="btn btn-primary" id="complete-enrollment">Finish Enrollment</button>
                    </div>
                </div>
            </div>

            <div class="tab-content" id="fingerprints-tab">
                <div class="alert alert-warning">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M1 21H23L12 2L1 21ZM13 18H11V16H13V18ZM13 14H11V10H13V14Z" fill="currentColor"/>
                    </svg>
                    Fingerprint scanner status: {% if fingerprint_connected %}Connected{% else %}Disconnected{% endif %}. {% if not fingerprint_connected %}Please connect the fingerprint scanner to enable management.{% endif %}
                </div>
                <div class="file-upload" id="fingerprint-upload">
                    <div class="file-upload-icon">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M18 16.08C17.24 16.08 16.56 16.38 16.04 16.85L8.91 12.7C8.96 12.47 9 12.24 9 12C9 11.76 8.96 11.53 8.91 11.3L15.96 7.19C16.5 7.69 17.21 8 18 8C19.66 8 21 6.66 21 5C21 3.34 19.66 2 18 2C16.34 2 15 3.34 15 5C15 5.24 15.04 5.47 15.09 5.7L8.04 9.81C7.5 9.31 6.79 9 6 9C4.34 9 3 10.34 3 12C3 13.66 4.34 15 6 15C6.79 15 7.5 14.69 8.04 14.19L15.16 18.35C15.11 18.56 15.08 18.78 15.08 19C15.08 20.61 16.39 21.92 18 21.92C19.61 21.92 20.92 20.61 20.92 19C20.92 17.39 19.61 16.08 18 16.08Z" fill="var(--primary)"/>
                        </svg>
                    </div>
                    <div class="file-upload-text">Upload Fingerprint Template</div>
                    <div class="file-upload-hint">Supports .fpt, .ist, and .ansi formats</div>
                </div>
                <div class="fingerprint-list">
                    {% for fingerprint in fingerprints %}
                    <div class="fingerprint-item">
                        <div class="fingerprint-info">
                            <div class="fingerprint-icon">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M18.1 7.9C16.3 6.1 13.7 5 11 5C6 5 2 9.1 2 14C2 18.9 6 23 11 23H12V21H11C7.1 21 4 17.9 4 14C4 10.1 7.1 7 11 7C13.1 7 15.1 8.1 16.4 9.8L18.1 7.9Z" fill="currentColor"/>
                                    <path d="M11 11C9.3 11 8 12.3 8 14V18C8 19.7 9.3 21 11 21C12.7 21 14 19.7 14 18V14C14 12.3 12.7 11 11 11ZM11 13C11.6 13 12 13.4 12 14V18C12 18.6 11.6 19 11 19C10.4 19 10 18.6 10 18V14C10 13.4 10.4 13 11 13Z" fill="currentColor"/>
                                    <path d="M16.2 3.5C13.7 1.5 10.2 1.1 7.3 2.8L5.8 1.3C9.3 -0.8 13.7 -0.4 16.9 2.3L16.2 3.5Z" fill="currentColor"/>
                                    <path d="M20.9 6.1C19.2 4.4 16.9 3.5 14.6 3.5C13.4 3.5 12.2 3.7 11 4.1V6.2C11.9 5.8 12.8 5.5 13.7 5.5C15.5 5.5 17.2 6.2 18.5 7.5L20.9 6.1Z" fill="currentColor"/>
                                </svg>
                            </div>
                            <div>
                                <div class="fingerprint-id">ID: {{ fingerprint.id }}</div>
                                <div class="fingerprint-name">{{ fingerprint.name }}</div>
                            </div>
                        </div>
                        <button class="btn btn-danger" data-id="{{ fingerprint.id }}">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;">
                                <path d="M6 19C6 20.1 6.9 21 8 21H16C17.1 21 18 20.1 18 19V7H6V19ZM19 4H15.5L14.5 3H9.5L8.5 4H5V6H19V4Z" fill="currentColor"/>
                            </svg>
                            Delete
                        </button>
                    </div>
                    {% endfor %}
                </div>
                <div class="btn-group" style="justify-content: flex-end; margin-top: 20px;">
                    <button class="btn btn-primary" id="scan-new-fingerprint">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;">
                            <path d="M4.27 3L3 4.27L9.73 11H6c-2.21 0-4 1.79-4 4v2c0 .55.45 1 1 1h14.73l2 2L21 19.73 4.27 3zM15 18H6v-3c0-1.66 1.34-3 3-3h.73l6 6H15zM19 8h-2.73l2 2H19c1.1 0 2 .9 2 2v4c0 .55-.45 1-1 1h-.18l3 3L23 18.73 19 14.73V8z" fill="currentColor"/>
                        </svg>
                        Scan New Fingerprint
                    </button>
                </div>
            </div>

            <div class="tab-content" id="logs-tab">
                <div class="form-group">
                    <label class="form-label">Filter Logs</label>
                    <div style="display: flex; gap: 10px;">
                        <input type="date" class="form-control" id="log-date">
                        <select class="form-control" id="log-type">
                            <option value="all">All Types</option>
                            <option value="entry">Entry Only</option>
                            <option value="exit">Exit Only</option>
                            <option value="denied">Denied Attempts</option>
                        </select>
                        <button class="btn btn-secondary">Apply Filter</button>
                    </div>
                </div>
                <div class="activity-log">
                    {% for log in attendance_logs %}
                    <div class="activity-item">
                        <div class="activity-icon">
                            {% if log.type == 'entry' %}
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M10 17L15 12L10 7V17Z" fill="var(--success)"/>
                            </svg>
                            {% elif log.type == 'exit' %}
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M14 7L9 12L14 17V7Z" fill="var(--danger)"/>
                            </svg>
                            {% else %}
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41Z" fill="var(--warning)"/>
                            </svg>
                            {% endif %}
                        </div>
                        <div class="activity-details">
                            <div class="activity-name">{{ log.name }}</div>
                            <div class="activity-meta">
                                <span>{{ log.time }}</span>
                                <span class="activity-method">{{ log.method }}</span>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
                <div class="btn-group" style="justify-content: flex-end; margin-top: 20px;">
                    <button class="btn btn-secondary">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;">
                            <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4C9.11 4 6.6 5.64 5.35 8.04C2.34 8.36 0 10.91 0 14C0 17.31 2.69 20 6 20H19C21.76 20 24 17.76 24 15C24 12.36 21.95 10.22 19.35 10.04ZM19 18H6C3.79 18 2 16.21 2 14C2 11.95 3.53 10.24 5.56 10.03L6.63 9.92L7.13 8.97C8.08 7.14 9.94 6 12 6C14.62 6 16.88 7.86 17.39 10.43L17.69 11.93L19.22 12.04C20.78 12.14 22 13.45 22 15C22 16.65 20.65 18 19 18Z" fill="currentColor"/>
                        </svg>
                        Refresh Logs
                    </button>
                    <button class="btn btn-primary">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;">
                            <path d="M15 9H9V15H15V9Z" fill="currentColor"/>
                            <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3ZM19 19H5V5H19V19Z" fill="currentColor"/>
                        </svg>
                        Export CSV
                    </button>
                </div>
            </div>

            <div class="tab-content" id="system-tab">
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-label">System Uptime</div>
                        <div class="stat-value" id="uptime">-</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">CPU Usage</div>
                        <div class="stat-value" id="cpu-usage">-</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Memory Usage</div>
                        <div class="stat-value" id="memory-usage">-</div>
                    </div>
                </div>
                <div class="terminal">
                    <div class="terminal-line"><span class="terminal-prompt">>></span> <span class="terminal-command">system_status --all</span></div>
                    <div class="terminal-line terminal-output">Nexus Biometric System v2.3.5</div>
                    <div class="terminal-line terminal-output">Initialized: 2023-06-15 08:42:17</div>
                    <div class="terminal-line terminal-output">Last reboot: 2023-06-28 03:15:42</div>
                    <div class="terminal-line terminal-output">Camera: {% if camera_connected %}Connected (640x480 @ 30fps){% else %}Disconnected{% endif %}</div>
                    <div class="terminal-line terminal-output">Fingerprint Scanner: {% if fingerprint_connected %}Connected (AS602){% else %}Disconnected{% endif %}</div>
                    <div class="terminal-line terminal-output">Access Control: {% if arduino_connected %}Connected (COM3){% else %}Disconnected{% endif %}</div>
                    <div class="terminal-line terminal-output">Database: Connected (127.0.0.1:5432)</div>
                    <div class="terminal-line"><span class="terminal-prompt">>></span> <span class="terminal-command">performance_monitor</span></div>
                    <div class="terminal-line terminal-output" id="performance-line">Loading real-time performance data...</div>
                </div>
                <div class="btn-group" style="justify-content: flex-end; margin-top: 20px;">
                    <button class="btn btn-danger" id="restart-system">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;">
                            <path d="M12 5V1L7 6L12 11V7C15.31 7 18 9.69 18 13C18 16.31 15.31 19 12 19C8.69 19 6 16.31 6 13H4C4 17.42 7.58 21 12 21C16.42 21 20 17.42 20 13C20 8.58 16.42 5 12 5Z" fill="currentColor"/>
                        </svg>
                        Restart System
                    </button>
                </div>
            </div>
        </div>
    </div>

    <div class="modal" id="face-capture-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 class="modal-title">Capture Face Image</h3>
                <button class="modal-close" id="close-face-modal">&times;</button>
            </div>
            <div class="modal-body">
                <div class="video-container" style="height: 300px;">
                    <img class="video-feed" src="{{ url_for('video_feed') }}">
                    <div class="video-overlay">
                        <div class="detection-status">
                            <div class="detection-indicator"></div>
                            <span class="detection-text">AWAITING DETECTION</span>
                        </div>
                    </div>
                </div>
                <div class="alert alert-info" style="margin-top: 15px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM13 17H11V11H13V17ZM13 9H11V7H13V9Z" fill="currentColor"/>
                    </svg>
                    Position your face in the center of the frame. Ensure good lighting and remove any obstructions.
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" id="cancel-capture">Cancel</button>
                <button class="btn btn-primary" id="confirm-capture">Capture</button>
            </div>
        </div>
    </div>

    <div class="modal" id="fingerprint-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 class="modal-title">Fingerprint Enrollment</h3>
                <button class="modal-close" id="close-fingerprint-modal">&times;</button>
            </div>
            <div class="modal-body">
                <div class="scan-animation">
                    <div class="scan-line"></div>
                    <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="fingerprint-icon-large">
                        <path d="M18.1 7.9C16.3 6.1 13.7 5 11 5C6 5 2 9.1 2 14C2 18.9 6 23 11 23H12V21H11C7.1 21 4 17.9 4 14C4 10.1 7.1 7 11 7C13.1 7 15.1 8.1 16.4 9.8L18.1 7.9Z" fill="currentColor"/>
                        <path d="M11 11C9.3 11 8 12.3 8 14V18C8 19.7 9.3 21 11 21C12.7 21 14 19.7 14 18V14C14 12.3 12.7 11 11 11ZM11 13C11.6 13 12 13.4 12 14V18C12 18.6 11.6 19 11 19C10.4 19 10 18.6 10 18V14C10 13.4 10.4 13 11 13Z" fill="currentColor"/>
                        <path d="M16.2 3.5C13.7 1.5 10.2 1.1 7.3 2.8L5.8 1.3C9.3 -0.8 13.7 -0.4 16.9 2.3L16.2 3.5Z" fill="currentColor"/>
                        <path d="M20.9 6.1C19.2 4.4 16.9 3.5 14.6 3.5C13.4 3.5 12.2 3.7 11 4.1V6.2C11.9 5.8 12.8 5.5 13.7 5.5C15.5 5.5 17.2 6.2 18.5 7.5L20.9 6.1Z" fill="currentColor"/>
                    </svg>
                    <div class="scan-text" id="fingerprint-status">PLACE YOUR FINGER ON THE SCANNER</div>
                </div>
                <div class="progress-container">
                    <div class="progress-label">
                        <span>Enrollment Progress</span>
                        <span id="fingerprint-progress">0%</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" id="fingerprint-progress-bar" style="width: 0%;"></div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-danger" id="cancel-fingerprint">Cancel</button>
            </div>
        </div>
    </div>

    <script>
        // Tab switching functionality
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                // Remove active class from all tabs and contents
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                
                // Add active class to clicked tab and corresponding content
                tab.classList.add('active');
                const tabId = tab.getAttribute('data-tab') + '-tab';
                document.getElementById(tabId).classList.add('active');
            });
        });

        // Enrollment steps navigation
        const steps = ['step1', 'step2', 'step3'];
        let currentStep = 0;

        function showStep(stepIndex) {
            // Hide all step contents
            document.querySelectorAll('[id$="-content"]').forEach(el => {
                el.style.display = 'none';
            });
            
            // Show current step content
            document.getElementById(steps[stepIndex] + '-content').style.display = 'block';
            
            // Update step indicators
            document.querySelectorAll('.step').forEach((step, index) => {
                step.classList.remove('active', 'completed');
                if (index < stepIndex) {
                    step.classList.add('completed');
                } else if (index === stepIndex) {
                    step.classList.add('active');
                }
            });
        }

        document.getElementById('next-step1').addEventListener('click', () => {
            currentStep = 1;
            showStep(currentStep);
        });

        document.getElementById('prev-step2').addEventListener('click', () => {
            currentStep = 0;
            showStep(currentStep);
        });

        document.getElementById('next-step2').addEventListener('click', () => {
            currentStep = 2;
            showStep(currentStep);
        });

        document.getElementById('prev-step3').addEventListener('click', () => {
            currentStep = 1;
            showStep(currentStep);
        });

        document.getElementById('complete-enrollment').addEventListener('click', () => {
            // Reset enrollment form
            currentStep = 0;
            showStep(currentStep);
            document.getElementById('enrollment-name').value = '';
            document.getElementById('face-preview').innerHTML = '<div class="no-face">No face captured</div>';
            document.getElementById('next-step1').disabled = true;
            
            // Show success notification
            alert('Enrollment completed successfully!');
        });

        // Face capture modal
        const faceModal = document.getElementById('face-capture-modal');
        document.getElementById('capture-face-btn').addEventListener('click', () => {
            faceModal.classList.add('active');
        });

        document.getElementById('close-face-modal').addEventListener('click', () => {
            faceModal.classList.remove('active');
        });

        document.getElementById('cancel-capture').addEventListener('click', () => {
            faceModal.classList.remove('active');
        });

        document.getElementById('confirm-capture').addEventListener('click', () => {
            // In a real app, this would capture the frame from the video feed
            // For demo, we'll just use a placeholder
            const facePreview = document.getElementById('face-preview');
            facePreview.innerHTML = '<img src="https://via.placeholder.com/150x150/0a0a1a/00f0ff?text=Face+Captured" alt="Captured Face">';
            
            // Enable next button
            document.getElementById('next-step1').disabled = false;
            
            // Close modal
            faceModal.classList.remove('active');
        });

        // Fingerprint modal
        const fingerprintModal = document.getElementById('fingerprint-modal');
        document.getElementById('scan-new-fingerprint').addEventListener('click', () => {
            fingerprintModal.classList.add('active');
            simulateFingerprintScan();
        });

        document.getElementById('close-fingerprint-modal').addEventListener('click', () => {
            fingerprintModal.classList.remove('active');
        });

        document.getElementById('cancel-fingerprint').addEventListener('click', () => {
            fingerprintModal.classList.remove('active');
        });

        function simulateFingerprintScan() {
            const statusText = document.getElementById('fingerprint-status');
            const progressBar = document.getElementById('fingerprint-progress-bar');
            const progressText = document.getElementById('fingerprint-progress');
            
            let progress = 0;
            const interval = setInterval(() => {
                progress += Math.floor(Math.random() * 10) + 5;
                if (progress > 100) progress = 100;
                
                progressBar.style.width = progress + '%';
                progressText.textContent = progress + '%';
                
                if (progress < 30) {
                    statusText.textContent = 'SCANNING FINGERPRINT...';
                } else if (progress < 70) {
                    statusText.textContent = 'PROCESSING IMAGE...';
                } else if (progress < 100) {
                    statusText.textContent = 'VERIFYING TEMPLATE...';
                } else {
                    statusText.textContent = 'FINGERPRINT CAPTURED!';
                    clearInterval(interval);
                    
                    // Enable next button in enrollment
                    if (currentStep === 1) {
                        document.getElementById('next-step2').disabled = false;
                    }
                    
                    // Close modal after 1 second
                    setTimeout(() => {
                        fingerprintModal.classList.remove('active');
                    }, 1000);
                }
            }, 500);
        }

        // Simulate detection updates
        const names = ['John Doe', 'Jane Smith', 'Robert Johnson', 'Emily Davis', 'Michael Wilson'];
        setInterval(() => {
            if (Math.random() > 0.7) {
                const randomName = names[Math.floor(Math.random() * names.length)];
                document.getElementById('detection-name').textContent = randomName;
                document.querySelector('.detection-indicator').classList.add('active');
                
                // Add to activity log
                const activityLog = document.getElementById('activity-log');
                const activityItem = document.createElement('div');
                activityItem.className = 'activity-item';
                activityItem.innerHTML = `
                    <div class="activity-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M10 17L15 12L10 7V17Z" fill="var(--success)"/>
                        </svg>
                    </div>
                    <div class="activity-details">
                        <div class="activity-name">${randomName}</div>
                        <div class="activity-meta">
                            <span>${new Date().toLocaleTimeString()}</span>
                            <span class="activity-method">Face Recognition</span>
                        </div>
                    </div>
                `;
                activityLog.insertBefore(activityItem, activityLog.firstChild);
                
                // Clear after 3 seconds
                setTimeout(() => {
                    document.getElementById('detection-name').textContent = '-';
                    document.querySelector('.detection-indicator').classList.remove('active');
                }, 3000);
            }
        }, 5000);

        // Simulate system stats
        function updateSystemStats() {
            document.getElementById('uptime').textContent = Math.floor(Math.random() * 24) + 'h ' + 
                                                          Math.floor(Math.random() * 60) + 'm';
            
            document.getElementById('cpu-usage').textContent = Math.floor(Math.random() * 30) + 10 + '%';
            document.getElementById('memory-usage').textContent = Math.floor(Math.random() * 40) + 30 + '%';
            document.getElementById('today-logs').textContent = Math.floor(Math.random() * 50) + 10;
            
            const performanceLine = document.getElementById('performance-line');
            performanceLine.textContent = `CPU: ${Math.floor(Math.random() * 30) + 10}% | Memory: ${Math.floor(Math.random() * 40) + 30}% | Processes: ${Math.floor(Math.random() * 150) + 50}`;
        }
        
        updateSystemStats();
        setInterval(updateSystemStats, 3000);

        // Particles background
        function createParticles() {
            const particlesContainer = document.getElementById('particles');
            const particleCount = 30;
            
            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.classList.add('particle');
                
                // Random size between 1px and 3px
                const size = Math.random() * 2 + 1;
                particle.style.width = `${size}px`;
                particle.style.height = `${size}px`;
                
                // Random position
                particle.style.left = `${Math.random() * 100}vw`;
                particle.style.top = `${Math.random() * 100}vh`;
                
                // Random animation
                const duration = Math.random() * 20 + 10;
                const delay = Math.random() * 5;
                particle.style.animation = `float ${duration}s ease-in-out ${delay}s infinite`;
                
                particlesContainer.appendChild(particle);
            }
        }
        
        createParticles();
    </script>
</body>
</html>
"""""                

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
app = Flask(__name__, template_folder='templates')

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
FINGERPRINT_DB = os.path.join(BASE_DIR, "/home/hacker_sam/Desktop/server_CMRL/fingerprint_db.csv")
MODEL_PATH = "yolov8n.pt"
CAMERA_INDEX = 0
FINGERPRINT_SENSOR_PORT = '/dev/ttyACM1'
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
        self.detection_history = deque(maxlen=20)  # Increased buffer
        self.lock = threading.Lock()
        self.fingerprint_cache = {}
        self.system_status = {
            'camera': self.camera is not None,
            'fingerprint': FINGERPRINT_CONNECTED,
            'arduino': ARDUINO_CONNECTED,
            'last_check': time.time(),
            'fingerprint_count': 0
        }
        
        # Initialize serial connection to Arduino
        self.arduino = self.initialize_arduino()
        self.fingerprint = self.initialize_fingerprint()
        
    def initialize_arduino(self):
        if not ARDUINO_CONNECTED:
            return None
        try:
            arduino = serial.Serial(ARDUINO_PORT, 9600, timeout=1)
            time.sleep(2)  # Allow time for connection
            return arduino
        except Exception as e:
            print(f"Arduino connection error: {str(e)}")
            return None

    def initialize_fingerprint(self):
        if not FINGERPRINT_CONNECTED:
            return None
        try:
            fp = PyFingerprint(FINGERPRINT_SENSOR_PORT, FINGERPRINT_BAUDRATE)
            if fp.verifyPassword():
                self.system_status['fingerprint_count'] = fp.getTemplateCount()
                return fp
            return None
        except Exception as e:
            print(f"Fingerprint sensor error: {str(e)}")
            return None

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
        with self.lock:
            try:
                with open(FINGERPRINT_DB, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    for fid, name in self.fingerprint_db.items():
                        writer.writerow([fid, name])
            except Exception as e:
                print(f"Error saving fingerprint DB: {str(e)}")

    def enroll_fingerprint(self):
        if not FINGERPRINT_CONNECTED:
            return {'success': False, 'message': 'Fingerprint sensor not connected'}
        
        try:
            # Send command to Arduino to start enrollment
            if self.arduino:
                self.arduino.write(b'ENROLL_START\n')
            
            # Get next available ID
            next_id = max(self.fingerprint_db.keys(), default=0) + 1
            
            # Wait for Arduino to complete enrollment
            start_time = time.time()
            while time.time() - start_time < FINGERPRINT_ENROLLMENT_TIMEOUT:
                if self.arduino and self.arduino.in_waiting:
                    response = self.arduino.readline().decode().strip()
                    if response == "ENROLL_SUCCESS":
                        return {
                            'success': True,
                            'fingerprint_id': next_id,
                            'message': 'Fingerprint enrolled successfully'
                        }
                    elif "FAIL" in response:
                        return {'success': False, 'message': response}
                time.sleep(0.1)
            
            return {'success': False, 'message': 'Enrollment timeout'}
        except Exception as e:
            return {'success': False, 'message': str(e)}

    def verify_fingerprint(self):
        if not FINGERPRINT_CONNECTED:
            return None
        
        try:
            # Send verification command to Arduino
            if self.arduino:
                self.arduino.write(b'VERIFY\n')
            
            # Wait for response
            start_time = time.time()
            while time.time() - start_time < 5:  # 5 second timeout
                if self.arduino and self.arduino.in_waiting:
                    response = self.arduino.readline().decode().strip()
                    if response.startswith("FINGERPRINT_ID:"):
                        fid = int(response.split(':')[1])
                        if fid in self.fingerprint_db:
                            return fid
                time.sleep(0.1)
            return None
        except Exception as e:
            print(f"Fingerprint verification error: {str(e)}")
            return None

    def check_hardware_status(self):
        current_time = time.time()
        if current_time - self.system_status['last_check'] > 5:
            self.system_status.update({
                'camera': self.camera is not None and self.camera.isOpened(),
                'arduino': self.arduino is not None,
                'last_check': current_time
            })
            
            if FINGERPRINT_CONNECTED and self.fingerprint:
                try:
                    self.system_status['fingerprint'] = self.fingerprint.verifyPassword()
                    self.system_status['fingerprint_count'] = self.fingerprint.getTemplateCount()
                except:
                    self.system_status['fingerprint'] = False
        return self.system_status

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
        # Create necessary directories
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        os.makedirs(os.path.dirname(FINGERPRINT_DB), exist_ok=True)
        
        print("Starting biometric system...")
        print(f"Known faces loaded: {len(system.known_faces)}")
        
        # Start hardware status monitoring thread
        def hardware_monitor():
            while True:
                system.check_hardware_status()
                time.sleep(5)
        
        monitor_thread = threading.Thread(target=hardware_monitor, daemon=True)
        monitor_thread.start()
        
        print("Starting web server...")
        app.run(host='0.0.0.0', port=5000, threaded=True)
        
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        cleanup()
        print("Cleanup complete")