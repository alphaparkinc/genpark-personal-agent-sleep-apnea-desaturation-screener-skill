# -*- coding: utf-8 -*-
"""Nocturnal SpO2 Desaturation Screener for GenPark Personal Agent."""
import json
from typing import Dict, Any, List

class NocturnalSpO2DesaturationScreener:
    @staticmethod
    def calculate_oxygen_desaturation_index(spo2_time_series_readings: List[float], sleep_duration_hours: float) -> Dict[str, Any]:
        if not spo2_time_series_readings or sleep_duration_hours <= 0:
            return {"error": "Invalid telemetry inputs."}
            
        nadir = min(spo2_time_series_readings)
        mean_spo2 = round(sum(spo2_time_series_readings) / len(spo2_time_series_readings), 1)
        
        # Count drops >= 3% from local rolling baseline
        desat_events = 0
        baseline = spo2_time_series_readings[0]
        for val in spo2_time_series_readings:
            if baseline - val >= 3.0:
                desat_events += 1
                baseline = val
            elif val > baseline:
                baseline = val
                
        odi3 = round(desat_events / sleep_duration_hours, 1)
        return {
            "sleep_duration_hours": sleep_duration_hours,
            "mean_spo2_pct": mean_spo2,
            "nadir_spo2_pct": nadir,
            "desaturation_event_count": desat_events,
            "odi3_events_per_hour": odi3
        }

    @staticmethod
    def classify_nocturnal_hypoxemia_severity(odi_score: float, lowest_spo2_pct: float, time_below_90_pct: float = 0.0) -> Dict[str, Any]:
        if odi_score >= 30.0 or lowest_spo2_pct < 80.0 or time_below_90_pct > 10.0:
            tier = "SEVERE_SLEEP_APNEA_SUSPECTED"
            referral = "URGENT_PULMONOLOGY_SLEEP_LAB"
        elif odi_score >= 15.0 or lowest_spo2_pct < 85.0:
            tier = "MODERATE_OBSTRUCTIVE_SLEEP_APNEA"
            referral = "HOME_SLEEP_TEST_RECOMMENDED"
        elif odi_score >= 5.0:
            tier = "MILD_DESATURATION"
            referral = "LIFESTYLE_POSITIONAL_THERAPY"
        else:
            tier = "PHYSIOLOGICAL_NORMAL"
            referral = "ROUTINE_MONITORING"
            
        return {
            "odi_score": odi_score,
            "nadir_spo2": lowest_spo2_pct,
            "clinical_hypoxemia_tier": tier,
            "diagnostic_recommendation": referral,
            "positional_countermeasure": "Trial side-sleeping positional pillow or Mandibular Advancement Device (MAD)."
        }
