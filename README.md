# playwrightTutorial

# Pytest CLI Command
# pytest -x           # stop after first failure
# pytest --maxfail=2  # stop after two failures
# pytest -k "MyClass and not method" # Run tests by keyword expressions. Can be used to run specific single test
# pytest -lf          # Run Last Failed test only
# pytest -ff          # Run All test start from Last Failed test

# Generate Report using Pytest with pytest-reporter-html1 library
# pytest --template=html1/index.html --report=report.html

# Running Pytest in parallel using pytest-xdist library
# pytest -n auto
# pytest -n NUMCPUS # Replace "NUMCPUS" with number - based on your CPU capabilities

# Running Pytest using ready-made playwright fixture to setup some options
# Headless mode OFF: pytest -k <test_file.py> --headed

# some other options:
# --browser             : To run different browser e.g.: chromium, firefox, etc. By default is Chromium
# In order to use different browser, we need to install that browser using playwright
# e.g.: playwright install firefox
# We can chain different browser into one CLI: "pytest -v --headed --browser chromium --browser firefox"

# --browser-channel     : To run different browser channel
# Browser channel is when we want to test it on browser installed in our machine. e.g.: chrome

# --slowmo              : To run in slow motion
# --device              : To run which device

# --video               : To run the test with recording. The value must be "on", "off", OR "retain-on-failure". Default is Off
# e.g.: pytest -k <test_file.py> --headed --video=retain-on-failure
# By default, it will create a new folder test-results
# But we can rename this folder with different name by adding --output=
#   .e.g.: pytest -k <test_file.py> --headed --video=retain-on-failure --output=video_rec_test_result

# --screenshot          : To automatically run screenshot. The value must be "on", "off", OR "retain-on-failure".
# By default, it will create a new folder test-results
# But we can rename this folder with different name by adding --output=
#   .e.g.: pytest -k <test_file.py> --headed --video=retain-on-failure --output=screenshot_test_result
# e.g.: pytest -k <test_file.py> --headed --screenshot=retain-on-failure

# --base-url            : To specify bas url