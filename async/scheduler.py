import asyncio
from time import time
from random import randint


async def job(name, future=None):
	start = time()
	print('{} is scheduled'.format(name))
	op_time = randint(3,10)
	await asyncio.sleep(op_time)
	diff = time()-start
	result = '{} is done in {:.2f}'.format(name, diff)
	if future:
		future.set_result(result)
	else:
		return result


def on_fetch(function):
	print(function.result())


async def scheduler(name, future=None):
	task = asyncio.ensure_future(job(name, future))
	await asyncio.wait([task])
	if future:
		future.add_done_callback(on_fetch)
	else:
		task.add_done_callback(on_fetch)


main_start = time()
looper = asyncio.get_event_loop()
task1 = asyncio.ensure_future(scheduler('Task-1'))
future = asyncio.Future()
task2 = asyncio.ensure_future(scheduler('Task-2', future))
looper.run_until_complete(asyncio.gather(task1, task2))
main_diff = time() - main_start
print('script took: {:.2f} to complete all tasks'.format(main_diff))
looper.close()