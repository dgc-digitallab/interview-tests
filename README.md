# Setup

```bash
virtualenv -p python2 venv
```

```bash
source venv/bin/activate
pip2 install -r requirements.txt
```

# Test if an exercice is valid

```bash
source venv/bin/activate
python2 -m pytest test.py
```