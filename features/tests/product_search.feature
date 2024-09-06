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


  Scenario:  User can go to settings and edit the personal information
    Given Open sign in page
    When  Log in to the page
    When Click on settings option
    When Click on Edit profile option
    When Enter test data into the name field
    When Enter test data into the phone number field
    Then Check the right information is present in the name input fields
    Then Check the right information is present in the phone number input field
    Then Check “Save Changes” button is available and clickable
    Then Check “Close” button is available and clickable
