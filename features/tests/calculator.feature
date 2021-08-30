#
Feature: Roi Calculator


  Scenario: User can input value into total field area
    Given Open calculator page
    When Enter 1000 into input field
    When Click Total Benefits button
    Then Verify User can see the result popup


  Scenario: Verify that the user only can input numbers in total field are
    Given Open calculator page
    Then Verify the tag has the number attribute


  Scenario Outline: Verify user can see tooltip
    Examples:
    |section|

    |Information|
    |Willing to implement|
    Given Open calculator page
    When Hover over <section> tooltip
    #Then Verify User can see tooltips text

  Scenario Outline: User can click over my farm information section
    Examples:
    |form_section|
    |Information: Soil type|
    |Information: Crop type|
    |Information: Crop type|
    |Currently practicing: Tillage management|
    |Currently practicing: Cover crops|
    |Currently practicing: Nitrogen efficiency practices|
    |Willing to implement: Tillage management|
    |Willing to implement: Cover crops|
    |Willing to implement: Type of cover crop|
    |Willing to implement: Nitrogen efficiency practices|
    Given Open calculator page
    Then click over form <form_section> section

  Scenario Outline: User can click over Region drop-down menu
    Examples:
      |region|
      |Region name: Northern IA/Southern MN Region|
      |Region name: Southern IA/Northern MO|
    Given Open calculator page
    Then click over region option <region>



