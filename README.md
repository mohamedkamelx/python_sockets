# Python Socket Chat Application

A simple TCP/IP socket-based chat application using Python's socket and threading.

## Features

- Multi-threaded server handles multiple client connections
- Header-based messaging protocol (64-byte headers)
- Graceful client disconnection handling

## Quick Start

### Server

```bash
python server.py
```

### Client

```bash
python client.py
```

## How It Works

### Server

- Binds to local IP address on port 5050
- Creates a new thread for each client connection
- Receives messages from clients with length-prefixed protocol
- Handles client disconnections properly

### Client

- Connects to server using local IP on port 5050
- Receives welcome message from server
- Sends user input messages to server with proper header
- Uses "kosomk" as disconnection message

## Communication Protocol

- Each message has a 64-byte header containing the message length
- After the header, the actual message content is sent
- UTF-8 encoding is used for all messages


## Future Improvements

1. **Complete the receive function**: Implement message receiving in the client
2. **Add message broadcasting**: Allow server to broadcast messages to all clients
3. **Implement username system**: Let users identify themselves with usernames
4. **Add GUI**: Create a graphical interface for easier interaction
5. **Encrypt communication**: Add security with end-to-end encryption
6. **File transfer**: Enable sending files between clients
7. **Private messaging**: Allow clients to send direct messages to specific users
8. **Chat rooms**: Implement separate chat rooms or channels
9. **Message history**: Store and retrieve previous messages
10. **Connection status**: Show online/offline status of users
