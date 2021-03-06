from sio.executors import common
#from sio.workers.executors import VCPUExecutor
from sio.workers.executors import IsolateExecutor, Terrarium2Executor

def run(environ):
    if environ['exec_info']['mode'] == 'python3':
        return common.run(environ, Terrarium2Executor())
    else:
        return common.run(environ, IsolateExecutor())
