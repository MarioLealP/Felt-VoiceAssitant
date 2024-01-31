python -m venv .
call Scripts\activate.bat
python -m pip install setuptools wheel pip -U
pip install -r requirements.txt
python start.py
