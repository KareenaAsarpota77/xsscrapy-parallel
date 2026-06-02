# Cyber Port Scanner Dashboard

## Overview
A web-based network security tool built with Flask that performs TCP port scanning, identifies open and closed ports, and visualizes results with basic reporting. The project demonstrates fundamental concepts of network scanning, socket programming, and security reporting.

## Features
- TCP port scanning using Python sockets
- Web-based dashboard using Flask
- Open and closed port detection
- Graphical visualization using Matplotlib
- Timestamped scan report generation
- Domain and IP-based scanning support

## Requirements
- Python 3.8 or higher
- Flask
- Matplotlib

Install dependencies:
pip install flask matplotlib

## Folder Structure

The application requires the following directory structure:

cyber-port-scanner/
├── app.py
├── scanner.py
├── templates/
│   └── index.html
├── static/ (stores generated visualization files)
├── reports/ (stores generated scan reports)
└── README.md

Note: Create the static/ and reports/ directories before running the application.

## Execution

Start the application:
python app.py

Open in browser:
http://127.0.0.1:5000/

## Input
- IPv4 addresses
- Domain names

Example inputs:
- 127.0.0.1 (local testing only)
- scanme.nmap.org (authorized test environment for security learning)

## Output
- Open/closed port results
- Graph visualization
- Scan report file

## Disclaimer
This project is intended for educational purposes and authorized security testing only.

The author is not responsible for misuse or damage caused by this tool. Users are responsible for ensuring proper authorization before scanning any target systems.

Unauthorized scanning may violate applicable laws and regulations.

## License
MIT License
