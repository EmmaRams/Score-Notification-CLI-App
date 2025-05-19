"""
Live Sports Score CLI Notifier
"""
import requests
import time
import argparse
from datetime import datetime
from typing import Dict, List

# Configuration
API_KEY = "your_api_key_here"  # Get from https://www.api-sports.io/
BASE_URL = "https://v1.rugby.api-sports.io"
POLL_INTERVAL = 60  # Seconds between checks
FAVORITE_TEAMS = ["France", "New Zealand"]  # Customize your teams

def get_live_matches() -> List[Dict]:
    """Get live matches from API"""
    headers = {"x-rapidapi-key": API_KEY}
    params = {"live": "all"}
    
    try:
        response = requests.get(
            f"{BASE_URL}/games",
            headers=headers,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()["response"]
    except (requests.RequestException, KeyError):
        return []

def display_match(match: Dict) -> str:
    """Format match data for display"""
    return (
        f"{match['teams']['home']['name']} {match['scores']['home']} - "
        f"{match['scores']['away']} {match['teams']['away']['name']}\n"
        f"Status: {match['status']['long']} | Time: {match['status']['timer']}\n"
        f"League: {match['league']['name']}"
    )

def monitor_scores():
    """Monitor and display score updates"""
    previous_matches = []
    
    while True:
        current_matches = get_live_matches()
        new_updates = [
            m for m in current_matches
            if m not in previous_matches
            or any(m['teams'][t]['id'] in FAVORITE_TEAMS 
                for t in ['home', 'away'])
        ]

        if new_updates:
            print(f"\n{'-'*40}")
            print(f"Update at {datetime.now().strftime('%H:%M:%S')}")
            for match in new_updates:
                print("\n" + display_match(match))
            print(f"{'-'*40}\n")

        previous_matches = current_matches
        time.sleep(POLL_INTERVAL)

def main():
    """CLI interface"""
    parser = argparse.ArgumentParser(
        description="Live Sports Score Notifier",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-s", "--sport",
        choices=["rugby", "football", "basketball"],
        default="rugby",
        help="Sport to monitor"
    )
    parser.add_argument(
        "-i", "--interval",
        type=int,
        default=POLL_INTERVAL,
        help="Update interval in seconds"
    )

    args = parser.parse_args()
    
    print(f"Starting live score monitor for {args.sport}...")
    print("Ctrl+C to exit\n")
    
    try:
        monitor_scores()
    except KeyboardInterrupt:
        print("\nMonitoring stopped")

if __name__ == "__main__":
    main()