Feature: Context Menu

    I want to test the display of context menu add-ons that appear in a right-click menu.

    Scenario: Right-click menu
        Given I go to "context_menu"
        When I right click in the dotted line box
        Then The alert "You selected a context menu" is shown
