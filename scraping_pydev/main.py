"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
#path is /home/runner/pythonchallengedaylast
from so_extract import extraction_so
from wwr_extract import extraction_wwr
from rmt_extract import extraction_rmt
from save_csv import save

result_rmt=extraction_rmt('https://remoteok.io/remote-dev+python-jobs')
result_so=extraction_so('https://stackoverflow.com/jobs?r=true&q=python')
result_wwr=extraction_wwr('https://weworkremotely.com/remote-jobs/search?term=python')

save(result_so)
save(result_wwr)
#save(result_rmt)

print('All complete!!')