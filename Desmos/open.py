import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = "graphs/<your_graph_name>.json"

driver: webdriver.Chrome | None = None

try:
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.desmos.com/calculator")

    with open(path, "r") as f:
        state = json.load(f)

    driver.execute_script("Calc.setState(arguments[0]);", state)

except Exception as e:
    print(f"Error: {e}")
