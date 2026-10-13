# EC2 — Elastic Compute Cloud

EC2 supplies resizable virtual machines. An AMI defines the initial operating system
and disk image; an instance type defines CPU, memory, network, and accelerator shape.
A key pair supports SSH authentication, although Systems Manager Session Manager is
often safer because it avoids inbound SSH and private-key distribution.

Security Groups are stateful virtual firewalls. EBS provides persistent block
volumes independent of instance process lifetime. Public IPs permit routed internet
connectivity when the subnet route and firewall allow it; private addresses are used
inside the VPC. Elastic IPs are stable public addresses and can incur charges.

Lifecycle: pending, running, stopping/stopped, shutting-down, and terminated.
Stopping normally preserves EBS; termination deletes the instance and any volume
whose `delete_on_termination` flag is true.

Common uses include web/application servers, build runners, development machines,
batch work, and workloads that need OS-level control. Use Auto Scaling and load
balancing for resilient services; patch images, use instance roles, encrypt disks,
and avoid broad inbound rules.
