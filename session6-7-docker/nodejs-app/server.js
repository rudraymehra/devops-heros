const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Node.js Hello World</title>
  <style>
    body { margin: 0; font-family: Arial, sans-serif; background: #1f2937; color: #f9fafb;
           display: flex; align-items: center; justify-content: center; height: 100vh; }
    .card { background: #374151; padding: 40px 60px; border-radius: 12px; text-align: center;
            box-shadow: 0 8px 24px rgba(0,0,0,0.4); }
    h1 { margin: 0 0 10px; color: #68a063; }
    p { margin: 0; color: #d1d5db; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Hello World from Node.js!</h1>
    <p>Served by Express inside a Docker container on port ${PORT}</p>
  </div>
</body>
</html>`);
});

app.get('/health', (req, res) => {
  res.json({ status: 'ok', app: 'nodejs-app' });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Node.js Hello World app listening on port ${PORT}`);
});
