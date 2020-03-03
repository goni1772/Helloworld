from flask import Flask #flask 호출

app = Flask(__name__) #flask 객체 생성

@app.route('/') #기본 route설정 '/' 는 로컬호스트을 의미(http://127.0.0.1:5000)
def default():
    return 'default page'

@app.route('/helloworld')  #기본 route뒤에 URL 추가하여 routing 설정(http://127.0.0.1:5000/helloworld)
def hello():
    return 'hello world'

if __name__ == '__main__': #해당 코드를 실행 시 최초에 생성한 객체(Flask)를 실행하겠다고 선언
    app.run()
