
Feature: Main Page Tests

  Scenario: User can access Terms
    Given Open main page
    When Click on terms of service
    Then Verify Terms of service page opened

  Scenario: User can shop by product Face Washes
    Given Open main page
    When Click on Hamburger Menu
    And Click on "Shop by product"
    And Click on Face Washes
    Then Verify user is taken to https://shop.cureskin.com/collections/face-wash

   Scenario: User can shop by Sunscreens
     Given Open main page
     When Click on Hamburger Menu
     And Click on "Shop by product"
     And Click on Sunscreens
     And Click on first product
     Then Verify first product name has Sunscreen in it

   Scenario: User can shop by category Face
     Given Open main page
     When Click on Hamburger Menu
     And Click on "Shop by category"
     And Click on Face
     And Verify user is taken to https://shop.cureskin.com/collections/face
     And Click on first face product
     Then Verify first product name has Face in it
     
   Scenario: User can shop by category Body
     Given Open main page
     When Click on Hamburger Menu
     And Click on "Shop by category"
     And Click on Body
     Then Verify user is taken to https://shop.cureskin.com/collections/body










