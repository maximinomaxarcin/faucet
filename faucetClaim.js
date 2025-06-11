const puppeteer = require('puppeteer');

const accounts = [
    { privateKey: 'your_private_key1', proxy: 'http://user:pass@proxy1:port' },
    { privateKey: 'your_private_key2', proxy: 'http://user:pass@proxy2:port' },
    // Add more accounts and proxies as needed
];

async function claimFaucet(account) {
    const browser = await puppeteer.launch({
        headless: true, // Set to false if you want to see the browser
        args: [`--proxy-server=${account.proxy}`]
    });

    const page = await browser.newPage();
    await page.goto('https://testnet.pharosnetwork.xyz/');

    // Connect Wallet (this part may vary based on the wallet implementation)
    await page.evaluate((privateKey) => {
        // Replace this with the actual function to connect the wallet
        // Example: connectWallet(privateKey);
        console.log(`Connecting wallet with private key: ${privateKey}`);
    }, account.privateKey);

    // Wait for 20 seconds after connecting the wallet
    await page.waitForTimeout(20000);

    // Claim Faucet
    try {
        const claimButton = await page.waitForSelector('button:contains("Claim Faucet")', { timeout: 10000 });
        await claimButton.click();
        console.log("Faucet claimed successfully!");
    } catch (error) {
        console.error("Error claiming faucet:", error);
    }

    await page.waitForTimeout(5000); // Wait for the claim to process
    await browser.close();
}

(async () => {
    for (const account of accounts) {
        await claimFaucet(account);
    }
})();
