@app.route('/result')
def result():
    if not is_logged_in():
        return redirect(url_for('index'))

    return render_template('result.html')


if __name__ == "__main__":
    app.run(
        debug=False,
        port=5000
    )