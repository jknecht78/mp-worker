python -m venv env-benchmark
env-benchmark\scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python create_sample_data.py