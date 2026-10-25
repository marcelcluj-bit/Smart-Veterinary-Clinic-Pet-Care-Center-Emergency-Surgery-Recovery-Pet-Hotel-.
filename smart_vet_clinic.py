import time
import json
import random
from datetime import datetime

class SmartVetClinicAI:
    """
    AI-driven ICU vital sign telemetry, automated triage/scheduling, 
    and Web3 RWA Tokenomics for modern Veterinary Clinics & Pet Care Centers.
    """
    def __init__(self, icu_capacity=10, general_wards=30):
        self.icu_capacity = icu_capacity
        self.general_wards = general_wards
        self.active_icu_patients = {}
        self.sensor_data_history = []
        
    def admit_patient(self, pet_id: str, species: str, owner_wallet: str, condition: str, is_critical: bool):
        """
        Admits a pet into either ICU or general wards based on clinical triage.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ward_type = "ICU" if is_critical else "GENERAL_WARD"
        
        if is_critical and len(self.active_icu_patients) >= self.icu_capacity:
            return {"timestamp": timestamp, "status": "DENIED_ICU_FULL", "message": "Transfer to partner facility required."}
            
        patient_record = {
            "timestamp": timestamp,
            "pet_id": pet_id,
            "species": species,
            "owner_wallet": owner_wallet,
            "condition": condition,
            "assigned_ward": ward_type,
            "status": "ADMITTED"
        }
        
        if is_critical:
            self.active_icu_patients[pet_id] = patient_record
            
        return patient_record

    def read_icu_vitals_iot(self, pet_id: str):
        """
        Simulates IoT collar/cage sensor telemetry tracking pet vital signs in ICU.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Simulated vitals based on species average (e.g., canine/feline)
        heart_rate = round(random.uniform(70, 140), 0)
        body_temp = round(random.uniform(37.5, 39.5), 1)
        oxygen_spo2 = round(random.uniform(92.0, 99.5), 1)
        
        telemetry = {
            "timestamp": timestamp,
            "pet_id": pet_id,
            "heart_rate_bpm": heart_rate,
            "body_temperature_celsius": body_temp,
            "oxygen_spo2_percent": oxygen_spo2
        }
        
        # AI Critical Alert Logic
        alerts = []
        if oxygen_spo2 < 94.0:
            alerts.append("CRITICAL_ALERT: Low blood oxygen (SpO2) detected!")
        if body_temp > 39.2 or body_temp < 37.8:
            alerts.append("WARNING: Abnormal body temperature detected.")
            
        telemetry["alerts"] = alerts if alerts else ["VITALS_STABLE"]
        self.sensor_data_history.append(telemetry)
        return telemetry

    def simulate_vet_tokenomics(self, monthly_clinic_revenue_usd: float, total_equipment_tokens: int = 500_000):
        """
        Calculates Web3 equipment fractional ownership yield distribution for medical investors.
        """
        # Allocates 15% of monthly revenue as equipment lease dividends to token holders
        dividend_pool_usd = monthly_clinic_revenue_usd * 0.15
        yield_per_token_usd = dividend_pool_usd / total_equipment_tokens
        
        return {
            "monthly_clinic_revenue_usd": monthly_clinic_revenue_usd,
            "equipment_dividend_pool_usd": round(dividend_pool_usd, 2),
            "total_equipment_tokens": total_equipment_tokens,
            "yield_per_token_usd": round(yield_per_token_usd, 6),
            "smart_contract_status": "READY_FOR_DISTRIBUTION"
        }

# Execution Entry Point
if __name__ == "__main__":
    vet_system = SmartVetClinicAI()
    
    print("=== 1. PATIENT ADMISSION & TRIAGE ===")
    admission = vet_system.admit_patient(
        pet_id="PET-DOG-REX-01",
        species="Canine",
        owner_wallet="0x42109A3B...F219",
        condition="Post-operative trauma recovery",
        is_critical=True
    )
    print(json.dumps(admission, indent=2))
    
    print("\n=== 2. ICU IOT VITAL SIGNS TELEMETRY ===")
    vitals = vet_system.read_icu_vitals_iot("PET-DOG-REX-01")
    print(json.dumps(vitals, indent=2))
    
    print("\n=== 3. RWA EQUIPMENT TOKENOMICS & YIELD DISTRIBUTION ===")
    tokenomics = vet_system.simulate_vet_tokenomics(monthly_clinic_revenue_usd=65000.0)
    print(json.dumps(tokenomics, indent=2))
