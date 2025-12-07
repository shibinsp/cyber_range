# Security Guide

## Overview
RetroRange implements defense-in-depth security controls.

## Authentication
- OAuth2 + JWT
- bcrypt password hashing (cost: 12)
- 15-minute access tokens
- 7-day refresh tokens

## Authorization (RBAC)
- 8 role tiers: superadmin, admin, instructor, red, blue, analyst, student, guest
- Row-level permissions
- API-layer enforcement

## Network Isolation
- Isolated VLANs per scenario
- Egress filtering via controlled NAT
- Malware sandboxing in dedicated VM pools

## Data Protection
- Database credentials in Vault/K8s Secrets
- Encrypted sensitive fields (JSONB metadata)
- Audit logs (immutable, append-only)

## Hardening Checklist
- [ ] Change default admin password
- [ ] Configure firewall rules
- [ ] Enable HTTPS (TLS 1.3)
- [ ] Set up Vault for secrets
- [ ] Enable audit logging
- [ ] Configure backups
- [ ] Set up monitoring alerts
- [ ] Run security scans (Trivy, Snyk)

## Compliance
- OWASP Top 10 mitigations
- WCAG AA accessibility
- SOC 2 Type II ready (with proper configuration)
