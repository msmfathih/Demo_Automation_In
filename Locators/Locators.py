class Locators:

    SINGIN_BUTTON_ID = "btn1"
    USERNAME_XPATH = "//input[@placeholder='E mail']"
    PASSWORD_XPATH =  "//input[@placeholder='Password']"
    LOGIN_BUTTON_ID = "enterbtn"
    VERIFY_WRONG_EMAIL_XPATH  = "// label[ @ id = 'errormsg']"
    VERIFY_EMAIL_MESSAGE = "Invalid User Name or PassWord"
    VALID_EMAIL_ID = "email"
    INDEX_LOGIN_BUTTON_ID = "enterimg"

    """
    mouse hover
    """
    HOVER_INTERACTION_XPATH = "//a[contains(text(),'Interactions')]"
    HOVER_DRAG_DROP_XPATH  = "//a[contains(text(),'Drag and Drop')]"
    HOVER_STATIC_XPATH =  "//a[contains(text(),'Static')]"

    """
    Alert Page
    """
    SWITCH_TO_XPATH = "//a[contains(text(),'SwitchTo')]"
    ALERT_TO_XPATH = "//a[contains(text(),'Alerts')]"
    ALERT_WITH_OK_XPATH = "//button[contains(text(),'alert box:')]"
    ALERT_WITH_OK_CANCEL_XPATH = "//a[contains(text(),'Alert with OK & Cancel')]"
    ALERT_CANCEL_BUTTON_XPATH = "//button[contains(text(),'click the button to display a confirm box')]"
    #"//*[@id='CancelTab']/button"
    ALERT_TEXTBOX_XPATH = "//a[contains(text(),'Alert with Textbox')]"
    ALERT_TEXTBOX_FIELD_XPATH = "//*[@id='Textbox']/button"


    """
    Test_HomePage Property 
    """
    VERIFY_REGISTER_PAGE_TITLE = "//h1[contains(text(),'Automation Demo Site')]"
    REGISTER_PAGE_TITLE_MESSAGE = "Automation Demo Site"
    FIRST_NAME_XPATH = "//input[@placeholder='First Name']"
    LAST_NAME_XPATH = "//input[@placeholder='Last Name']"
    ADDRESS_XPATH = "//*[@id='basicBootstrapForm']/div[2]/div/textarea"
    EMAIL_ADDRESS_XPATH = "//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]"
    PHONE_NUMBER_XPATH = "//*[@id='basicBootstrapForm']/div[4]/div/input"
    GENDER_NAME = 'radiooptions'
    HOBBY1_ID = "checkbox1"
    HOBBY2_ID = "checkbox2"
    LANGUAGE_DROPDOWN_ID = "msdd"
    SKILL_ID = "Skills"
    COUNTRY_ID = "countries"
    DOB_YEAR_ID = "yearbox"
    DOB_MONTH_XPATH = '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select'
    DOB_DATE_ID  = "daybox"

    SET_PASSWORD_ID = "daybox"
    CONFIRM_PASSWORD_ID  = "secondpassword"
    UPLOAD_PROFILE_PICTURE_ID = "imagesrc"
    PROFILE_IMAGE_PATH = "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png"
    SUBMIT_BUTTON_ID = "submitbtn"


    """
    Test_Windown_Page
    """
    WINDOWS_PAGE_XPATH = "//*[@id='header']/nav/div/div[2]/ul/li[4]/ul/li[2]/a"
    TABBED_CLICK_WINDOW_XPATH = "//*[@id='Tabbed']/a/button"
    SEPERATE_WINDOW_XPATH = "//a[contains(text(),'Open New Seperate Windows')]"
    SEPERATE_CLICK_BUTTON_XPATH = "//*[@id='Seperate']/button"
    MULTIPLE_WINDOW_LABLE_XPATH = "//a[contains(text(),'Open Seperate Multiple Windows')]"
    MULTI_WINDOW_CLICK_BUTTON_XPATH = "//*[@id='Multiple']/button"






