import subprocess

datasets= ['5hrdata.data','23-03-24-15-22.data','23-03-27-14-56.data','23-03-28-14-52.data','23-03-29-15-04.data','23-04-03-14-43.data','23-04-18-00-43.data','23-04-18-11-43.data','23-04-19-11-03.data']

script = 'muon.py'
for i in range(len(datasets)):
    subprocess.call(['python', script,'--data',datasets[i]])
    #print(i)