# Fresh command evidence — reviewed index

Rudray Mehra | 24 BCS 10425 | Batch B

Raw logs and capture manifests are unchanged. Visual decisions are hash-bound in
[the review record](../../../evidence/coursework/native-review.json).
Rejected images remain local and are excluded from publication. A pass is only for the named command.

## Session 04 — actual 01-route

Execution: PASS.

[Original command output](01-route.txt)

Native capture: **accepted**. Actual default-route output and Rudray heading visible.

![Reviewed native window capture](01-route.png)

## Session 04 — actual 02-sockets

Execution: PASS.

[Original command output](02-sockets.txt)

Native capture: **accepted**. Socket output tail and identity visible; command is above the viewport, so use the paired original log for context.

![Reviewed native window capture](02-sockets.png)

## Session 04 — actual 03-dns

Execution: PASS.

[Original command output](03-dns.txt)

Native capture: **accepted**. Actual DNS result and Rudray heading visible.

![Reviewed native window capture](03-dns.png)

## Session 04 — actual 04-ping

Execution: PASS.

[Original command output](04-ping.txt)

Native capture: **accepted**. Actual ping results and Rudray heading visible.

![Reviewed native window capture](04-ping.png)

## Session 04 — actual 05-http

Execution: FAILED / BLOCKED.

[Original command output](05-http.txt)

Native capture: **rejected**. Wrong window: chat conversation instead of HTTP command output. Retake; the paired curl log records a timeout, not success.

## Reference-specific pending items

Execution: NOT RUN: Capture routes, sockets, DNS, ping and HTTP on the actual host. Record network restrictions as failures, not successful connectivity..

Native capture: **not-captured**. No native image captured.
