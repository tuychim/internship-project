Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


  Scenario: User can open market tab and filter by developers option
    Given Open the main page.
    And Sign in
    When  Click on “market” at the left side menu
    When Verify the right page opens
    When Click on Developers filter at the top of the page
    Then Verify all cards has the license tag



Scenario: User can click on verifications settings option and verify the right page opens
  Given Open the main page.
    And Sign in
    When Click on “settings” at the left side menu.
    When Click on the verification option.
    When Verify the right page opens.
    Then Verify “upload image” and “Next step” buttons are available.


Scenario:  User can open market tab and go through the pagination
  Given Open the main page
    And Sign in
    When Click on “market” at the left side menu.
    When Verify the right page opens..
    When Go to the final page using pagination.
    Then Go to the first page using pagination.



  Scenario: User can go to settings and edit the personal information
    Given Open sign in page
    When Click on settings option
    When Click on Edit profile option
    When Enter test data into the name field
    When Enter test data into the phone number field
    Then Check the right information is present in the name input fields
    Then Check the right information is present in the phone number input field
    Then Check “Save Changes” button is available and clickable
    Then Check “Close” button is available and clickable


  Scenario: User can change the language from the page
    Given Open the main page.
    When  Log in to the page
    When Click on Main menu
    When Change the language of the page to Russian. The option will be “RU” which is the list of the languages
    Then Verify the language has changed