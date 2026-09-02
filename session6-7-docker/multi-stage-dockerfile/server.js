const express = require("express");

const app = express();
const PORT = process.env.PORT || 8080;

app.get("/", (req, res) => {
  res.type("html").send(`<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Docker Multi-Stage Build</title>
  </head>
  <body>
    <h1>Hello World from Docker multi-stage build</h1>
    <p>Served by Express inside a container, listening on port ${PORT}</p>
  </body>
</html>
`);
});

app.get("/health", (req, res) => {
  res.json({ status: "ok", port: Number(PORT) });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
