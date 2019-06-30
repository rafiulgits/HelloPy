from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

from tornado.httpclient import HTTPClient

class RootController(RequestHandler):
	def get(self):
		print('[LOG] Root called')
		self.write('Server root<br><a href="/task/">Task</a>')


class TaskController(RequestHandler):
	def get(self):
		print('[LOG] Task called')
		self.write('Task')


urlpatterns = [
	(r'/', RootController),
	(r'/task/', TaskController)
]

def init():
	app = Application(urlpatterns)
	app.listen(8888)
	looper = IOLoop.current()
	print('[LOG] Server starting...')
	looper.start()


if __name__ == '__main__':
	init()