*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  keijo
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Registration Should Succeed

Register With Special Character In Password
    Set Username  keijo
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Registration Should Succeed

Register With Password And Confirmation That Differ
    Set Username  keijo
    Set Password  kalle123
    Set Password Confirmation  kalle456
    Click  button >> text=Register
    Registration Should Fail With Message  Password and confirmation do not match

Register With Password Containing Only Lowercase Letters
    Set Username  keijo
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Registration Should Fail With Message  Password must contain a non-letter character

Register With Password Containing Only Mixed Case Letters
    Set Username  keijo
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Registration Should Fail With Message  Password must contain a non-letter character


Register With Too Short Username And Valid Password
    Set Username  ok
    Set Password  keijo123
    Set Password Confirmation  keijo123
    Click  button >> text=Register
    Registration Should Fail With Message  Username must be atleat 3 characters long

Register With Valid Username And Too Short Password
    Set Username  keijo
    Set Password  keijo12
    Set Password Confirmation  keijo12
    Click  button >> text=Register
    Registration Should Fail With Message  Password must be atleat 8 characters long

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  keijo123
    Set Password Confirmation  keijo123
    Click  button >> text=Register
    Registration Should Fail With Message  Username already taken


*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
