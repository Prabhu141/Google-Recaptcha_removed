import tkinter as tk
from tkinter import ttk
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


win = tk.Tk()
win.minsize(800, 600)
win.title("Maximized Window")

# Maximize the window
win.attributes("-alpha", True)
win.title("Python GUI App")

ttk.Label(win, text="Selenium Automation").pack()

# Define the dropdown options
options = [
    "|   |___Web Design",
    "|   |___Web Design and Development"

]

# Create the combobox widget
combobox = ttk.Combobox(win, values=options)
combobox.pack()

driver = webdriver.Chrome()
def open_website():

            #-------------------------------------------------------------------------------
            # Setup
            Username = 0
            Email = 1
            URL = 2

            with open('data1.csv', 'r') as csv_file:

                csv_reader = csv.reader(csv_file)

            #-------------------------------------------------------------------------------
            # Web Automation

                for line in csv_reader:


                    # driver = webdriver.Chrome()
                    driver.get('https://unique-listing.com/submit.php')
                    driver.maximize_window()
                    #time.sleep(5)

                    element = driver.find_elements(By.NAME, 'CATEGORY_ID')
                    print('ok')
                    drp = Select(element[0])
                    selected_option = combobox.get()  # Get the selected option from the combobox
                    drp.select_by_visible_text(selected_option)
                    time.sleep(4)


                    Title_field = driver.find_element("xpath", '//*[@id="main"]/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input')
                    Title_field.send_keys(line[3])
                    time.sleep(3)

                    Url_field = driver.find_element("xpath", '//*[@id="main"]/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/input')
                    Url_field.send_keys(line[2])
                    time.sleep(3)


                    Description_field = driver.find_element("xpath", '//*[@id="main"]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/textarea')
                    Description_field.send_keys(line[4])
                    time.sleep(3)

                    Ownername_field = driver.find_element("xpath", '//*[@id="main"]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input')
                    Ownername_field.send_keys(line[0])
                    time.sleep(3)

                    Email_field = driver.find_element("xpath", '//*[@id="main"]/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/input')
                    Email_field.send_keys(line[1])
                    time.sleep(3)

                    submit = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div[2]/form/table/tbody/tr[9]/td/input')
                    submit[0].click()
                    print("completed")


button = ttk.Button(win, text="Open Website", command=open_website)
button.pack()
win.mainloop()   

    