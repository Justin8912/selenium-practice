import {Builder, By, WebDriver} from 'selenium-webdriver';
import chrome from 'selenium-webdriver/chrome.js';

(async function(){
    const link = "https://google.com";
    let driver = await chrome.Driver.createSession();

    await driver.get(link);
    await driver.manage().setTimeouts({implicit:1000});
    const actions = driver.actions({async: true});
    let searchBar = await driver.findElement(By.css('textarea'));
    let searchButton = await driver.findElement(By.name("btnK"));
    searchBar.sendKeys("Selenium yay!");
    // await searchButton.click();
    // await searchButton.press().perform();
    await driver.quit();
})()
