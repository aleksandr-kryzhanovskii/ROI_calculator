#
Feature: Roi Calculator


  Scenario: User can input value into total field area
    Given Open calculator page
    When Scroll down to calculator section
    When Enter 1000 into input field
    When Click Total Benefits button
    Then Verify User can see the result popup


  Scenario: Verify User CAN NOT input negative num in total field area
    Given Open calculator page
    When Scroll down to calculator section
    When Enter e into input field
    Then Verify letters was NOT added to search field


  Scenario: Verify User CAN NOT input 0 num in total field area
    Given Open calculator page
    When Scroll down to calculator section
    When Enter 0 into input field
    Then Verify 0 was NOT added to search field


  Scenario: Verify User CAN NOT input symbols num in total field area
    Given Open calculator page
    When Scroll down to calculator section
    When Enter . into input field
    Then Verify symbol was NOT added to search field

  Scenario: Verify User CAN NOT input letters in total field area
    Given Open calculator page
    When Enter e into input field
    Then Verify letters was NOT added to search field

  Scenario: Verify user can choose Northern IA/Southern MN Region
    Given Open calculator page
    When Scroll down to calculator section
    When Enter 3000 into input field
    And Click on Region Menu
    And Click on Northern IA/Southern MN Region
    And Click Total Benefits button
    Then Verify User can see the result popup

  Scenario: Verify user can see Soil type tooltip
    Given Open calculator page
    When Hover over Soil type tooltip
    Then Verify User can see tooltips text

  Scenario Outline: User can click over my farm information section
    Examples:
    |form_section|
    |Information: Soil type|
    |Information: Crop type|
    |Currently practicing: Tillage management|
    |Currently practicing: Cover crops|
    |Currently practicing: Nitrogen efficiency practices|
    |Willing to implement: Tillage management|
    |Willing to implement: Cover crops|
    |Willing to implement: Type of cover crop|
    |Willing to implement: Nitrogen efficiency practices|
    Given Open calculator page
    When Scroll down to calculator section
    Then click over form <form_section> section







