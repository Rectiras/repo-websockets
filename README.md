# WebSocket Comparison Project

This project aims to compare WebSocket implementations in two Python frameworks: Tornado and Websockets. The evaluation includes measuring latency, throughput, scalability, and collecting hardware details during data exchange.

## Prerequisites

1. Clone the repository: `git clone https://github.com/Rectiras/repo-websockets.git`
2. Navigate to the project directory: `cd repo-websockets`
3. Ensure Python is installed on your system.
4. Install project dependencies: `pip install -r requirements.txt`

## Tornado WebSocket Implementation

### Files for Tornado

1. `tornado_client.py`: Tornado WebSocket client. Sends messages to the server and generates an Excel file named tornado.xlsx containing real-time data, including latency, throughput, and hardware details.

2. `tornado_server.py`: Tornado WebSocket server. Listens for incoming messages from the client, simulates real-time data, and calculates latency and throughput.

### Running the Tornado WebSocket Project

1. Start the server: `python tornado_server.py`
2. Launch the client: `python tornado_client.py`

### Using Tornado WebSockets

- The client can input messages and receive responses from the server with fixed JSON data (modifiable in `tornado_server.py`).
- To generate the Excel file with a summary, clients must input `exit`.

## Websockets WebSocket Implementation

### Files for Websockets

1. `websockets_client.py`: Websockets WebSocket client. Sends messages to the server and generates an Excel file named websockets.xlsx containing real-time data, including latency, throughput, and hardware details.

2. `websockets_server.py`: Websockets WebSocket server. Listens for incoming messages from the client, simulates real-time data, and calculates latency and throughput.

### Running the Websockets WebSocket Project

1. Start the server: `python websockets_server.py`
2. Launch the client: `python websockets_client.py`

### Using Websockets

- Similar to Tornado, the client can input messages and receive responses from the server with fixed JSON data (modifiable in `websockets_server.py`).
- To generate the Excel file with a summary, clients must input `exit`.

### Results

1. **Latency Comparison**
   - Tornado Average Latency: 0.000965
   - Websockets Average Latency: 0.000876

   - Websockets Performed 10% better than Tornado

2. **Throughput Comparison**
   - Tornado Throughput: 30,2804844366243
   - Websockets Throughput: 30,3015221337059

   - Almost Identical Throughput with Websockets performing slighly better than Tornado.

3. **Scalability**
   - Tornado:
   - - Well-suited for handling concurrent connections
   - - May require fine-tuning for specific scalability requirements

   - Websockets:
   - - High concurrency support
   - - Asynchronous architecture for efficiency

### Conclusion

Based on the comparison, Websockets demonstrated approximately 10% better latency and nearly identical throughput compared to Tornado. While both libraries have their strengths, Websockets is recommended for this scenario due to superior latency performance.
