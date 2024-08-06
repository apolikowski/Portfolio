*** Settings ***
Resource    ../Resources/base.resource

*** Variables ***
${Let Me Hack Btn}    class:btn btn-primary

*** Test Cases ***
Test Case
    Open Browser And URL
    Click Element        ${Let Me Hack Btn}

