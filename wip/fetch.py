"""Download the official PDF into .cache/ (private)."""
import subprocess, pathlib
U = 'https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2024/07/20240716890312078.pdf'
d = pathlib.Path(__file__).parent / '.cache'; d.mkdir(exist_ok=True)
subprocess.run(['curl', '-sL', '-m', '180', '-o', str(d / 'coi.pdf'), U], check=True)
subprocess.run(['pdftotext', '-layout', str(d / 'coi.pdf'), str(d / 'coi.txt')], check=True)
