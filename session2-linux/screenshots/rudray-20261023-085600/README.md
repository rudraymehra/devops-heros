# Session 01–02 — Task 1 capture

Rudray Mehra | 24 BCS 10425 | Batch B

Capture date: 2026-10-23, approximately 08:56 local time. Environment: macOS
Terminal. This demonstrates link behavior on the Mac host; it is not Linux VM evidence.

![Hard and soft link demonstration](01-links.png)

The output shows that `original.txt` and `hardlink.txt` share inode `133473123`.
After removing `original.txt`, the hard link still prints the file contents, while
`softlink.txt` points to the removed name and reports “No such file or directory.”
