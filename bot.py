import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Function to claim faucet
def claim_faucet(private_key, proxy):
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.add_argument('--headless')  # Run in headless mode

    driver = webdriver.Chrome(service=Service('path/to/chromedriver'), options=chrome_options)
    driver.get('https://testnet.pharosnetwork.xyz/')

    # Connect wallet (this part may vary based on the wallet implementation)
    # Example: driver.execute_script("connectWallet();") 

    time.sleep(20)  # Wait for 20 seconds after connecting the wallet

    # Claim faucet
    try:
        claim_button = driver.find_element(By.XPATH, '//button[text()="Claim Faucet"]')
        claim_button.click()
        print("Faucet claimed successfully!")
    except Exception as e:
        print(f"Error claiming faucet: {e}")

    time.sleep(5)  # Wait for the claim to process
    driver.quit()

# Main execution
if __name__ == "__main__":
    private_keys = ['your_private_key1', 'your_private_key2']  # Add your private keys
    # Proxies with authentication in the format username:password@ip_address:port
    proxies = ['user:pass@192.168.1.1:8080', 'user:pass@192.168.1.2:8080']  # Replace with your actual proxies

    for private_key, proxy in zip(private_keys, proxies):
        claim_faucet(private_key, proxy)
