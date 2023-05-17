## Small testing of web page using selenium

---
- Input user data  
- Click button  
- Сreating a screenshot of webpage  

**Local testing:**
```bash
python -m venv venv
. venv/bin/activate

python -m pip install --upgrade pip
pip install -r selenium/requirements.txt

python selenium/selenium_local.py

# Check .../selenium/screenshot   folder
```

**Docker testing:**
```bash
cd selenium/

sudo docker build -t selenium_test .

sudo docker run -v $(pwd)/screenshots:/app/screenshots --name selenium selenium_test
# sudo docker run -d -v $(pwd)/screenshots:/app/screenshots --name selenium selenium_test

# Check .../selenium/screenshot   folder
```