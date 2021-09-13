import simplejson as json
from init import Configuration, app
import routes.GoalPage
import routes.JournalPage
import routes.LikePage
import routes.PicturePage
import routes.UserPage

@app.route('/')
def hello_name():
   return 'Hello Taqi!'


if __name__ == '__main__':
   if Configuration.TESTING:
        SESSION_COOKIE_SECURE = False
        app.run(debug=True, port=Configuration.PORT)