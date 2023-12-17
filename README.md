# Tornado WebSocket Project

This project utilizes Tornado, a Python web framework and asynchronous networking library, to establish a WebSocket connection between a client and a server. The goal is to measure latency, throughput, and collect hardware details during data exchange.

## Files

### 1. `tornado_client.py`

This file represents the Tornado WebSocket client. It sends messages to the server and generates an Excel file called tornado.xlsx that contains real-time data, including latency, throughput, and hardware details.

### 2. `tornado_server.py`

This file contains the Tornado WebSocket server. It listens for incoming messages from the client, simulates real-time data, and calculates latency and throughput.

### Prerequisites

1. `git clone https://github.com/Rectiras/repo-websockets.git`
2. cd repo-websockets
3. Make sure Python installed on your system.
4. pip install -r requirements.txt

## Running the Project

1. python tornado_server.py
2. python tornado_client.py

### Using the Tornado Websockets

1. Client can input messages and see responses from the server with a fixed json data which can be changed in tornado_server.py . Client must input `exit` in order to generate the Excel file which provides the summary.
