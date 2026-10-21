# Nocturnal SpO2 Oxygen Desaturation & ODI Sleep Apnea Screener Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Oxygen Desaturation Index (ODI3/ODI4), SpO2 dip nadir and duration, pulse rate variability nocturnal arousal proxy, and sleep quality index. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_oxygen_desaturation_index`: Compute ODI3 (events/hr with >= 3% SpO2 drop) and lowest nocturnal nadir from pulse oximetry time series.
- `classify_nocturnal_hypoxemia_severity`: Classify sleep apnea risk tier (Mild, Moderate, Severe) and recommend clinical polysomnography urgency.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_sleep_apnea_desaturation_screener_skill.server --test
```
