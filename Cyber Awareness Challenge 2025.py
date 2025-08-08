from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

cyber_awareness_answers = {
    "Matt is a government employee who needs to share a document containing source selection data with his supervisor. Which of the following describes the most appropriate way for Matt to do this?":
    "Encrypt it and send it via digitally signed Government e-mail.",
    
    "Which of the following statements is true of DoD Unclassified data?":
    "It must be cleared before being released to the public.",
    
    "Which of the following statements about Protected Health Information (PHI) is true?":
    "It is health information that identifies the individual.",
    
    "Which of the following is true of Controlled Unclassified Information (CUI)?":
    "It belongs to a defined category established in the DoD CUI Registry.",
    
    "When linked to a specific individual, which of the following is NOT an example of Personally Identifiable Information (PII)?":
    "Smartphone brand and model",
    
    "Tessa is processing payroll data that includes employees’ names, home addresses, and salary. Which of the following is Tessa prohibited from doing with the data?":
    "Using her home computer to print the data while working remotely",
    
    "Which type of data could reasonably be expected to cause damage to national security?":
    "Confidential",
    
    "Which of the following is a way to protect classified data?":
    "Store it in a GSA-approved container",
    
    "Who designates whether information is classified and its classification level?":
    "Original classification authority",
    
    "Which of the following is true of spillage?":
    "It can be either inadvertent or intentional.",
    
    "As you browse a social media site, you come across photos of information with classification markings. What should you do?":
    "Notify your security point of contact.",
    
    "Which of the following describes Sensitive Compartmented Information (SCI)?":
    "SCI introduces an overlay of security to Top Secret, Secret, and Confidential information.",
    
    "What are the requirements for access to Sensitive Compartmented Information (SCI)?":
    "Top Secret clearance and indoctrination into the SCI program",
    
    "Adam sees a coworker who does not have the required clearance with a printed document marked as Sensitive Compartmented Information (SCI). What should he do?":
    "Contact his security POC to report the incident.",
    
    "Which of the following provides precise, comprehensive guidance regarding specific program, system, operation, or weapon system elements of information to be classified?":
    "Security Classification Guide",
    
    "Which of the following is true of transmitting or transporting Sensitive Compartmented Information (SCI)?":
    "You must be courier-briefed for SCI to transport it.",
    
    "Which of the following is a best practice for physical security?":
    "Report suspicious activity",
    
    "Steve occasionally runs errands during virtual meetings. He joins the meetings using his approved government device. Does this pose a security concern?":
    "Yes. Eavesdroppers may be listening to Steve’s conversation.",
    
    "Which of the following is permitted when using an unclassified laptop within a collateral classified space?":
    "A personally-owned wired headset without a microphone",
    
    "Which of the following is true of working within a Sensitive Compartmented Information Facility (SCIF)?":
    "Badges must be worn while in the facility and removed when leaving the facility.",
    
    "Which of the following is true of Sensitive Compartmented Information Facilities (SCIFs)?":
    "Personnel should physically assess whether everyone within listening distance has a need-to-know before starting conversations involving classified information.",
    
    "Which of the following is permitted within a Sensitive Compartmented Information Facility (SCIF)?":
    "An authorized Government-owned Portable Electronic Device (PED)",
    
    "Under which Cyberspace Protection Condition (CPCON) is the priority focus limited to critical functions?":
    "CPCON 1",
    
    "Which of the following is an allowed use of government furnished equipment (GFE)?":
    "E-mailing your supervisor",
    
    "Which of the following is an appropriate use of government e-mail?":
    "Using a digital signature when sending hyperlinks",
    
    "Which of the following is a best practice for using government e-mail?":
    "Do not solicit sales",
    
    "Which of the following is an example of a strong password?":
    "bRobr@79l*P",
    
    "Which of the following would work in combination for two-factor authentication?":
    "Common Access Card (CAC) and Personal Identification Number (PIN)",
    
    "Which of the following is NOT an appropriate use of your Common Access Card (CAC)?":
    "Exchanging it for a visitor pass in another building",
    
    "Which of the following is an appropriate use of a DoD Public Key Infrastructure (PKI) token?":
    "Only leave it in a system while actively using it for a PKI-required task",
    
    "How can malicious code do damage?":
    "All of these",
    
    "How can you prevent viruses and malicious code?":
    "Scan all e-mail attachments",
    
    "Which of these is NOT a potential indicator that your device may be under a malicious code attack?":
    "An operating system update",
    
    "You receive a phone call from an unknown person asking for a directory name on your government furnished laptop so that a software update can be made. Which course of action should you take?":
    "Document the interaction and contact your security POC or help desk.",
    
    "You receive an e-mail with a link to run an anti-virus scan. Your IT department has not sent links like this in the past. The e-mail is not digitally signed. What action should you take?":
    "Report the e-mail to your security POC or help desk.",
    
    "You receive an e-mail marked important from your agency head asking you to call them using a number you do not recognize. The e-mail was sent from a personal e-mail address that you do not recognize, but it addresses you by name. What action should you take?":
    "This may be a spear phishing attempt. Report it to your security POC or help desk.",
    
    "You receive a text message from a vendor notifying you that your order is on hold due to needing updated payment information from you. It provides a shortened link for you to provide the needed information. What is the best course of action?":
    "Delete the message",
    
    "Which of the following is an example of removable media?":
    "Compact disc",
    
    "Which of the following uses of removable media is allowed?":
    "Sam uses approved Government owned removable media to transfer files between government systems as authorized.",
    
    "When allowed, which of the following is an appropriate use of removable media?":
    "Labeling media that contains personally identifiable information (PII)",

    "Which of the following is true of removable media and portable electronic devices (PEDs)?": 
    "The risks associated with them may lead to loss of life.",
    
    "How can you protect data on a mobile device?":
    "Use two-factor authentication",
    
    "How can you protect a mobile device while traveling?":
    "Connect with a Government VPN",
    
    "Does it pose a security risk to tap your smartwatch to pay for a purchase at a store?":
    "Yes, there is a risk that the signal could be intercepted and altered.",
    
    "When is the safest time to post on social media about your work-related travel?":
    "After the trip",
    
    "Which of the following is the safest to share on a social networking site?":
    "Your favorite movie",
    
    "How can you protect yourself on social networking sites?":
    "Validate connection requests through another source if possible",
    
    "As you scroll through your social media feed, a news headline catches your eye. What should you consider before sharing it with your connections?":
    "Whether the source is credible and reliable",
    
    "Which of the following is a best practice when browsing the Internet?":
    "Look for h-t-t-p-s in the URL name",
    
    "Which of the following is true of compressed URLs (e.g., TinyURL, goo.gl)?":
    "They may be used to mask malicious intent.",
    
    "John receives an e-mail about a potential shutdown of a major social service unless a petition receives enough signatures. Which of the following actions should John NOT take with the e-mail?":
    "Forward it",
    
    "Which of the following can be used to catalogue information about you?":
    "All of these",
    
    "Which of the following is a best practice to protect your identity?":
    "Ask how information will be used before giving it out",
    
    "How can you protect yourself from identity theft?":
    "Review your credit report annually",
    
    "What is an insider threat?":
    "Someone who uses authorized access, either wittingly or unwittingly, to harm national security.",
    
    "Which of the following is a potential insider threat indicator?":
    "Death of a spouse",
    
    "Based on the description provided, how many insider threat indicators are present? Edward has worked for a DoD agency for 2 years. He is an analyst who takes a great deal of interest in his work. He occasionally takes a somewhat aggressive interest in others’ work as well, including asking for classified details of their projects. He otherwise gets along well with his colleagues.":
    "1",
    
    "Which of the following is an example of behavior that you should report?":
    "Bringing a phone into a prohibited area",
    
    "Which of the following is a best practice for telework and remote work?":
    "Connect to your Government Virtual Private Network (VPN).",
    
    "Which of the following personally owned peripherals can you use with government furnished equipment (GFE)?":
    "A wired keyboard connected via USB",
    
    "Which of the following is a best practice for protecting your home wireless network for telework or remote work?":
    "Implement, as a minimum, Wi-Fi Protected Access 2 (WPA2) Personal encryption",
    
    "Which of the following poses a security risk while teleworking in an environment where Internet of Things (IoT) devices are present?":
    "All of these",
    
    "What is a best practice for creating user accounts for your home computer?":
    "Create separate accounts for each user and have each user create their own password"
    }

