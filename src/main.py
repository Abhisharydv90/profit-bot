import time
import json
from datetime import datetime

def track_profit():
    with open('config/settings.json', 'r') as f:
        config = json.load(f)
    
    profit = 0
    start_time = datetime.now()
    
    while True:
        # Simulate profit generation
        profit += 0.01  # $0.01 per second
        
        if profit >= config['profit_target']:
            print(f"Target reached! ${profit:.2f}")
            break
            
        time.sleep(1)

if __name__ == "__main__":
    track_profit()
