Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


  Scenario: User can filter by sale status Last Units
    Given Open the main page
    When Log in to the page
    When Click on “'off plan” at the left side menu
    When Verify the right page opens
    When Filter by sale status of “Last Units”
    Then Verify each product contains the Last Units tag



  Scenario: The user can enter the information into the input fields on the registration page
    Given Open the registration page or sign up page
    When Enter some test information in the input fields.
    Then Verify the right information is present.


  Scenario: The user can click on “Connect the company” on the left side of the main page
    Given Open sign in page
    When  Log in to the page.
    When Click on “Connect the company"
    When Switch the new tab.
    Then Verify the right tab opens
