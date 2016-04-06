from flask import Flask, render_template, request, redirect, url_for
import sgsc
import os

app = Flask(__name__)

# Get hard-coded list of customers that have at least 3 different HAN plugs
f = open('data/customer_ids.txt', 'r')
c_keys = f.read().split(',')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('homepage.html', c_keys=c_keys)
    else:
        customer_id = request.form['customer_id']
        plug_list = sgsc.get_and_save_han_dynamo(customer_id.strip())
        return redirect(
                # TODO figure out how to pass an array.
                url_for('.select_plug', plug_list=str(plug_list)[1:-2],
                        customer_id=customer_id))


@app.route('/select_plug', methods=['GET', 'POST'])
def select_plug():
    if request.method == 'GET':
        plug_list = request.args['plug_list']
        # TODO figure out how to pass an array.
        plug_list = plug_list.replace(" '", '')
        plug_list = plug_list.replace("'", '')
        plug_list = plug_list.split(',')
        return render_template('/select_plug.html', plug_list=plug_list,
                               customer_id=request.args['customer_id'])
    else:
        plug = request.form['plug']
        return redirect(url_for('.plot', plug=plug))


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'GET':
        plug = request.args['plug']
        sgsc.static_bar_plot(plug)
        return render_template('/plot.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  # , debug=True)
    # app.run(debug=True)
