import pandas as pd
import re

bombard_count = 400
test_label = 'test1'
log_folder = 'bombard {}'.format(test_label)
worker1_task_count = 0
worker2_task_count = 0

task_record  = pd.DataFrame(index=range(bombard_count))
task_record['execute_count'] = 0

with open('./{}/worker1-{}.log'.format(log_folder, test_label)) as worker1_log:
    for line in worker1_log:
        if 'Received task:' in line:
            worker1_task_count += 1
        elif 'This is the message received:' in line:
            find_label = re.search('Hello World (.+?) !', line)
            if find_label:
                task_label = int(find_label.group(1))
                task_record.loc[task_label, 'execute_count'] += 1

with open('./{}/worker2-{}.log'.format(log_folder, test_label)) as worker2_log:
    for line in worker2_log:
        if 'Received task:' in line:
            worker2_task_count += 1
        elif 'This is the message received:' in line:
            find_label = re.search('Hello World (.+?) !', line)
            if find_label:
                task_label = int(find_label.group(1))
                task_record.loc[task_label, 'execute_count'] += 1
