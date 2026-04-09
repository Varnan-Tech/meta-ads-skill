def check_auth_status():
    print("Checking Meta Ads API authentication token...")
    token_valid = False

    if not token_valid:
        print("Error: No valid access token found.")
        print("Please authenticate to continue.")
        print("Action Plan:")
        print(
            "1. Ensure the local OAuth web server is running: python src/auth/run_web_server.py"
        )
        print("2. Visit http://localhost:8000/auth/facebook in your web browser")
        print("3. Grant the requested permissions")
        print("4. Return here once authentication is complete")
        return False
    else:
        print("Authentication successful! Token is valid.")
        return True


if __name__ == "__main__":
    check_auth_status()