duplicate_questions = {
    "How can you protect your home computer?": {
        frozenset(["Use the administrator account for all users", "Decline security updates", "Disable the password feature", "Use legitimate, known antivirus software"]): "Use legitimate, known antivirus software",
        frozenset(["Disable firewall protection", "Turn off antivirus software scans", "Accept all mobile code", "Install spyware protection software"]): "Install spyware protection software",
    },
}

URL = "https://lms-jets.cce.af.mil/moodle/course/view.php?id=14124"
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(5) 

auth_button = driver.find_element(By.XPATH, "//div/button[@class='button-small']")
auth_button.click()

time.sleep(5)

pki_button = driver.find_element(By.ID, "pki-login")
pki_button.click()
time.sleep(10)

#click on launch the course link
launch_content = driver.find_element(By.XPATH, "//div[@class='activityname']/a[contains(@href, '292598')]")
launch_content.click()
time.sleep(7)

#click on the enter button with id = 'n'\
button = driver.find_element(By.ID, "n")
button.click()
time.sleep(20)

original_window = driver.current_window_handle
all_windows = driver.window_handles

for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break
        
print("Current window handle:", driver.current_window_handle)
print("Current window title:", driver.title)
print("Current window URL:", driver.current_url)

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
print("Switched to iframe.")

