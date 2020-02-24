from subprocess import Popen

chrome_cmd = 'export BROWSER=chrome && python functional_tests.py'
firefox_cmd = 'export BROWSER=firefox && python functional_tests.py'
Popen(chrome_cmd, shell=True)
Popen(firefox_cmd, shell=True)
