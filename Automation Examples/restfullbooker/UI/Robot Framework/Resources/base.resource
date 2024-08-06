*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${Restfull Booker App-Url}       https://automationintesting.online/
${Browser}                       Chrome
${Title}                         Restful-booker-platform demo

*** Keywords ***
Open Browser And URL
    Open Browser    ${Restfull Booker App-Url}     ${Browser}
    Title Should Be    ${Title}