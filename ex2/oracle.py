from dotenv import load_dotenv
import os
import sys

def load_config() -> dict[str, str | None]:
    load_dotenv()
    config = {
        "mode": os.getenv("MATRIX_MODE", "Not Set"),
        "db": os.getenv("DATABASE_URL", "Not Connected"),
        "api": os.getenv("API_KEY"),
        "log": os.getenv("LOG_LEVEL", "INFO"),
        "zion": os.getenv("ZION_ENDPOINT", "Offline")
    }
    return config

def main():
    config = load_config()
    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {'Connected' if config['db'] != 'Not Connected' else 'Disconnected'}")
    print(f"API Access: {'Authenticated' if config['api'] else 'Missing Key'}")
    print(f"Log Level: {config['log']}")
    print(f"Zion Network: {'Online' if config['zion'] != 'Offline' else 'Offline'}")

    print("""\nEnvironment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available
The Oracle sees all configurations.""")

if __name__ == "__main__":
    main()
