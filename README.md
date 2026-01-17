# 🛡️ SOC-Snap: Automated SOC Evidence Collector

SOC-Snap is a specialized Python-based endpoint monitoring tool designed for **Security Operations Centers (SOC)**. It automates the process of capturing visual evidence during an investigation, packaging it for exfiltration, and sanitizing the local environment to maintain a clean forensic footprint.



## ✨ Core Features
- **Mission-Based Monitoring:** Define a specific "mission" with a total duration and capture interval. ⏱️
- **Efficient Exfiltration:** Instead of flooding an inbox, it bundles all captures into a single compressed **ZIP report**. 🗜️
- **Encrypted Delivery:** Securely dispatches findings to a centralized SOC inbox via `SMTP_SSL`. 📧
- **Zero-Footprint Cleanup:** Automatically wipes the local screenshot directory and the temporary ZIP file after a successful dispatch. 🧹
- **High-Performance Capture:** Built with `mss` for lightweight, cross-platform screen monitoring. 📸

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.x installed. Install the high-performance capture library:
```bash
pip install mss

```

### 2. Configuration

Open the script and update the **SOC Credentials** section with your environment details:

* `SENDER_EMAIL`: The account used to dispatch alerts.
* `RECEIVER_EMAIL`: The SOC analyst's inbox.
* `APP_PASSWORD`: A 16-character Google App Password (do NOT use your regular password!).

### 3. Usage

Execute the monitor and follow the mission prompts:

```bash
python sentinelsnap.py

```

> **Example Mission:** A 60-second window with a 10-second interval will generate a 6-image forensic report.

---

## 🧠 SOC Operational Logic

The script follows a standard "Observe, Collect, Report, Sanitize" logic flow:

1. **Observe:** Periodic snapshots are saved to a temporary vault.
2. **Collect:** Data is compressed to minimize network traffic and stay within email limits.
3. **Report:** The zip is sent to the SOC with a timestamped subject line for easy triage.
4. **Sanitize:** The tool performs a recursive delete of the local vault to prevent unauthorized access to captured data.

---

## ⚖️ Ethical Use & Disclaimer

This tool is developed for **educational purposes** and **authorized SOC monitoring** only. Unauthorized monitoring of computer activity is illegal and unethical. Use this tool only on systems you own or have explicit, written permission to monitor.

-----
