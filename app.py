import os
import psutil
import platform
from flask import Flask, render_template

app = Flask(__name__)

# Retrieve configuration from environment variables
DEBUG = os.environ.get('FLASK_DEBUG', True)
HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
# Port = int(os.environ.get("PORT", 8000)) #default port = 5000

@app.route("/")
def index():
    try:
        # Retrieve CPU, memory, disk and system usage metrics
        cpu_metric = psutil.cpu_percent()
        mem_metric = psutil.virtual_memory().percent
        disk_metric = psutil.disk_usage('/').percent
        system_info = {
            'hostname': platform.node(),
            'cpu_count': psutil.cpu_count(),
            'disk_partitions': psutil.disk_partitions(),
        }

    except Exception as e:
        # Handle exceptions and provide an appropriate response
        message = f"An error occurred, Please fix the error and try me again!: {str(e)}"
        return render_template("error.html", message=message)

    # Determine if CPU usage is high
    if cpu_metric > 80:
        cpu_message = "Alert! CPU utilization is high, above 80%"
    else:
        cpu_message = "CPU utilization is normal"

    # Determine if Mem usage is high
    if mem_metric > 80:
        mem_message = "Alert! Memory utilization is high, above 80%"
    else:
        mem_message = "Memory utilization is normal"

    # Determine if Disk usage is high
    if disk_metric > 80:
        disk_message = "Alert! Disk utilization is high, above 80%"
    else:
        disk_message = "Disk utilization is normal"

    # Render the template with the metrics and message
    return render_template("index.html", cpu_metric=cpu_metric, cpu_message=cpu_message, mem_metric=mem_metric, mem_message=mem_message, disk_metric=disk_metric, disk_message=disk_message, system_info=system_info)

if __name__=='__main__':
    app.run(debug=DEBUG, host=HOST)
    # app.run(debug=DEBUG, host=HOST, port=Port)

