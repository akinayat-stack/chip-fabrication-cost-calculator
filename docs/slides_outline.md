# Revised Defense Slides Outline
## 1. Project Overview & Economic Value

Title: Chip Fabrication Cost Calculator.

Core Value: Interactive tool evaluating the economic feasibility of semiconductor manufacturing, specifically comparing Monolithic vs. Chiplet designs (calculating DPW, yield, and cost-per-die).

## 2. System Architecture & Modular Design

Overview: Three modular blocks communicating via a cloud-ready REST API.

The Blocks:

Backend: Python Flask API for numerical models (/calculate, /compare-chiplet).

Frontend: Single-page HTML/JS application featuring a Canvas-based wafer map.

Data Layer: CSV-driven dataset (real_chips.csv) for benchmarking and scenario comparisons.

## 3. Pair 1: Backend & Mathematical Modeling

Team Members: Askhan Moldir, Kinayatova Aruzhan.

DPW & Edge Correction: Dies-per-wafer formulas utilizing circular-edge clipping and partial-die accounting for precision.

Yield Models: Implementation of the Murphy model and Bose-Einstein clustered-defect approximation.

Cost Metrics: Aggregation of wafer cost, testing, packaging, and effective cost-per-die including scrap/retest overhead.

## 4. Pair 2: Frontend & Wafer Visualization

Team Members: Bairakimova Galiya, Abdumalik Zhanerke.

User Dashboard: Parameterized inputs (wafer diameter, defect density D 
0, die size, wafer cost) for rapid iteration.

Canvas Wafer Map: Real-time rendering with clipping math to map a rectangular die grid onto a circular boundary, using yield probability to drive per-tile pass/fail coloring.

## 5. Pair 3: Data, Comparison & Documentation

Team Members: Tolegenova Moldir, Kudaibergen Nazerke.

Baseline Dataset: real_chips.csv curated with industry-standard chip specs (die dimensions, process nodes, typical costs).

Scenario Scripts: Automated batch comparisons handling monolithic vs. chiplet splits and sensitivity sweeps.

Docs & Versioning: Technical README/USAGE guides covering API contracts, mathematical equations, and Git version control.

## 6. AI Tool Integration & Engineering Aids

OpenAI Codex: Utilized for synthesizing core mathematical routines and optimizing heavy Canvas clipping loops.

Claude: Assisted with professional technical writing, editing documentation, and organizing the 6-person team structure.

## 7. Key Decisions & Technical Challenges

Platform Choice: Selected Python + Flask for rapid prototyping of numerically intensive models.

Canvas Performance: Solved the rendering latency of mapping a rectangular grid to a circular boundary using Codex-optimized loop unrolling.

Team Management: Instituted a strict two-person-per-block split to minimize code overlap and clarify ownership of the API, UI, and data layers.

## 8. Final Results & Project Summary

Outcome: A functional tool that effectively evaluates the "Monolithic vs. Chiplet" cost-benefit ratio.

Key Features: High-accuracy yield modeling, data-driven comparisons, and real-time visual feedback.

Status: Ready for deployment (Dependencies: flask, flask-cors).