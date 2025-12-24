import time
from rq import get_current_job

def example(seconds):
    job = get_current_job()
    print("starting task")
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()
        print(i)
        time.sleep(1)
    
    job.meta['progress'] = 100
    job.save_meta()

    print("task completed")

# STARTING WORKER
# (venv) ubuntu@vagrant:~/microblog$ rq worker microblog-tasks

# TEST RUN JOB FROM FLASK SHELL
# >>> from redis import Redis
# >>> import rq
# >>> queue = rq.Queue('microblog-tasks', connection=Redis.from_url('redis://'))
# >>> job = queue.enqueue('app.temp.example',14)
# >>> job.refresh()
# >>> job.meta
# {'progress': 5.0}
# >>> job.meta
# {'progress': 5.0}
# >>> job.refresh()
# >>> job.meta
# {'progress': 45.0}
# >>> job.refresh()
# >>> job.meta
# {'progress': 60.0}
# >>> job.refresh()
# >>> job.meta
# {'progress': 95.0}
# >>> job.refresh()
# >>> job.meta
# {'progress': 100}
# >>> job.is_finished
# True
######################################