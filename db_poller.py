import json

x = [ { 'job_id': "1", 'status': "NOT_STARTED"}, { 'job_id': "2", 'status': "PR_APPROVED"}, { 'job_id': "3", 'status': "NOT_STARTED"}, { 'job_id': "1", 'status': "PR_APPROVED"} ]

print(json.dumps(x))