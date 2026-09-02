import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

/**
 * Minimal Hello World HTTP server using only the JDK (no frameworks).
 */
public class Main {

    private static final int PORT = 8080;

    private static final String PAGE = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>Java Hello World</title>
          <style>
            body { margin: 0; font-family: Arial, sans-serif; background: #3b1f1f; color: #f9fafb;
                   display: flex; align-items: center; justify-content: center; height: 100vh; }
            .card { background: #5a2d2d; padding: 40px 60px; border-radius: 12px; text-align: center;
                    box-shadow: 0 8px 24px rgba(0,0,0,0.4); }
            h1 { margin: 0 0 10px; color: #f89820; }
            p { margin: 0; color: #d1d5db; }
          </style>
        </head>
        <body>
          <div class="card">
            <h1>Hello World from Java!</h1>
            <p>Served by com.sun.net.httpserver inside a Docker container on port 8080</p>
          </div>
        </body>
        </html>
        """;

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);

        server.createContext("/", Main::handleRoot);
        server.createContext("/health", Main::handleHealth);

        server.setExecutor(null); // default single-threaded executor
        server.start();
        System.out.println("Java Hello World server listening on port " + PORT);
    }

    private static void handleRoot(HttpExchange exchange) throws IOException {
        byte[] body = PAGE.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().add("Content-Type", "text/html; charset=utf-8");
        exchange.sendResponseHeaders(200, body.length);
        try (OutputStream os = exchange.getResponseBody()) {
            os.write(body);
        }
    }

    private static void handleHealth(HttpExchange exchange) throws IOException {
        byte[] body = "{\"status\":\"ok\",\"app\":\"java-app\"}".getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().add("Content-Type", "application/json");
        exchange.sendResponseHeaders(200, body.length);
        try (OutputStream os = exchange.getResponseBody()) {
            os.write(body);
        }
    }
}
