Feature: Test
	As someone new to testing
	So I can learn behavior driven development
	I want to write some scenarios
 
        Scenario: I can view the home page
                Given I am at "http://127.0.0.1:9000/home/"
                Then I should see "Hello home world!"
        Scenario: I can view the help page
                Given I am at "http://127.0.0.1:9000/help/"
                Then I should see "Hello help world!"
        Scenario: I can view the test page
                Given I am at "http://127.0.0.1:9000/about/"
                Then I should see "Hello about world!"
