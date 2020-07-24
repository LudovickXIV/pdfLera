import datetime
import pdfkit

date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
print(date_time)

options = {
    'page-size': 'A4',
    'dpi': 130,
    'encoding': 'UTF-8',
    'no-outline': None
}
logf = open("script.log", "w")

try:
    pdfkit.from_file('source/EXAMPLE/index.html', 'output/' + date_time + '.pdf', options=options)
except Exception as e:
    logf.write(str(e))