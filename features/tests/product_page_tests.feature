
Feature: Product page tests

  Scenario: User can add a product to a cart
    Given Open Product Details page
    When Click to add product to cart
    And Verify VIEW CART confirmation is shown
    And Click "View my cart"
    Then Verify Your cart is visible