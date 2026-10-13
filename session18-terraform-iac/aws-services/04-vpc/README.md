# VPC — Virtual Private Cloud

A VPC is an isolated regional IP network. Its CIDR defines the address range, which
is divided into availability-zone subnets. A subnet is public when its route table
has a route to an Internet Gateway and its workloads have public addressing; a
subnet is private when it lacks that direct route.

Route tables select a next hop for destination CIDRs. An Internet Gateway connects
public IPv4 workloads to the internet. A NAT Gateway lets private-subnet workloads
initiate outbound IPv4 connections without accepting unsolicited inbound traffic.

Security Groups are stateful and attach to network interfaces. Network ACLs are
stateless subnet-level allow/deny lists. Security Groups are normally the primary
workload control; NACLs provide coarse subnet defense.

Production designs use multiple Availability Zones, separate public/private/data
subnets, controlled egress, VPC Flow Logs, endpoints for AWS services, non-overlapping
CIDRs, and no unrestricted administrative ports.
