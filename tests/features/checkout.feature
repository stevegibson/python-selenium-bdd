Feature: Test the checkout flow

  Scenario: Add an item to the cart and complete the checkout flow
    Given I am logged in to the saucedemo site using the standard user account
    When I add an item to the cart
    Then I should be able to complete the checkout process

  Scenario: Add two items to the cart and verify the total is correct in the cart
    Given I am logged into the saucedemo site using the standard user account
    When I add two items to the cart
    Then I should see the correct total price on the cart page
  