#
Feature: Roi Calculator


  Scenario: User can input value into total field area
    Given Open calculator page
    When Scroll down to calculator section
    When Enter 2000 into input field
#    Then Verify 2000 was added
    When Click Total Benefits button

  Scenario: Verify User CAN NOT input negative num in total field area
    Given Open calculator page
    When Scroll down to calculator section
    When Enter -1 into input field
    Then Verify User CAN NOT input negative num in total field area
#
  Scenario: Verify User CAN NOT input symbols in total field area
    Given Open calculator page
    When Enter . into input field
    Then Verify User CAN NOT input symbols in total field area
#
  Scenario: Verify User CAN NOT input letters in total field area
    Given Open calculator page
    When Enter e into input field
    Then Verify User CAN NOT input letters in total field area
#
  Scenario: Verify user can choose Northern IA/Southern MN Region
    Given Open calculator page
    When Scroll down to calculator section
    And Click on Region Menu
    And Click on Northern IA/Southern MN Region
    And Click Total Benefits button
    Then Verify User can see the result popup

  Scenario: Verify user can see Soil type tooltip
    Given Open calculator page
    When Hover over Soil type tooltip
#    Then Verify User can see tooltips text







