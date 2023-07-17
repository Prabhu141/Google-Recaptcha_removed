from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get("http://example.com")

# Execute JavaScript code to open a pop-up after a delay of 1 second
driver.execute_script("""
    // Function to open the pop-up after a delay
    function openPopup() {
        setTimeout(function() {
            // Create a div element for the pop-up
            var popupDiv = document.createElement('div');
            popupDiv.style.position = 'fixed';
            popupDiv.style.top = '50%';
            popupDiv.style.left = '50%';
            popupDiv.style.transform = 'translate(-50%, -50%)';
            popupDiv.style.padding = '10px';
            popupDiv.style.backgroundColor = 'lightgray';

            // Create an input field within the pop-up
            var inputField = document.createElement('input');
            inputField.type = 'text';
            inputField.style.width = '200px';
            inputField.id = 'inputField';

            // Create a submit button within the pop-up
            var submitButton = document.createElement('button');
            submitButton.textContent = 'Submit';

            // Append the input field and submit button to the pop-up
            popupDiv.appendChild(inputField);
            popupDiv.appendChild(submitButton);

            // Append the pop-up to the body of the page
            document.body.appendChild(popupDiv);

            // Focus on the input field
            inputField.focus();

            // Event listener for form submission
            submitButton.addEventListener('click', function(e) {
                e.preventDefault();
                var inputData = inputField.value;
                //window.alert('Submitted data: ' + inputData);
                window.alert(inputData);
            });
        }, 1000); // Delay of 1 second
    }

    // Call the function to open the pop-up
    openPopup();
""")



# Wait for the alert and print the submitted data
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
submitted_data = alert.text
alert.accept()
print("Submitted data:", submitted_data)

# Close the WebDriver
driver.quit()