import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import time

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()
    message_count = 0
    start_time = None

    def open(self):
        print("WebSocket opened")
        self.clients.add(self)

    def on_message(self, message):
        print(f"Received message: {message}")

        # Simulate or obtain real-time data
        real_time_data = {
            "data_type": "json_data",
            "data": {
                "employees": [
                    {"name": "Shyam", "email": "shyamjaiswal@gmail.com"},
                    {"name": "Ram", "email": "ramjaiswal@gmail.com"},
                    {"name": "Hari", "email": "harijaiswal@gmail.com"},
                    {"name": "Gita", "email": "gitajaiswal@gmail.com"},
                ]
            }
        }
        # Calculate the size of the serialized JSON string
        serialized_data = json.dumps(real_time_data)
        data_size = len(serialized_data)

        # Include data size in the real_time_data
        real_time_data["data_size"] = data_size

        # Send real-time data to all connected clients
        for client in self.clients:
            client.write_message(json.dumps(real_time_data))

        # Update throughput metrics
        self.message_count += 1
        if self.start_time is None:
            self.start_time = time.time()
        elapsed_time = time.time() - self.start_time

        if elapsed_time >= 10:  # Update throughput every 10 seconds (adjust as needed)
            throughput = self.message_count / elapsed_time
            print(f"Throughput: {throughput} messages/second")

            # Send throughput to all connected clients
            throughput_data = {
                "data_type": "throughput",
                "data": {
                    "throughput": throughput
                }
            }
            for client in self.clients:
                client.write_message(json.dumps(throughput_data))

            # Reset counters for the next interval
            self.message_count = 0
            self.start_time = time.time()

    def on_close(self):
        print("WebSocket closed")
        self.clients.remove(self)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, WebSocket!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("WebSocket server is running at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()