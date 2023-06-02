import { io } from 'socket.io-client';

// "undefined" means the URL will be computed from the `window.location` object
const URL = '127.0.0.1:8000/ws/socket-server/';

export const socket = io(URL);