#click the save button
save_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn-purple')]"))
    )
save_button.click()
print("Save button clicked.")


forward_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'absolute left-[77px] bottom-[23px]')]"))
    )
for _ in range(29):
    forward_button.click()
    time.sleep(0.5)
    
next_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'absolute right-[19px] bottom-[23px]')]"))
    )
next_button.click()
time.sleep(10)

forward_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'absolute left-[77px] bottom-[23px]')]"))
    )
for _ in range(38):
    forward_button.click()
    time.sleep(0.5)
    
accept_challenge_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'absolute left-[423px] top-[366px]')]"))
    )
accept_challenge_button.click()


for _ in range(38):
    try:
        # Wait for the forward button to be clickable in each iteration
        forward_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'absolute left-[77px] bottom-[23px]')]"))
        )
        forward_button.click()
    except StaleElementReferenceException:
        print("Button was refreshed; retrying...")
        # Retry locating and clicking the button
        forward_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'absolute left-[77px] bottom-[23px]')]"))
        )
        forward_button.click()
    time.sleep(0.5)  # Adjust as necessary

next_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'absolute right-[19px] bottom-[23px]')]"))
    )
next_button.click()

knowledge_check_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'absolute left-[399px] top-[281px]')]"))
    )
knowledge_check_button.click()
time.sleep(5)


for i in range(25):  # Assuming there are 25 questions
    try:
        print(f"Processing question {i + 1}...")

        # Extract and normalize the question text
        question = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//legend[contains(@class, 'absolute left-[75px] top-[79px]')]"))
        ).text
        print(f"Extracted Question: {question}")

        # Locate the Submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='absolute right-[159px] bottom-[32px] btn-blue']"))
        )

        # Extract and normalize all answers
        # answers = [
            # {
                # "element": driver.find_element(By.ID, "sm-response-0"),
                # "text": driver.find_element(By.XPATH, "//label[@class='leading-tight' and @for='sm-response-0']").text
            # },
            # {
                # "element": driver.find_element(By.ID, "sm-response-1"),
                # "text": driver.find_element(By.XPATH, "//label[@class='leading-tight' and @for='sm-response-1']").text
            # },
            # {
                # "element": driver.find_element(By.ID, "sm-response-2"),
                # "text": driver.find_element(By.XPATH, "//label[@class='leading-tight' and @for='sm-response-2']").text
            # },
            # {
                # "element": driver.find_element(By.ID, "sm-response-3"),
                # "text": driver.find_element(By.XPATH, "//label[@class='leading-tight' and @for='sm-response-3']").text
            # }
        # ]
        
        answers = []
        for index in range(4):  # Check for up to 4 possible answers
            try:
                answer_element = driver.find_element(By.ID, f"sm-response-{index}")
                answer_text = driver.find_element(
                    By.XPATH, f"//label[@class='leading-tight' and @for='sm-response-{index}']"
                ).text
                answers.append({"element": answer_element, "text": answer_text})
            except NoSuchElementException:
                print(f"No element found for response {index}. Skipping...")
                continue
        
               # Create a set of answer texts
        answer_texts = frozenset([a["text"] for a in answers])

        # Handle duplicate questions
        if question in duplicate_questions:
            print("Duplicate question detected.")
            possible_answers = duplicate_questions[question]

            if answer_texts in possible_answers:
                correct_answer = possible_answers[answer_texts]
                print(f"Correct Answer: {correct_answer}")

                # Click the correct answer
                for answer in answers:
                    if answer["text"] == correct_answer:
                        answer["element"].click()
                        time.sleep(1)
                        submit_button.click()
                        print(f"Clicked answer: {answer['text']}")
                        break
            else:
                print(f"Answer options do not match known contexts: {answer_texts}")

        # Handle regular questions
        elif question in cyber_awareness_answers:
            correct_answer = cyber_awareness_answers[question]
            print(f"Correct Answer: {correct_answer}")

            # Click the correct answer
            for answer in answers:
                if answer["text"] == correct_answer:
                    answer["element"].click()
                    time.sleep(1)
                    submit_button.click()
                    print(f"Clicked answer: {answer['text']}")
                    break
        else:
            print(f"Question not found in any dictionary: {question}")
    
        time.sleep(2)
    except TimeoutException:
        print("Timed out while waiting for an element.")
        continue  # Retry the next question


time.sleep(15)