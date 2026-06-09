# Find-Evil: AI-Powered DFIR Investigation Agent

## Overview

Find-Evil is an AI-driven Digital Forensics and Incident Response (DFIR) assistant that automates memory dump investigations using Volatility 3 and LangGraph.

The system analyzes memory artifacts, evaluates suspicious activity, selects appropriate forensic plugins, executes investigations, and generates a structured forensic report.

## Problem Statement

Memory forensics investigations often require analysts to manually inspect multiple Volatility outputs and determine the next investigative step.

This process can be time-consuming and heavily dependent on analyst experience.

Find-Evil assists investigators by:

* Collecting forensic artifacts
* Scoring suspicious activity
* Reasoning about findings
* Selecting investigation plugins automatically
* Generating investigation reports

## Features

### Process Analysis

* Parses Volatility process listings
* Identifies suspicious processes
* Calculates suspicion scores

### Network Analysis

* Parses Volatility netscan output
* Detects listening services
* Detects network communication artifacts

### Investigation Reasoning

* Explains why processes are suspicious
* Generates human-readable reasoning

### Automated Plugin Selection

Based on observed evidence, the agent automatically selects an appropriate Volatility plugin.

Examples:

* windows.cmdline
* windows.netscan

### Report Generation

Generates structured investigation reports containing:

* Process findings
* Network findings
* Suspicion score
* Investigation reasoning
* Plugin output preview

## Architecture

Memory Dump

↓

Volatility 3

↓

Artifact Collection

↓

LangGraph Investigation Agent

↓

Reasoning Engine

↓

Plugin Selection

↓

Investigation Report

## Technologies Used

* Python
* LangGraph
* Volatility 3
* Git
* SIFT Workstation

## Project Structure

find-evil/

├── agent/

│ ├── graph.py

│ ├── nodes.py

│ └── state.py

├── parser.py

├── network_parser.py

├── volatility_runner.py

├── main.py

└── investigation_report.txt

## Architecture
                  +------------------+
                  |  Memory Dump     |
                  | (.raw/.mem file) |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  |   Volatility 3   |
                  +--------+---------+
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
 +------------------+             +------------------+
 | windows.pslist   |             | windows.netscan  |
 +--------+---------+             +--------+---------+
          |                                 |
          v                                 v
 +------------------+             +------------------+
 | Process Parser   |             | Network Parser   |
 +--------+---------+             +--------+---------+
          |                                 |
          +----------------+----------------+
                           |
                           v
                  +------------------+
                  | LangGraph Agent  |
                  +--------+---------+
                           |
      +--------------------+--------------------+
      |                    |                    |
      v                    v                    v
+-------------+   +---------------+   +----------------+
| Score Node  |   | Reasoning Node|   | Decision Node  |
+------+------+   +-------+-------+   +--------+-------+
       |                  |                    |
       +------------------+--------------------+
                           |
                           v
                  +------------------+
                  | Plugin Selection |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | windows.cmdline  |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Report Generator |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Investigation    |
                  | Report (.txt)    |
                  +------------------+
## Running the Project

Generate Volatility outputs:

```bash
windows.pslist > pslist_output.txt
windows.netscan > netscan_output.txt
```

Run the agent:

```bash
python3 main.py
```

Generated report:

```text
investigation_report.txt
```

## Future Improvements

* Multi-stage investigations
* Timeline reconstruction
* Additional Volatility plugins
* Malware artifact detection
* Interactive analyst dashboard

## Author

Aadya Nair

