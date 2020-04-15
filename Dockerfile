FROM python:3
ADD mac_address_check.py /opt
ENV mac_address=""
CMD ["python", "/opt/mac_address_check.py"]
