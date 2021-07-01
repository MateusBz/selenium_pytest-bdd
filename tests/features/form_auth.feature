Feature: Log in to the application

    I want to test logging in at the-internet.herokuapp.com
    
    Scenario Outline: Logging test
        Given I go to "login"
        When I enter <user_name> into "Username" input
        And I enter <password> into "Password" input
        And I click on "Login"
        Then <message> is shown

        Examples:
            | user_name | password                  | message                           |
            |           |                           | Your username is invalid!         |
            | tomsmith  | 1234                      | Your password is invalid!         |
            | 1234      | SuperSecretPassword!      | Your username is invalid!         |
            | tomsmith  | SuperSecretPassword!      | You logged into a secure area!    |

