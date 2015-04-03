from lettuce import world, step

@step(u'I am at "([^"]*)"')
def i_am_at_url(step, url):
    world.browser.get(url)
    

@step(u'I should see "([^"]*)"')
def i_should_see_content(step, content):
	if content not in world.browser.find_element_by_id("content").text:
		raise Exception("Content not found.")
