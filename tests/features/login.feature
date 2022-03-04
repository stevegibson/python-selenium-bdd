Feature: Make sure users can login to the saucedemo site

  Scenario: Log in using the standard username and password
    Given I navigate to the saucedemo site
    When I log in using the standard username and password
    Then I should see the inventory page
 