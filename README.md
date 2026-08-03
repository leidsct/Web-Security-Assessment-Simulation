# 🛡️ Web Application Interface Manipulation & Vulnerability Assessment

## 📌 Overview
This project demonstrates a **Client-Side DOM Manipulation Simulation** and an automated security vulnerability audit on a web application inside a **Kali Linux** testing environment using **OWASP ZAP**. 

> **Disclaimer:** The interface modifications shown here are client-side simulations performed via browser Developer Tools for demonstration, testing, and educational purposes. No actual server-side files were permanently altered.

---

## 📸 Simulation & Security Analysis

### 1. Client-Side DOM & UI Manipulation Simulation
Demonstration of temporary client-side layout and style overrides executed via DevTools to simulate interface response testing.
![Defacement PoC](./defacement-poc.jpg)

### 2. OWASP ZAP Vulnerability Scanning Results
Automated security assessment highlighting missing security headers and configuration risks.
![ZAP Scan](./zap-scan.jpg)

### 3. Intercepted Authentication Request
Inspection of HTTP POST requests and parameter handling captured using OWASP ZAP proxy.
![ZAP Request](./zap-request.jpg)

---

## 🛠️ Simulation Steps (DevTools Layout Overrides)

1. **Access Developer Console:** Press `F12` or `Ctrl + Shift + I` in Firefox/Chrome.
2. **Apply Custom Theme:**
   Modify the `<body>` element style attribute:
   ```css
   background-image: url('MATRIX_IMAGE_URL');
   background-size: cover;
   background-attachment: fixed;
