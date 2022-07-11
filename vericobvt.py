#Sample automation for initial Post Deployment Verfication
#Based on Python/Playwright framework with py-test

from playwright.sync_api import sync_playwright
from models.add_user import AddUser
import pytest
import os
import json



testenv = os.environ['PYTEST_BASE_URL'] #Global Test BASE URL - note:pytest_base_url not really working

#hooks for console, request and response
def log_console(msg):
    print("in console: " + msg.type + " " +msg.text)

def log_request(requestfinished):
    print("REQUEST: ")
    headers = requestfinished.headers
    print(headers)

def log_response(response):
    print("REPSONSE: ")
    respheader = response.headers
    print(respheader)



#Login Fixture - gets login/session for rest of the tests
@pytest.fixture(scope='module')

def vericol_session():
    """Create Concur Login Session for use with additional tests

    Sets up Playwright browser and new_page for use with additional tests"""

    p = sync_playwright().start()
    browser_type = p.chromium
    #browser_type = p.firefox
    #browser_type = p.webkit

    browser = browser_type.launch(headless=False,devtools=False)
    # browser.start_tracing(path='/Users/i857921/trace.json')
    #
    #browser = browser.new_context(record_har_path='/Users/i857921/har')
    page = browser.new_page(record_har_path='/Users/johnraymond/har/test.har')

# Turn on hooks for response, console and request

    page.on('console', log_console) #send page console messages to log_console
    #page.on('requestfinished', log_request)
    #page.on('response', log_response)
    #page.on("response", lambda response: print("<<", response.status, response.url, response.all_headers().get("date")))
    #page.on("requestfailed ", lambda request: print(request.url + ":" + request.failure))

    page.goto(testenv)
    page.wait_for_load_state()
    un = os.environ['USERNAME']
    pw = os.environ['PW']
    page.fill("id=cp_master_txt_username", un)


    page.wait_for_load_state()
    page.fill("id=cp_master_txt_password", pw)
    page.click("id=cp_master_lbtn_login")


#Yield connection to rest of tests / includes session info
    yield page



def test_workforce_project(vericol_session):
    """Simple Workforce Project Screen Rendered Test"""

    vericol_session.goto(testenv + "workforce/project")
    vericol_session.wait_for_load_state('domcontentloaded')

    assert vericol_session.wait_for_selector("id=cp_master_srt_project_manager_lbl_sort_label")

def test_workforce_vacancy(vericol_session):
    """Simple Workforce Vacancy Screen Rendered Test"""

    vericol_session.goto(testenv + "workforce/vacancy")
    vericol_session.wait_for_load_state('domcontentloaded')

    assert vericol_session.wait_for_selector("id=cp_master_srt_organization_internal_short_name_with_parent_lbl_sort_label")

def test_workforce_assignment(vericol_session):
    """Simple Workforce Assignment Screen Rendered Test"""

    vericol_session.goto(testenv + "workforce/assignment")
    vericol_session.wait_for_load_state('domcontentloaded')

    assert vericol_session.wait_for_selector("id=cp_master_srt_project_assignment_identifier_lbl_sort_label")

def test_workforce_people(vericol_session):
    """Simple Workforce People Screen Rendered Test"""

    vericol_session.goto(testenv + "workforce/people")
    vericol_session.wait_for_load_state('domcontentloaded')

    assert vericol_session.wait_for_selector("id=cp_master_srt_employee_id_lbl_sort_label")

def test_workforce_planner(vericol_session):
    """Simple Workforce Planner Screen Rendered Test"""

    vericol_session.goto(testenv + "workforce/planner/board")
    vericol_session.wait_for_load_state('domcontentloaded')

    assert vericol_session.wait_for_selector("id=cp_master_lbtn_reset")


def test_add_person(vericol_session):
    """ Simple Add Person Test"""

    add_user = AddUser(vericol_session)
    add_user.navigate()

    add_user.add_new_user()



def test_workforce_report(vericol_session):
    """Simple Workforce Planner Screen Rendered Test"""

    vericol_session.goto(testenv + "report")
    vericol_session.wait_for_load_state('domcontentloaded')

    assert vericol_session.wait_for_selector("id=cp_master_lbl_action_title")

def test_workforce_lead(vericol_session):
    """Simple Workforce People Screen Rendered Test"""

    vericol_session.goto(testenv + "lead")
    vericol_session.wait_for_load_state('domcontentloaded')

    assert vericol_session.wait_for_selector("id=cp_master_srt_lead_phase__code_value_lbl_sort_label")

def test_workforce_people_list(vericol_session):
    """Simple Workforce People Screen Rendered Test"""

    vericol_session.goto(testenv + "workforce/people")
    vericol_session.wait_for_load_state('domcontentloaded')
    assert vericol_session.wait_for_selector("id=cp_master_srt_employee_id_lbl_sort_label")
    peeps = vericol_session.locator("tbody")

    print("TESTERPEEPS")
    print(peeps)