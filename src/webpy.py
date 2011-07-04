import web

urls = ("/(.+)", "hello")
app = web.application(urls, globals(), autoreload=True)

class hello:
    def GET(self, name):
        return name


class session:
    
    render = web.template.render('templates')
    
    def GET(self):
        data = web.data()
        if 'topsession' in data:
            session = data['top_session']
            top_sign = data['top_sign']
        else:
            return 
        
if __name__ == "__main__":
    app.run()
