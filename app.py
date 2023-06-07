from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/first')

def first():
    return render_template('first.html')

@FAI.route('/second')
def second():
    return render_template('second.html',name='Rahul',age=23)
if __name__=='__main__':
    FAI.run(debug=True)

if __name__=='__main__':
    FAI.run(debug=True)