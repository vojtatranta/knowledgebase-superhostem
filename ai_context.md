# Superhostem.cz — AI Context

This document provides context for AI coding agents working on the **Superhostem.cz** project.

Its goal is to ensure that AI agents understand:

* the purpose of the system
* core architectural principles
* expected coding philosophy
* the core data model

Agents should read this document together with **project.md (PDE)** before generating code.

---

# System Purpose

Superhostem.cz is a platform for **short-term rental hosts in the Czech Republic**.

The system provides a central dashboard where hosts can:

* track reservations
* see estimated revenue
* manage properties
* simplify administrative work

The platform integrates reservation data from booking platforms such as Airbnb and Booking.com using **iCal feeds and parsed booking emails**.

The system's purpose is **operational clarity and automation**, not replacing OTA platforms.

---

# Key Product Principles

AI agents should design solutions that follow these principles.

### Simplicity First

Prefer simple solutions over complex architectures.

Avoid unnecessary abstractions or premature scaling.

---

### Automation Over Manual Work

Features should reduce manual work for hosts.

If a process can be automated, it should be automated.

---

### Minimal Dependencies

Avoid unnecessary external dependencies.

Prefer stable, widely used libraries.

---

### Data Reliability

Reservation and revenue data must be handled carefully.

The system should prioritize **data correctness over UI complexity**.

---

# Core System Workflow

The platform works by combining two sources of information.

## Calendar Data

Reservation dates are imported through **iCal feeds**.

These provide:

* reservation dates
* blocked calendar periods

But they do not include financial information.

---

## Email Parsing

Hosts forward booking emails from platforms such as Airbnb.

The system parses emails to extract:

* booking price
* fees
* booking identifiers

These emails are matched with reservations imported from iCal feeds.

This allows the system to reconstruct **revenue per reservation**.

---

# Core Entities

AI agents should design data structures around the following core entities.

User
Represents a platform account.

Property
A rental unit owned or managed by the user.

Calendar
iCal feed connected to a property.

Reservation
A booking detected via calendar data.

Email
Forwarded booking email containing financial information.

Revenue
Financial information associated with a reservation.

Subscription
Billing record for the platform subscription.

Ambassador
User who referred other customers to the platform.

---

# Key Relationships

Typical relationships between entities:

User → owns → Properties

Property → connected to → Calendar

Calendar → generates → Reservations

Reservation → matched with → Email

Email → produces → Revenue data

User → has → Subscription

User → may be referred by → Ambassador

---

# Expected Architecture Approach

AI agents should prefer architectures that are:

* modular
* easy to maintain
* easy to extend

Avoid overly complex enterprise-style architectures.

Focus on **clear service boundaries** and **clean data flow**.

---

# API Design Guidelines

When generating APIs:

* use clear resource names
* follow REST-style patterns
* prefer predictable endpoints

Example pattern:

/properties
/reservations
/revenue
/subscriptions

Avoid deeply nested or overly complex endpoints.

---

# Database Design Philosophy

The database should prioritize:

* clarity
* strong relationships
* easy querying

Prefer:

* normalized structures
* clear foreign keys
* explicit entity relationships

Avoid unnecessary polymorphism or complex inheritance models.

---

# Development Stage

The project is currently in **MVP stage**.

Priority is building the core operational system.

Important MVP capabilities:

* iCal ingestion
* email parsing
* reservation detection
* revenue reconstruction
* dashboard visibility

AI agents should avoid implementing features unrelated to these goals.

---

# Non-Goals (For Now)

The system does NOT aim to:

* replace Airbnb or Booking
* manage guest messaging
* provide OTA channel management
* support global markets yet

Focus is **Czech hosts and operational visibility**.

---

# Coding Expectations

Generated code should be:

* readable
* well structured
* minimal
* production oriented

Avoid:

* unnecessary abstractions
* speculative scalability
* overly complex frameworks

Prefer solutions that a **small engineering team can maintain easily**.

---

# Long-Term Vision

Superhostem.cz aims to become the **operational backbone for short-term rental hosts in the Czech Republic**.

Future features may include:

* accounting exports
* regulatory reporting
* VAT summaries
* administrative tools

However, these features should only be implemented **after the MVP operational core is stable**.
