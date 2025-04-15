import os
import json
from datetime import datetime
from selenium import webdriver

code = """
x = y
x = 2y
x = 2y + 3
...
<put your code here>
"""

driver: webdriver.Chrome | None = None

try:
    driver = webdriver.Chrome()
    driver.get("https://www.desmos.com/calculator")

    active = driver.switch_to.active_element
    active.send_keys(code.strip())
    state = driver.execute_script("return Calc.getState();")

    os.makedirs("graphs", exist_ok=True)
    format_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"graphs/{format_time}.json", "w") as f:
        json.dump(state, f)

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
